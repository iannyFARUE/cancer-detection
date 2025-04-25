from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.yaml",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    path_obj = Path(filepath)
    filedir, filename = os.path.split(path_obj)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
# Create a README file
readme_path = Path("README.md")
if not readme_path.exists():
    with open(readme_path, 'w') as f:
        f.write("# Project Title\n\n")
        f.write("## Description\n\n")
        f.write("## Installation\n\n")
        f.write("## Usage\n\n")
    logging.info(f"Creating file: {readme_path}")
else:
    logging.info(f"File already exists: {readme_path}")
    
# Create a requirements.txt file
requirements_path = Path("requirements.txt")
if not requirements_path.exists():
    with open(requirements_path, 'w') as f:
        f.write("# Add your project dependencies here\n")
    logging.info(f"Creating file: {requirements_path}")
else:
    logging.info(f"File already exists: {requirements_path}")