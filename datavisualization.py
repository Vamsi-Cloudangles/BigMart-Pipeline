import seaborn as sns
import pandas as pd
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


    # # Visualize the categorical columns by using the count plot
    # for i in categorical_columns:
    #     fig,ax = plt.subplots(1,1, figsize=(5,4))
    #     sns.countplot(x=dataset[i][1:])
    #     # fig.savefig(f'{i}fig.png')
    # # Visualize the categorical columns by using the pie chart
    # for c in categorical_columns:
    #     fig,plt.pie(dataset[c].value_counts(), labels = dataset[c].unique(), autopct='%1.2f%%')
    #     plt.show()
    # # Visualize the numerical columns using the distplot
    # for i in numerical_columns:
    #     fig, ax = plt.subplots(1,1, figsize=(8,4))
    #     sns.distplot(x = dataset[i][1:])
    # # Finding the outliers using the boxplot
    # for n in numerical_columns:
    #     plt.boxplot(dataset[n])
    #     plt.xlabel(n)
    #     plt.show()

    plt.figure(figsize=(6,4))
    sns.countplot(x='Item_Fat_Content' , data=dataset ,palette='mako')
    plt.xlabel('Item_Fat_Content', fontsize=14)
    plt.show()

    plt.figure(figsize=(27,10))
    sns.countplot(x='Item_Type' , data=dataset ,palette='summer')
    plt.xlabel('Item_Type', fontsize=14)
    plt.show()

    plt.figure(figsize=(15,4))
    sns.countplot(x='Outlet_Identifier' , data=dataset ,palette='winter')
    plt.xlabel('Outlet_Identifier', fontsize=14)
    plt.show()

    plt.figure(figsize=(10,4))
    sns.countplot(x='Outlet_Size' , data=dataset ,palette='autumn')
    plt.xlabel('Outlet_Size', fontsize=14)
    plt.show()

    plt.figure(figsize=(10,4))
    sns.countplot(x='Outlet_Location_Type' , data=dataset, palette='twilight_shifted')
    plt.xlabel('Outlet_Location_Type', fontsize=14)
    plt.show()

    plt.figure(figsize=(10,4))
    sns.countplot(x='Outlet_Type' , data=dataset ,palette='rocket')
    plt.xlabel('Outlet_Type', fontsize=14)
    plt.show()

    # ScatterPlot for Sales per Item_Visibilty
    plt.scatter(dataset['Item_Visibility'], dataset['Item_Outlet_Sales'])
    plt.title('Sales based on Item Visibilty')
    plt.xlabel('Item_Visibility')
    plt.ylabel('Item_Outlet_Sales')
    plt.show()

    # ScatterPlot for Sales per Item_Weight
    plt.scatter(dataset['Item_Weight'], dataset['Item_Outlet_Sales'])
    plt.title('Sales based on Item Weight')
    plt.xlabel('Item_Weight')
    plt.ylabel('Item_Outlet_Sales')
    plt.show()

    # ScatterPlot for Sales per Item_MRP
    plt.scatter(dataset['Item_MRP'], dataset['Item_Outlet_Sales'])
    plt.title('Sales based on Item MRP')
    plt.xlabel('Item_MRP')
    plt.ylabel('Item_Outlet_Sales')
    plt.show()

    pl=sns.violinplot(x='Item_Fat_Content',y='Item_Outlet_Sales',data=dataset,linewidth=0.5,width=1)
    _=pl.set_xticklabels(labels=dataset.Item_Fat_Content.unique(),rotation=30)

    pl=sns.violinplot(x='Outlet_Identifier',y='Item_Outlet_Sales',data=dataset,linewidth=0.5,width=1)
    _=pl.set_xticklabels(labels=dataset.Outlet_Identifier.unique(),rotation=30)

    pl=sns.violinplot(x='Outlet_Size',y='Item_Outlet_Sales',data=dataset,)

    plt.figure(figsize=(27,10))
    sns.barplot('Item_Type' ,'Item_Outlet_Sales', data=dataset ,palette='gist_rainbow_r')
    plt.xlabel('Item_Type', fontsize=14)
    plt.legend()
    plt.show()

    plt.figure(figsize=(27,10))
    sns.barplot('Outlet_Identifier' ,'Item_Outlet_Sales', data=dataset ,palette='gist_rainbow')
    plt.xlabel('Outlet_Identifier', fontsize=14)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10,5))
    sns.barplot('Outlet_Type' ,'Item_Outlet_Sales', data=dataset ,palette='nipy_spectral')
    plt.xlabel('Outlet_Type', fontsize=14)
    plt.legend()
    plt.show()

    plt.figure(figsize = (10,9))
    plt.subplot(311)
    sns.boxplot(x='Outlet_Size', y='Item_Outlet_Sales', data=dataset, palette="Set1")
    plt.subplot(312)
    sns.boxplot(x='Outlet_Location_Type', y='Item_Outlet_Sales', data=dataset, palette="Set1")
    plt.subplot(313)
    sns.boxplot(x='Outlet_Type', y='Item_Outlet_Sales', data=dataset, palette="Set1")
    plt.subplots_adjust(wspace = 0.2, hspace = 0.4,top = 1.5)
    plt.show()

    sale_type = pd.concat([dataset['Item_Outlet_Sales'],dataset['Item_Type']],axis=1)
    plt.box(sale_type,x='Item_Type',y='Item_Outlet_Sales')
    plt.show()

    plt.figure(figsize = (14,9))
    plt.subplot(211)
    ax = sns.boxplot(x='Outlet_Identifier', y='Item_Outlet_Sales', data=dataset, palette="Set1")
    ax.set_title("Outlet_Identifier vs. Item_Outlet_Sales", fontsize=15)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("Item_Outlet_Sales", fontsize=12)

    plt.subplot(212)
    ax = sns.boxplot(x='Item_Type', y='Item_Outlet_Sales', data=dataset, palette="Set1")
    ax.set_title("Item_Type vs. Item_Outlet_Sales", fontsize=15)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("Item_Outlet_Sales", fontsize=12)
    plt.subplots_adjust(hspace = 0.9, top = 0.9)
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.show()

    dataset.groupby('Outlet_Establishment_Year')['Item_Outlet_Sales'].mean().plot.bar()
    plt.show()

    plt.Figure(figsize=(20,10))
    sns.heatmap(dataset.corr(), annot=True)

    #checking for outliers

    plt.figsize = (16,8)
    plt.subplot(2,3,1)
    sns.boxplot(dataset['Item_Weight'])

    plt.subplot(2,3,2)
    sns.boxplot(dataset['Item_Visibility'])

    plt.subplot(2,3,3)
    sns.boxplot(dataset['Item_MRP'])

    plt.subplot(2,3,4)
    sns.boxplot(dataset['Outlet_Establishment_Year'])

    plt.subplot(2,3,5)
    sns.boxplot(dataset['Item_Outlet_Sales'])
    
    # Visualize the categorical columns by using the count plot
    for i in categorical_columns:
        plt.subplots(1,1, figsize=(5,4))
        sns.countplot(x=dataset[i][1:])
    # Visualize the categorical columns by using the pie chart
    # for c in categorical_columns:
    #   plt.pie(dataset[c].value_counts(), labels = dataset[c].unique(), autopct='%1.2f%%')
        # plt.show()
    # Visualize the numerical columns using the distplot
    for i in numerical_columns:
        plt.subplots(1,1, figsize=(8,4))
        sns.distplot(x = dataset[i][1:])
    # Finding the outliers using the boxplot
    # for n in numerical_columns:
    #     plt.boxplot(dataset[n])
    #     plt.xlabel(n)
        # plt.show()

    corr = dataset.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, cmap='RdBu', annot = True, fmt=".2f")
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()
    Q1 = dataset['Item_Visibility'].quantile(0.25)
    Q3 = dataset['Item_Visibility'].quantile(0.75)
    IQR = Q3 - Q1
    dataset = dataset.query('(@Q1 - 1.5 * @IQR) <= Item_Visibility <= (@Q3 + 1.5 * @IQR)')
    return dataset
data_visualization()
