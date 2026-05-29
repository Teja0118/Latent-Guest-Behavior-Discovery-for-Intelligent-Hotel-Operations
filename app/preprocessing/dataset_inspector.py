import pandas as pd

class DatasetInspector:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def dataset_info(self):

        try:
            print("\nDataset Information:")
            print(self.dataframe.info())

        except Exception as error:
            print(f"Error while fetching dataset info: {error}")

    def check_missing_values(self):

        try:
            missing_values = self.dataframe.isnull().sum()
            missing_values = missing_values[missing_values > 0]
            print("\nMissing Values: \n")

            if missing_values.empty:
                print("No missing values found.")
            else:
                print(missing_values)

        except Exception as error:
            print(f"Error while checking missing values: {error}")

    def check_duplicate_rows(self):

        try:
            duplicate_count = self.dataframe.duplicated().sum()
            print(f"\nDuplicate Row Count: {duplicate_count}")

        except Exception as error:
            print(f"Error while checking duplicates: {error}")

    def seperate_feature_types(self):
        
        try:
            numerical_columns = self.dataframe.select_dtypes(
                include=['int64', 'float64']
            ).columns.tolist()

            categorical_columns = self.dataframe.select_dtypes(
                include=['object']
            ).columns.tolist()

            print("\nNumerical Columns: \n")
            print(numerical_columns)
            print("\nCategorical Columns: \n")
            print(categorical_columns)

        except Exception as error:
            print(f"Error while seperating feature types: {error}")

    def statistical_summary(self):

        try:
            print("\nStatistical Summary:\n")
            print(self.dataframe.describe())

        except Exception as error:
            print(f"Error while generating statistical summary: {error}")

            