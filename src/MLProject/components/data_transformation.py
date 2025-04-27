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
        scaler = StandardScaler()
        input_columns = data.drop(columns=[data.columns[-1]])
        target_column = data[data.columns[-1]]
        scaled_input = scaler.fit_transform(input_columns)
        scaled_input = pd.DataFrame(scaled_input, columns=input_columns.columns)
        scaled_input['quality'] = target_column.values
        scaled_input['quality'] = scaled_input['quality'].apply(lambda y: 1 if y >= 6 else 0 )
        
        train, test = train_test_split(scaled_input, test_size=0.2, random_state=101)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Standardized and split the data into training and testing sets.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")
        
        print(train.shape)
        print(test.shape)
