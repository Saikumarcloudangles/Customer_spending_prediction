from data_preprocessing import data_preprocess
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.figure_factory as ff
import string


def data_visualization():

    data=data_preprocess()
    count = 0
    letters = list(string.ascii_lowercase)
    names_cat=["gender","category"]
    for i in names_cat:
        count+=1
        lst = []
        lst.append(i)
        df = data.groupby(by=lst).size().reset_index(name="counts")
        fig=px.bar(data_frame=df, x=i, y="counts",color=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        #fig.show()
        fig.write_image(f"{letters[count]}count_{i}.jpg")
        
    
    names=["age","quantity","price"]

    for j in names:
        count += 1
        fig = px.box(data, y=j)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        #fig.show()
        fig.write_image(f"{letters[count]}box_{j}.jpg")

        fig = ff.create_distplot([data[j].values],group_labels=[j])
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        #fig.show()
        fig.write_image(f"{letters[count]}_dist_{j}.jpg")
       
    return data

data_visualization()