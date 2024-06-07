import os
from mlopsCreditRisk import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlopsCreditRisk.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def drop_features(self, X_data):
        temp_X = X_data.copy(deep=True)
        temp_X.drop(columns=self.config.all_drop_features.customer_id, inplace=True)
        return temp_X

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        drop_data = self.drop_features(data)

        # Split the data into training and testing sets. (0.75, 0.25) split.
        train, test = train_test_split(drop_data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)