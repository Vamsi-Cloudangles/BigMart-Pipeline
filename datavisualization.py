import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from datapreprocessing import data_preprocessing
def data_visualization():
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
    # Visualize the categorical columns by using the count plot
    for i in categorical_columns:
        fig,ax = plt.subplots(1,1, figsize=(5,4))
        sns.countplot(x=dataset[i][1:])
    # Visualize the categorical columns by using the pie chart
    for c in categorical_columns:
        fig,plt.pie(dataset[c].value_counts(), labels = dataset[c].unique(), autopct='%1.2f%%')
        plt.show()
    # Visualize the numerical columns using the distplot
    for i in numerical_columns:
        fig, ax = plt.subplots(1,1, figsize=(8,4))
        sns.distplot(x = dataset[i][1:])
    # Finding the outliers using the boxplot
    for n in numerical_columns:
        plt.boxplot(dataset[n])
        plt.xlabel(n)
        plt.show()

    Q1 = dataset['Item_Visibility'].quantile(0.25)
    Q3 = dataset['Item_Visibility'].quantile(0.75)
    IQR = Q3 - Q1
    dataset = dataset.query('(@Q1 - 1.5 * @IQR) <= Item_Visibility <= (@Q3 + 1.5 * @IQR)')
    return dataset
data_visualization()
