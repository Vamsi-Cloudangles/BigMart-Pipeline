from dataanalysis import data_analysis
def data_preprocessing():
    dataset = data_analysis()
    mean_iw = dataset['Item_Weight'].mean()
    dataset.Item_Weight.fillna(value = mean_iw, inplace = True)
    mean_ios = dataset['Item_Outlet_Sales'].mean()
    dataset.Item_Outlet_Sales.fillna(value = mean_ios, inplace = True)
    mode_os = dataset['Outlet_Size'].value_counts().idxmax()
    dataset.Outlet_Size.fillna(value  = mode_os, inplace = True)
    print(dataset.isnull().sum())
    return dataset
data_preprocessing()