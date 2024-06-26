# MLOps- credit risk analysis project for JPMorgan Chase & Co.
*The dataset used in this project is for demonstration purpose only.*


#  Workflow
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run the project?

### Steps:

Clone the repository

```bash
https://github.com/arijal23pdf/mlops_credit_risk
```

Create a conda environment after opening the repository
```bash
conda create -p venv python==3.8 -y
```

Activate the conda environment
```bash
conda activate venv
```

Install requirements
```bash
pip install -r requirements.txt
```

Run app.py
```bash
python app.py
```

Open up your local host and port
```bash
Open up your local host and port
```

MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

Running MLflow locally
```bash
mlflow ui
```

Storing remotely with
[Dagshub](https://dagshub.com/)

Create a .env file

```bash
vi .env
```

Add your mlflow related environment variables to .env file. Example:

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/arijal23pdf/mlops_credit_risk.mlflow
MLFLOW_TRACKING_USERNAME=<username>
MLFLOW_TRACKING_PASSWORD=<password>
```

AWS CICD
1. Log in to AWS console.
2. Create IAM user for deployment
```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 machine
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

6. Configure EC2 as self-hosted runner
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

7. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION

AWS_ECR_LOGIN_URI

ECR_REPOSITORY_NAME
```

# References:
1. Project description: JPMorgan Chase and Co. (https://www.theforage.com/simulations/jpmorgan/quantitative-research-11oc)
2. MLOps tutorial: https://www.youtube.com/watch?v=pxk1Fr33-L4&ab_channel=KrishNaik
