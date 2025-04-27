import os
from MLProject import logger
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from MLProject.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path)
    
    def Transform(self):
        data = self.data
        # print(data.columns.to_list())
        # print(data['quality'].value_counts())
        data['quality'] = data['quality'].apply(lambda y: 1 if y >= 6 else 0 )
        # print(data.columns.to_list())
        # print(data['quality'].value_counts())
        data.drop(columns=['Id'], inplace=True)
        
        train, test = train_test_split(data, test_size=0.2, random_state=101)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Standardized and split the data into training and testing sets.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")
        
        print(train.shape)
        print(test.shape)
