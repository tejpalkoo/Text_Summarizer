
# Here we will create structure of thefiles of our project 
import os
from pathlib import Path
import logging

project_name='textsummarizer'
project_path = Path(os.getcwd())
print(project_path)

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
# List all the required files:

list_files=[
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    ]

for filepath in list_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    # we will only create file when file do not exits and there is no code in the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")
    
    else:
        logging.info(f"File {filepath} already exists")

# Branch created