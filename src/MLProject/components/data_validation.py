import pandas as pd
from MLProject.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)

            actual_columns = list(data.columns)
            expected_columns = list(self.config.all_schema.keys())

            if actual_columns != expected_columns:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write("Validation failed: Columns do not match expected schema.\n")
                    f.write(f"Expected columns: {expected_columns}\n")
                    f.write(f"Actual columns: {actual_columns}\n")
                return validation_status

            actual_dtypes = data.dtypes
            expected_dtypes = list(self.config.all_schema.values())

            mismatched_dtypes = []
            for col, expected_dtype in zip(actual_columns, expected_dtypes):
                if str(actual_dtypes[col]).lower() != expected_dtype.lower().replace(" ", ""):
                    mismatched_dtypes.append((col, str(actual_dtypes[col]), expected_dtype))

            if mismatched_dtypes:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write("Validation failed: Data types do not match expected schema.\n")
                    for col, actual, expected in mismatched_dtypes:
                        f.write(f"Column: {col}, Expected: {expected}, Actual: {actual}\n")
                return validation_status

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Validation passed: All columns and data types are valid.\n")

            return validation_status

        except Exception as e:
            raise e
