import os
from box.exceptions import BoxValueError
import yaml
from MLProject import logger
import json
import joblib
from ensure import ensure_annotations # Enforces that arguments passed to a function adhere to the specified type annotations
from box import ConfigBox # Manage the configuration data (file) in an intuitive way. (In dictionary we can directly access values using '.' directly)
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yamal(path_to_yaml: Path) -> ConfigBox:
    '''
    Reads the yaml file and resutn.
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if the yaml file is empty
        e: empty file
    Return:
        ConfigBox: ConfigBox type
    '''

    try:
        with open(path_to_yaml) as yf:
            content = yaml.safe_load(yf)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    
    except BoxValueError:
        return ValueError("yaml file is empty.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose:True):
    '''
    Create list of directories.

    Args:
        path_to_directories (list): List of the paths of directories.
        ignore_log (bool, optional): Ignores if multiple directories are to be created. Default to False.
    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path:Path, data: dict):
    '''
    Saves the data in json file.

    Args:
        path (Path): path of the json file.
        data (dict): data to be saved in json.  
    '''
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''
    Loads the json file.

    Args:
        path (Path): path to json file.
    
    Returns:
        ConfigBox: data as class attributes instead of dict.
    '''

    with open(path) as f:
        content = json.load(f)
    logger.info(f"Json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    '''
    Saves the binary file. 

    Args:
        data (Any): data to be saved.
        path (Path): path of the binary file. 
    '''
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    '''
    Loads the binary file.

    Args:
        path (Path): path to binary file.
    
    Returns:
        Any: Object stored in the file.
    '''

    data = joblib.load(path)
    logger.info(f"Binary file loaded succesfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get the size of file in KB's.

    Args:
        path (Path): path of the file.
    
    Retunts:
        str: size of file in KB's.
    '''
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"

