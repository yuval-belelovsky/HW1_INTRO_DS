from math import sqrt

"""
    casts the string into float if needed
"""
def cast_values(values):
    int_lst = []
    for value in values:
        if type(value) != float:
            int_lst.append(float(value))
        else:
            int_lst.append(value)
    return int_lst

"""
    Calculates the mean of a set
"""

def calc_mean(values):
    values = cast_values(values)
    return sum(values) / len(values)


"""
    Calculates the standard deviation of the given set
"""


def calc_stdv(values):
    if len(values) == 1:
        return 0
    values = cast_values(values)
    avg = calc_mean(values)
    s = 0  # summation variable
    for value in values:
        s += (value - avg) ** 2
    s /= (len(values) -1)
    return sqrt(s)


"""
    Calculates covariance between two sets
"""


def calc_covariance(values1, values2):
    values1 = cast_values(values1)
    values2 = cast_values(values2)
    avg1 = calc_mean(values1)
    avg2 = calc_mean(values2)
    s = 0
    for (value1, value2) in zip(values1, values2):
        s += (value1 - avg1) * (value2- avg2)
    return s / (len(values1)-1)

def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    print("{}".format(feature_description))
    values = []
    print("{}: ".format(target), end="")
    for treatment, target in zip(data[treatment], data[target]):
        treatment = float(treatment)
        if is_above:
            if treatment > threshold:
                values.append(target)
        else:
            if treatment <= threshold:
                values.append(target)
    results = [function(values) for function in statistic_functions]
    print(",".join([str(x) for x in results]))
