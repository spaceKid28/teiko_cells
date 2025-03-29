from src.helper import helper
import pandas as pd

def main():
    # Set pandas options to display all rows and columns
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.max_rows', None)     # Show all rows


    helper_o = helper()
    # problem 1
    helper_o.load_to_pandas()
    helper_o.calculate_relative_freq()
    helper_o.write_solution_1()
    # problem 2
    helper_o.load_to_pandas()
    helper_o.calculate_relative_freq()
    helper_o.perform_filter()
    helper_o.data.to_csv("problem2.csv")
    helper_o.generate_boxplots() # Python Problem2a
    helper_o.perform_statistical_tests()


if __name__ == '__main__':
    main()