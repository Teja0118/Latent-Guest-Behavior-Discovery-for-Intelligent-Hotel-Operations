import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def drop_unnecessary_columns(self):
        
        try:
            columns_to_drop = [
                "stay_id",
                "guest_id",
                "property_id",
                "checkin_date",
                "overall_satisfaction_score"
            ]

            self.dataframe.drop(
                columns=columns_to_drop,
                inplace=True    
            )

            print("\nUnnecessary columns dropped successfully.")

        except Exception as error:
            print(f"Error while dropping columns: {error}")

    def encode_categorical_features(self):

        try:
            categorical_columns = self.dataframe.select_dtypes(
                include=['object']
            ).columns

            for column in categorical_columns:

                encoder = LabelEncoder()

                self.dataframe[column] = encoder.fit_transform(
                    self.dataframe[column]
                )

                self.label_encoders[column] = encoder
            
            print("\nCategorical feature encoding completed.")

        except Exception as error:
            print(f"Error while encoding categorical features: {error}")

    def scale_numerical_features(self):

        try:
            numerical_columns = self.dataframe.select_dtypes(
                include=["int64", "float64"]
            ).columns

            self.dataframe[numerical_columns] = self.scaler.fit_transform(
                self.dataframe[numerical_columns]
            )

            print("\nNumerical feature scaling completed.")

        except Exception as error:
            print(f"Error while scaling numerical features: {error}")

    def save_processed_dataset(self, output_path: str):

        try:
            self.dataframe.to_csv(
                output_path,
                index=False
            )

            print(
                f"\nProcessed dataset saved successfully at: \n{output_path}"
            )
        except Exception as error:
            print(f"Error while saving processed dataset: {error}")

    def get_processed_dataframe(self):
        return self.dataframe