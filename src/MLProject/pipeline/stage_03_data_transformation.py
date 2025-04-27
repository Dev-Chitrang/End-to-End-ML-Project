from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_transformation import DataTransformation
from MLProject import logger

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transfromation = DataTransformation(config=data_transformation_config)
        data_transfromation.Transform()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
