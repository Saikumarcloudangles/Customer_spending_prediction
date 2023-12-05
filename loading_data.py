import  pandas as pd

def loading_data():
    data = pd.read_csv('./customer_shopping_data.csv')
    return data

loading_data()