import pandas
import statistics
"""
    reads the data from the file and puts it in a dictionary with the necessary features
"""
def load_data(path,features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    data = {x:data[x] for x in features}
    return data
"""
    seperates the dictionary into two dictionaries by the value of each feature
"""


def filter_by_feature(data, feature, values):
    data1 = deep_copy_data(data)
    data2 = deep_copy_data(data)
    data1 = {"cnt": [], "hum": [], "t1": [], "is_holiday": [], "season": []}
    data2 = {"cnt": [], "hum": [], "t1": [], "is_holiday": [], "season": []}
    for i in range(len(data[feature])):
        if data[feature][i] in values:
            for k in ["cnt", "hum", "t1", "is_holiday", "season"]:
                data1[k].append(data[k][i])
        else:
            for k in ["cnt", "hum", "t1", "is_holiday", "season"]:
                data2[k].append(data[k][i])
    return data1, data2




        # data1 = deep_copy_data(data)
        #data2 = deep_copy_data(data)
        #    if data[feature][i] in values:
        #        for k in ["cnt","hum","t1","is_holiday","season"]:
        #       data2[k].remove(data[k][i])
        # else:
        #   for k in ["cnt","hum", "t1", "is_holiday", "season"]:
        #        data1[k].remove(data[k][i])

"""
    prints the value of the statistic methods for each feature
"""
def print_details(data, features, statistic_functions):
    temp = []
    for feature in features:
        for y in statistic_functions:
            temp.append(y(data[feature]))
        for i in range(len(temp)):
            temp[i] = "%.2f" % temp[i]
        print("{}: {}".format(feature,','.join(temp)))
        temp.clear()
    return()

"""
    prints the value of the statistic methods for for two features
"""


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    values = [data[feature] for feature in features]
    for function, function_name in zip(statistic_functions, statistic_functions_names):
        print("{}({}): {}".format(function_name,", ".join(features),function(*values)))


def deep_copy_data(data):
    return {feature : data[feature].copy() for feature in data}
