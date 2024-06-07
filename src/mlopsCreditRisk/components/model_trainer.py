import pandas as pd
import os
from mlopsCreditRisk import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from mlopsCreditRisk.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        target_column = self.config.target_column

        train_x = train_data.drop([target_column], axis=1)
        test_x = test_data.drop([target_column], axis=1)
        train_y = train_data[target_column]
        test_y = test_data[target_column]

        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators,  min_samples_split=self.config.min_samples_split, min_samples_leaf=self.config.min_sample_leaf, random_state = 42)

        rfc.fit(train_x, train_y)

        joblib.dump(rfc, os.path.join(self.config.root_dir, self.config.model_name))