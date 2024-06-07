from sklearn import metrics
import os
import pandas as pd
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlopsCreditRisk.entity.config_entity import ModelEvaluationConfig
from mlopsCreditRisk.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):

        accuracy_score = metrics.accuracy_score(actual, pred)
        tn, fp, fn, tp = metrics.confusion_matrix(actual, pred).ravel()
        fpr, tpr, thresholds = metrics.roc_curve(actual, pred)
        roc_auc = metrics.auc(fpr, tpr)
        
        return accuracy_score, roc_auc, tn, fp, fn, tp
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predictions = model.predict(test_x)

            accuracy_score, roc_auc, tn, fp, fn, tp =  self.eval_metrics(test_y, predictions)

            all_scores = {"accuracy_score": accuracy_score, "roc_auc": roc_auc, "tn": tn, "fp": fp, "fn": fn, "tp": tp}
            save_json(path=Path(self.config.metric_file_name), data=all_scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy_score", accuracy_score)
            mlflow.log_metric("roc_auc", roc_auc)
            mlflow.log_metric("tn", tn)
            mlflow.log_metric("fp", fp)
            mlflow.log_metric("fn", fn)
            mlflow.log_metric("tp", tp)

            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestModel")
            else:
                mlflow.sklearn.log_model(model, "model")
