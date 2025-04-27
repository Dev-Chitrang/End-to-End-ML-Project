import pandas as pd
import os
from pathlib import Path
from MLProject import logger
from MLProject.utils.common import save_json
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import numpy as np
from MLProject.entity.config_entity import ModelEvaluationConfig

# Function to convert numpy types inside a dictionary
def convert_numpy_in_dict(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_in_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_in_dict(item) for item in obj]
    elif isinstance(obj, (np.integer, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64)):
        return float(obj)
    elif isinstance(obj, np.bool_):
        return bool(obj)
    else:
        return obj

# Model Evaluation Class
class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def eval_model(self):
        model = joblib.load(self.config.model_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        pred_y = model.predict(test_x)

        # Get structured classification report
        report = classification_report(test_y, pred_y, output_dict=True)

        # Get confusion matrix
        matrix = confusion_matrix(test_y, pred_y)

        scores = {
            "classification_report": report,
            "confusion_matrix": {
                "labels": list(model.classes_),
                "matrix": matrix.tolist()
            }
        }

        # Convert numpy types BEFORE saving
        clean_scores = convert_numpy_in_dict(scores)

        save_json(path=Path(self.config.metric_file_name), data=clean_scores)
