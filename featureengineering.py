from sklearn import preprocessing
le = preprocessing.LabelEncoder()
import pandas as pd
from datapreprocessing import data_preprocessing
def feature_engineering():
    dataset = data_preprocessing()
    categorical_columns = []
    numerical_columns = []
    for col in dataset.columns:
        if dataset[col].dtypes == object:
            categorical_columns.append(col)
        else:
            numerical_columns.append(col)
    print(categorical_columns) 
    print(numerical_columns)
    # Changing the categorical columns to numerical by using the label encoding method.
    for c in categorical_columns:
        dataset[c] = le.fit_transform(dataset[c])
    # Performing the one hot encoding for some categorical values which contains less than 3 unique values
    dataset = pd.get_dummies(dataset, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type'])
    dataset.to_csv("Cleaned_dataset.csv")
    return dataset
feature_engineering()