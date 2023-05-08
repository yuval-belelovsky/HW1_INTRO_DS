import sys
import statistics
import data as dt

def q1(db_path, features):
    print("Question 1:")
    data = dt.load_data(db_path, features)
    q1_features = {"hum", "t1", "cnt"}
    summer_data = dt.filter_by_feature(data, "season", {"1"})
    holiday_data = dt.filter_by_feature(data, "is_holiday", {"1"})
    q1_statistic_funcs = {statistics.calc_mean, statistics.calc_stdv}
    for data_i, data_name in zip([summer_data, holiday_data, data], ["Summer", "Holiday", "All"]):
        print("{}:".format(data_name))
        dt.print_details(data_i, q1_features, q1_statistic_funcs)
        dt.print_joint_details(data, {"t1","cnt"}, statistics.calc_covariance,"Cov")

def q2(path, features):
    print("Question 2:")
    data = dt.load_data(path, features)
    data = dt.filter_by_feature(data, "season", {"3"})
    q2_features = {"cnt"}
    holiday_data, weekday_data = dt.filter_by_feature(data, "is_holiday", {"1"})
    print("if t1 <= 13.0, then:")
    statistics.population_statistics("Winter holiday records:", holiday_data, "t1", "cnt", 13.0, False,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter holiday records:", weekday_data, "t1", "cnt", 13.0, False,
                                     [statistics.calc_mean, statistics.calc_stdv])
    print("if t1 >= 13.0, then:")
    statistics.population_statistics("Winter holiday records:", holiday_data, "t1", "cnt", 13.0, True,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter holiday records:", weekday_data, "t1", "cnt", 13.0, True,
                                     [statistics.calc_mean, statistics.calc_stdv])


def main(argv):
    print(argv)
    q1("london_sample.csv")


if __name__ == '__main__':
    main(sys.argv)
