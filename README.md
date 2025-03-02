# Text-Summarizer-Project

## STEPS:

### Clone the repository

https://github.com/ankitpatil3003/Text-Summarizer-Project

## STEPS 01 - Create a conda environment after opening the repository

conda create -n textS python=3.8 -y

conda activate textS

## STEPS 02 - Install the requirements

pip install -r requirements.txt

python app.py

### Now,

Open system local host and port 


Author: Ankit  Patil
Email: ankitpatil3003@gmail.com

## AWS CI/CD Deployment with Github Actions

### 1. Login to AWS Console.

### 2. Create IAM user for deployment

with specific access
1. EC2 access: It is a virtual machine
2. ECR: Elastic Container Registory to save your docker image in AWS

Description: About the deployment
1. Build docker image of the scoure code
2. Push your docker image to ECR
3. Luanch your EC2
4. Pull your image from ECR to EC2
5. Luanch your docker image in EC2

Policy:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save docker image

- Save the URI: public.ecr.aws/l7c7f4a9/text-s

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and install docker in EC2 Machine:

optinal
sudo apt-get update -y
sudo apt-get upgrade
required
curl -faSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo udermod -aG docker ubuntu
newgrp docker

### 6. Configure EC2 as self-hosted runner:

settings>actions>runner>new self hosted runner> choose os> then run command one by one

### 7. Setup github secrets:

AWS_ACCESS_KEY_ID=xxxxxxxxxxxx

AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  public.ecr.aws/l7c7f4a9/text-s

ECR_REPOSITORY_NAME = text-s


## Workflow
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Updatethe configuration manager in src config
5. Update the components
6. Update the pipelinne
7. Update the main.py
8. Update the app.py