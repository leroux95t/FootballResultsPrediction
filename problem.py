import os
import pandas as pd
import rampwf as rw
from rampwf.score_types.base import BaseScoreType
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np





problem_title = 'FootballResults'
_target_column_name = 'Result'

_prediction_label_names = ['0', '1', '2']

Predictions = rw.prediction_types.make_multiclass(label_names=_prediction_label_names)

workflow = rw.workflows.Classifier()

score_types = [
    rw.score_types.Accuracy(name='acc'),
]


def _read_data(path, f_name):
    
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    y_array = data['Result'].values
    X_df = data.drop(['Result'], axis=1)

    X_array = X_df.to_numpy()
    return X_array, y_array

def get_train_data(path='.'):
    f_name = 'data_train.csv'
    return _read_data(path, f_name)

def get_test_data(path='.'):
    f_name = 'data_test.csv'
    return _read_data(path, f_name)

def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=3, test_size=0.20, random_state=42)
    return cv.split(X, y)
