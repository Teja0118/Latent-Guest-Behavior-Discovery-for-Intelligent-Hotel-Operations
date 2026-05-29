from preprocessing.data_loader import DataLoader
from preprocessing.dataset_inspector import DatasetInspector
from preprocessing.data_preprocessor import DataPreprocessor
from preprocessing.eda_analyzer import EDAAnalyzer


def main():
    try:
        dataset_path = "data/hospitality_operations_03.csv"
        processed_dataset_path = "data/processed_hospitality_operations.csv"

        # Loading Data
        data_loader = DataLoader(dataset_path)
        df = data_loader.load_dataset()

        print("Dataset Loaded Successfully!\n")

        # Inspect Data
        inspector = DatasetInspector(df)
        inspector.dataset_info()
        inspector.check_missing_values()
        inspector.check_duplicate_rows()
        inspector.seperate_feature_types()
        inspector.statistical_summary()

        # Preprocess Data
        preprocessor = DataPreprocessor(df)
        preprocessor.drop_unnecessary_columns()
        preprocessor.encode_categorical_features()
        preprocessor.scale_numerical_features()
        preprocessor.save_processed_dataset(processed_dataset_path) 

        # Perform EDA 
        preprocessed_df = preprocessor.get_processed_dataframe()
        eda_analyzer = EDAAnalyzer(preprocessed_df)
        eda_analyzer.correlation_heatmap()
        eda_analyzer.spending_distribution_analysis()
        eda_analyzer.service_usage_analysis()
        eda_analyzer.operational_metrics_analysis()
        eda_analyzer.categorical_feature_analysis()



        '''
        print("Dataset Shape: ")
        print(df.shape)

        print("First 5 Rows: ")
        print(df.head())

        print("Column Names: ")
        print(df.columns.tolist())
        '''
        

    except Exception as error:
        print(f"\nApplication Error: {error}")

if __name__ == "__main__":
    main()