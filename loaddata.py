import pandas as pd
def Load_Data():
    dataframe = pd.read_csv("bigmart.csv")
    print(dataframe.head(5))
    return dataframe

Load_Data()
