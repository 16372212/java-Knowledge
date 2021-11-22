import os
import sys
import json
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

color = sns.color_palette()
sns.set(style='whitegrid', color_codes=True)

from pandas_profiling import ProfileReport
import sweetviz as sv
import jsonlines
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.linear_model import LogisticRegression as lrc
from sklearn.metrics import accuracy_score, roc_curve
from xgboost import XGBClassifier
from xgboost import plot_importance

import warnings
def ignore_warn(*args,**kwargs):
    pass
warnings.warn=ignore_warn


# input_data_path = '/home/admin/workspace/job/input/train.jsonl'
# output_model_path = '/home/admin/workspace/job/output/'
# result_path = '/home/admin/workspace/job/output/'
input_data_path = '/mnt/atec/train.jsonl'
output_model_path = './result/'
result_path = './result/validate_result.json'


def grid_search(x_, y_, model, args):
    grid = GridSearchCV(model, param_grid=args, cv=10)
    grid.fit(x_, y_)
    return grid.best_params_, grid.best_score_


def model_train(model, X_train, y_train):
    clf = model()
    clf.fit(X_train, y_train)
    train_accurate = accuracy_score(y_train, clf.predict(X_train))
    print(f"train accuracy:{train_accurate:.3%}")
    return clf


def train2():
    with open(input_data_path, 'r', encoding='utf-8') as fp:
        for item in jsonlines.Reader(fp):
            print(item)
        pass
    return True


def train():
    raw_data = []
    with open(input_data_path, 'r', encoding='utf-8') as fp:
        for item in jsonlines.Reader(fp):
            raw_data.append(item)
        pass
    raw_data = pd.DataFrame(raw_data)

    # train_data_path = input_data_path
    # raw_data = pd.read_json(train_data_path,encoding='utf-8',lines=True)

    # 缺失值处理
    train = raw_data
    train_na = (train.isnull().sum() / len(train)) * 100
    train_na = train_na.drop(train_na[train_na == 0].index).sort_values(ascending=False)[:30]

    # 数据预处理
    ## 3.1 去除所有含有-1111的数据
    raw_data = raw_data.drop(raw_data[(raw_data['x0']==-1111)].index)

    ## 3.2 去掉此时只有⼀个值的变量

    columns = raw_data.columns.values.tolist()
    drop_list = []
    for col in columns:
        num = len(raw_data[col].unique())
        if num == 1:
            drop_list.append(col)

    raw_data = raw_data.drop(columns = drop_list)

    ## 3.3 处理缺失值
    raw_data['x375'] = raw_data['x375'].fillna(raw_data['x375'].mode()[0])

    # 4 划分数据集
    y_train = raw_data['label']
    X_train = raw_data
    X_train.drop(['label'], axis=1, inplace=True)
    X_train.drop(['memo_polish'], axis=1, inplace=True)

    # 5 训练
    lr_classifier = model_train(lrc, X_train, y_train)
    lr_model_path = output_model_path+'lr_model.dat'
    # lr_classifier.save_model(lr_model_path)
    lr_train_accurate = accuracy_score(y_train, lr_classifier.predict(X_train))

    rfc_classifier = model_train(rfc, X_train, y_train)
    rfc_model_path = output_model_path+'rfc_model.dat'
    # rfc_classifier.save_model(rfc_model_path)
    rfc_train_accurate = accuracy_score(y_train, rfc_classifier.predict(X_train))

    xgb_model = XGBClassifier()
    xgb_model.fit(X_train, y_train)
    xgb_train_accurate = accuracy_score(y_train, xgb_model.predict(X_train))

    with open(rfc_model_path,"wb") as myprofile:
        pickle.dump(rfc_classifier, myprofile)

    with open(result_path, 'w') as fp:
        # 任务结果信息，可以在训练执行完后查看
        json.dump({"rfc_train_accurate":rfc_train_accurate, "lr_train_accurate":lr_train_accurate, "xgb_train_accurate": xgb_train_accurate}, fp)
        fp.close()

    return True

if __name__ == '__main__':
    if train():
        # 训练成功一定要以0方式退出
        sys.exit(0)
    else:
        # 否则-1退出
        sys.exit(1)