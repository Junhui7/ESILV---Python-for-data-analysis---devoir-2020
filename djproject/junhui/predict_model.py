from pandas import DataFrame
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn import metrics
from sklearn.metrics import roc_auc_score
import numpy as np


def final_data():
    read_data = pd.read_csv("/Users/Junhui/Desktop/ESILV_5A/Python for Data Analysis/final_data.csv")
    fdata = DataFrame(read_data)
    return fdata


df = final_data()

X = df.loc[:,
    ['chest_ACC_0_mean', 'chest_ACC_1_mean', 'chest_ACC_2_mean', 'chest_ECG_mean', 'chest_EMG_mean', 'chest_EDA_mean',
     'chest_Temp_mean', 'chest_Resp_mean', 'wrist_ACC_0_mean', 'wrist_ACC_1_mean', 'wrist_ACC_2_mean', 'wrist_BVP_mean',
     'wrist_EDA_mean', 'wrist_TEMP_mean']]
y = df['Activity_Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


def rf_model():
    hyper_rf = {"n_estimators": 10,
                "max_features": 10,
                "max_depth": 50, }
    model_rf = RandomForestClassifier(**hyper_rf)
    model_rf.fit(X_train, y_train)
    return model_rf


def rf_predict(model_rf, p_data):
    final_data = [np.array(p_data)]
    return model_rf.predict(final_data)


def rf_score(model_rf):
    return model_rf.score(X_test, y_test)


def rf_hyper_score(n_estimators, max_features, max_depth):
    hyper_rf = {"n_estimators": n_estimators,
                "max_features": max_features,
                "max_depth": max_depth, }
    model_rf = RandomForestClassifier(**hyper_rf)
    return model_rf.fit(X_train, y_train).score(X_test, y_test)

