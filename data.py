import pandas



def load_data(path,features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient=”list”)


