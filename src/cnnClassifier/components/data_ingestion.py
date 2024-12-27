import os
from pathlib import Path
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
                
                # check if file is not empty
                if os.path.getsize(self.config.local_data_file) == 0:
                    raise Exception(f"downloaded file is empty")
            except Exception as e:
                logger.error(f"error downloading the file: {e}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))} bytes")


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # check file size before extraction
        if os.path.getsize(self.config.local_data_file) > 0:
            try:
                with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                    zip_ref.extractall(unzip_path)
                logger.info(f"file extracted successfully to {unzip_path}")
            except zipfile.BadZipFile:
                logger.error(f"corrupted zip file: {self.config.local_data_file}")
                raise
            except Exception as e:
                logger.error(f"error during extraction: {e}")
                raise
        else:
            logger.error("file is empty or not downloaded properly")
            raise Exception("invalid zip file: file is empty or corrupted.")