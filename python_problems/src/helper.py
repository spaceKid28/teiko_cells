import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

class helper:
    populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
    def __init__(self):
            pass
    def load_to_pandas(self):
        self.file_path = os.listdir("./data/")[0] # get path to file in data folder

        self.data = pd.read_csv(f"data/{self.file_path}") # convert to a pandas dataframe

    def calculate_relative_freq(self):
        self.data['total_count'] = self.data[self.populations].sum(axis=1) # find total count of all cells (across 5 populations)
        
        for population in self.populations: # loop through each population to calculate relative freq
            self.data[f"{population}_percentage"] = self.data[population] / self.data['total_count']
    
    def write_solution_1(self):
        # filter the columns out, per instruction
        list_of_columns = ['sample', 'total_count'] + self.populations \
            + [f"{population}_percentage" for population in self.populations]
        self.data = self.data[list_of_columns]
        self.data.to_csv('./solutions/python_1.csv')

    def perform_filter(self):
        # Filter the DataFrame based on the specified column values using masking
        self.data = self.data[
            (self.data['treatment'] == 'tr1') &
            (self.data['condition'] == 'melanoma') &
            (self.data['sample_type'] == 'PBMC')
        ]
    def generate_boxplots(self, output_dir='./solutions/problem_2a'):
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Loop through each population and generate a boxplot
        for population in self.populations:
            plt.figure(figsize=(8, 6))  # Set the figure size
            sns.boxplot(data=self.data, x='response', y=population)  # Create the boxplot
            plt.title(f'Boxplot of {population} by Response')  # Add a title
            plt.xlabel('Response')  # Label for x-axis
            plt.ylabel(f'{population}')  # Label for y-axis
            
            # Save the plot to a file
            output_file = os.path.join(output_dir, f'{population}_boxplot.png')
            plt.savefig(output_file, dpi=300)  # Save the plot
            plt.close()



    def perform_statistical_tests(self):
        # Define the immune cell population percentage columns
        populations = [
            'b_cell_percentage', 'cd8_t_cell_percentage', 'cd4_t_cell_percentage',
            'nk_cell_percentage', 'monocyte_percentage'
        ]
        
        # Create a dictionary to store the results
        results = []

        # Loop through each population and perform the t-test
        for population in populations:
            # Split the data into responders and non-responders
            responders = self.data[self.data['response'] == 'y'][population]
            non_responders = self.data[self.data['response'] == 'n'][population]
            
            # Perform the t-test
            stat, p_value = ttest_ind(responders, non_responders, equal_var=False)  # Welch's t-test
            
            # Append the results
            results.append({
                'Population': population,
                'Statistic': stat,
                'P-Value': p_value
            })
        
        # Convert results to a DataFrame for better readability
        results_df = pd.DataFrame(results)
        print(results_df)  # Print the results to the terminal
        results_df.to_csv('./solutions/problem_2b_statistics.csv', index=False)  # Save the results to a CSV file

    def write_solution_2(self):
        pass
        




