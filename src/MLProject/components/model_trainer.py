import pandas as pd
import os
from MLProject import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from MLProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]


        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators)
        rfc.fit(train_x, train_y.values.ravel())
        logger.info(f"Model training completed.")

        joblib.dump(rfc, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model saved.")
        