import sys
import statistics


CATEGORY_INDEXES = {
    "timestamp" : 0,
    "cnt" : 1,
    "t1" : 2,
    "t2" : 3,
    "hum" : 4,
    "wind_speed" : 5,
    "weather_code" : 6,
    "is_holiday" : 7,
    "is_weekend" : 8,
    "season" : 9
}
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
    returns the categories and data rows as lists, via the csv file path.
"""


def build_categories_and_data_lists(db_path):
    london_db = open(db_path,"r")
    london_db_text = london_db.read()
    data_catgories = london_db_text[:london_db_text.find('\n')].split(',')
    london_db_text = london_db_text[london_db_text.find('\n')+1:]
    data = london_db_text.split('\n')
    data = [row.split(',') for row in data][:-1]
    return data_catgories, data


"""
    returns the data list by the category name
"""


def get_lst_by_name(data, name):
    return [row[CATEGORY_INDEXES[name]] for row in data]

# returns true if value season = 1 and holiday = 1


def filter_summer(row):
    return row[CATEGORY_INDEXES["season"]] == "1"


def filter_holiday(row):
    return row[CATEGORY_INDEXES["is_holiday"]] == "1"


"""
    return a new list containing only the values fitting through the filter.    
"""


def filter_data(data, filter):
    filtered_data = []
    for row in data:
        if filter(row):
            filtered_data.append(row)
    return filtered_data

"""
    prints in the requested format, recieving the relevant data and the str (summer or holiday)
"""
def formatted_print(data, str):
    hum = get_lst_by_name(data,"hum")
    t1 = get_lst_by_name(data,"t1")
    cnt = get_lst_by_name(data,"cnt")
    categories_to_print = ["hum", "t1", "cnt"]
    categories_to_print_lsts = [hum, t1, cnt]
    print(str + ":")
    for cat_name, cat_lst in zip(categories_to_print, categories_to_print_lsts):
        mean = statistics.calc_mean(cat_lst)
        stdv = statistics.calc_stdv(cat_lst)
        mean  = "{:.2f}".format(mean)
        stdv = "{:.2f}".format(stdv)
        print("{}: {}, {}".format(cat_name, mean, stdv))
    cov = statistics.calc_covariance(t1, cnt)
    cov = "{:.2f}".format(cov)
    print("Cov(t1, cnt): {}".format(cov))



def q1(db_path):
    categories, data = build_categories_and_data_lists(db_path)
    formatted_print(filter_data(data, filter_summer), "Summer")
    formatted_print(filter_data(data, filter_holiday), "Holiday")
    formatted_print(data,"All")
def main():
    q1("london_sample.csv")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
