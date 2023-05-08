import pandas

def load_data(path,features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    data = {x:data[x] for x in features}
    return data

def filter_by_feature(data, feature, values):
    data1 = data.copy()
    data2 = data.copy()
    for i in range (len(data["cnt"])):
        if data[feature][i] in values:
            for k in ["cnt"",hum","t1","is_holiday","season"]:
                data2[k].remove(data[k][i])
        else:
            for k in ["cnt"",hum", "t1", "is_holiday", "season"]:
                data1[k].remove(data[k][i])
    return data1,data2

def print_details(data, features, statistic_functions):
    temp = []
    for feature in features:
        for y in statistic_functions:
            temp.append(y(x))
        print(feature,": ", ','.join(temp))
        temp.clear()
    return()


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for function in statistic_functions:
        print(statistic_functions_names[function],"(",features[1],",",features[2],"): ",function(features[1],features[2]))
    return()


