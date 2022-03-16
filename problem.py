import os
import pandas as pd
import rampwf as rw
from rampwf.score_types.base import BaseScoreType
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np


problem_title = 'FootballResults5League'
_target_column_name = 'FTR'

_prediction_label_names = ['H', 'A', 'D']

Predictions = rw.prediction_types.make_multiclass(label_names=_prediction_label_names)

workflow = rw.workflows.Classifier()

score_types = [
    rw.score_types.Accuracy(name='acc'),
]

def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, f_name), sep=',')
    y_array = data['FTR'].values
    X_df = data.drop(['FTR'], axis=1)
    return X_df, y_array

def get_train_data(path='./data/'):
    f_name = 'data_train.csv'
    return _read_data(path, f_name)

def get_test_data(path='./data/'):
    f_name = 'data_test.csv'
    return _read_data(path, f_name)

def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=8, test_size=0.20, random_state=42)
    return cv.split(X, y)
