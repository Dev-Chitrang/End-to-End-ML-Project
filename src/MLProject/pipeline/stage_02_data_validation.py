from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_validation import DataValidation
from MLProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidaionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = DataValidaionTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
