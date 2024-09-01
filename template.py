import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO,format = "[%(asctime)s] : %(message)s:")

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/Mr_Bot.ipynb",
    "app.py",
    "store_index.py",
    "static",
    "templates/chat.html"
    ]

for filepath in list_of_files:

    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created Directory {filedir} for file name {filename}")

    if(not os.path.exists(filepath) or os.path.getsize(filename==0)):
        with open(filename,"w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f"fileName {filename} aldready created")



