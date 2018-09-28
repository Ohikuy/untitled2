import numpy as np
import pandas as pd
from pandas import Series, DataFrame
train_df = pd.read_csv('D:/train.csv',low_memory=False)  # train set
test_df = pd.read_csv('D:/test.csv',low_memory=False)  # test set
combine = [train_df, test_df]

print(train_df.head())

