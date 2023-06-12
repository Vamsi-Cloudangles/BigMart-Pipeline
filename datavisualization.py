import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from datapreprocessing import data_preprocessing
def data_visualization():
    dataset = data_preprocessing()
    categ = []
    numer = []
    for col in dataset.columns:
        if dataset[col].dtypes == object:
            categ.append(col)
        else:
            numer.append(col)

    # Histogram plots ....................
    sns.histplot(dataset['Item_Fat_Content'])
    plt.show()
    sns.histplot(dataset['Outlet_Size'])
    plt.show()
    sns.histplot(dataset['Outlet_Location_Type'])
    plt.show()
    plt.figure(figsize=(10,5))
    sns.histplot(dataset['Outlet_Type'])
    plt.show()

    # Count plots ...................
    sns.countplot(x='Item_Fat_Content',data=dataset)
    plt.show()
    sns.countplot(x='Outlet_Type',data=dataset)
    plt.show()

    # Distribution plots .......................
    for i in numer:
        plt.subplots(1,1, figsize=(8,4))
        sns.distplot(x = dataset[i])
        plt.xlabel(i)
    plt.show()

    # Scatter Plots .................
    plt.scatter(dataset['Item_Visibility'], dataset['Item_MRP'])
    plt.xlabel('Item_Visibility')
    plt.ylabel('Item_MRP')
    plt.show()
    plt.scatter(dataset['Item_Weight'], dataset['Item_Outlet_Sales'])
    plt.xlabel('Item_Weight')
    plt.ylabel('Item_Outlet_Sales')
    plt.show()
    plt.scatter(dataset['Item_Visibility'], dataset['Item_Outlet_Sales'])
    plt.xlabel('Item_Visibility')
    plt.ylabel('Item_Outlet_Sales')
    plt.show()
    plt.scatter(dataset['Item_Weight'], dataset['Item_MRP'])
    plt.xlabel('Item_Weight')
    plt.ylabel('Item_MRP')
    plt.show()

    # Box plots.............
    for num in numer:
        plt.subplots(1,1, figsize=(5,5))
        sns.boxplot(dataset[num])
        plt.xlabel(num)
    plt.show()

    # Violin plots.............
    for num in numer:
        plt.subplots(1,1, figsize=(5,5))
        sns.violinplot(dataset[num])
        plt.xlabel(num)
    plt.show()

    #  Correlation Matrix.......................
#     corrolation = dataset.corr()
#     plt.subplots(figsize=(10, 10))
#     sns.heatmap(corrolation, cmap='RdBu', annot = True, fmt=".2f")
#     plt.xticks(range(len(corrolation.columns)), corrolation.columns);
#     plt.yticks(range(len(corrolation.columns)), corrolation.columns)
#     plt.show()
    Q1 = dataset['Item_Visibility'].quantile(0.25)
    Q3 = dataset['Item_Visibility'].quantile(0.75)
    IQR = Q3 - Q1
    dataset = dataset.query('(@Q1 - 1.5 * @IQR) <= Item_Visibility <= (@Q3 + 1.5 * @IQR)')
    return dataset
data_visualization()
