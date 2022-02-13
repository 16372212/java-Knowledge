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
import logging
import jsonlines

color = sns.color_palette()
sns.set(style='whitegrid', color_codes=True)

from pandas_profiling import ProfileReport
import sweetviz as sv

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
#output_predictions_path = '/home/admin/workspace/job/output/predictions.jsonl'
output_predictions_path = './result/predictions.jsonl'
output_model_path = './result/rfc_model.dat'


def rank():
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

    # 4 读取测试集
    X_test = raw_data
    X_test.drop(['memo_polish'], axis=1, inplace=True)
    
    # 5 预测
    model = pickle.load(open(output_model_path, 'rb'))
    y_pred = model.predict(X_test)


    # 6 结果写入
    with open(output_predictions_path, 'w') as fp:
        # 将预测结果写入文件中，格式请参考“数据集格式”小节
        for i, label in enumerate(y_pred):
            fp.write('{"id":"%d", "label":"%d"\n}'%(i+1, label))
            logging.warning('{"id":"%d", "label":"%d"}'%(i+1, label))
        fp.close()

    return True


if __name__ == '__main__':
    if rank():
        # 执行成功一定要以0方式退出
        sys.exit(0)
    else:
        # 否则1退出
        sys.exit(1)