import os
import urllib.request as request
import zipfile
import requests
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a browser request
                response = requests.get(self.config.source_URL, headers=headers, stream=True, timeout=30)
                response.raise_for_status()  # Raise error if request fails

                with open(self.config.local_data_file, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)

                logger.info(f"{self.config.local_data_file} downloaded successfully!")

            except requests.exceptions.RequestException as e:
                logger.error(f"Error downloading file: {e}")
                raise

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)