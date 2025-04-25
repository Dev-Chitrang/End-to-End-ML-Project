import os
from MLProject.entity.config_entity import DataIngestionConfig
import urllib.request as request
import zipfile
from MLProject import logger
from MLProject.utils.common import get_size
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_path
            )
            logger.info(f"{filename} download! with the following info: \n{headers}")
        else:
            logger.info(f"Filename already exists of size: {get_size(Path(self.config.local_data_path))}")
    
    def extract_zip(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory.
        Function return None.
        '''

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)