from sklearn.preprocessing import LabelEncoder
from scipy import stats
import numpy as np
from data_preprocessing import data_preprocess

def feature_engineering():

    data = data_preprocess()
    # print(data)
    def remove_outliers(data,par):
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data.drop(index=i,inplace=True)
       
    for j in ["price"]: 
        remove_outliers(data,j)

    le=LabelEncoder()
    data['gender']=le.fit_transform(data['gender'])
    data['category']=le.fit_transform(data['category'])
    data.to_csv("customer_spending_prediction.csv",index=False)
    print(data)
    return data

feature_engineering()