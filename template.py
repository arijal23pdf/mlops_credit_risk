import os
from pathlib import Path
import logging

# string for logging messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# project name
project_name = "mlopsCreditRisk"

# project structure: list of files (including constructor files)
list_of_files = [
    ".github/workflows/.gitkeep", # .github/workflows/ for CICD deployment using github actions. .gitkeep isn't a feature of git, but a practice to track an empty directory. By putting this .gitkeep file, git now tracks the directory in which the file resides- because git doesn't track empty directories. So, basically, you can name the file anything!
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # keep all the project's configurations here.
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/exercises.ipynb",
    "templates/index.html",
    "test.py"
]

# loop through the list of files (in project structure) and create them
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists.")