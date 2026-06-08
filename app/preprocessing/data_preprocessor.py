import pandas as pd

import joblib

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


class DataPreprocessor:

    def __init__(
        self,
        dataframe: pd.DataFrame
    ):

        self.original_dataframe = (
            dataframe.copy()
        )

        self.dataframe = dataframe.copy()

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

            self.original_dataframe.drop(

                columns=columns_to_drop,

                inplace=True
            )

            print(
                "\nUnnecessary columns "
                "dropped successfully."
            )

        except Exception as error:

            print(
                f"Error while dropping "
                f"columns: {error}"
            )

    def encode_categorical_features(self):

        try:

            categorical_columns = (
                self.dataframe.select_dtypes(
                    include=[
                        "object",
                        "string"
                    ]
                ).columns
            )

            for column in categorical_columns:

                encoder = LabelEncoder()

                self.dataframe[column] = (
                    encoder.fit_transform(
                        self.dataframe[column]
                    )
                )

                self.label_encoders[column] = (
                    encoder
                )

            print(
                "\nCategorical feature "
                "encoding completed."
            )

        except Exception as error:

            print(
                f"Error while encoding "
                f"categorical features: "
                f"{error}"
            )

    def scale_numerical_features(self):

        try:

            numerical_columns = (
                self.dataframe.select_dtypes(
                    include=[
                        "int64",
                        "float64"
                    ]
                ).columns
            )

            self.dataframe[
                numerical_columns
            ] = self.scaler.fit_transform(

                self.dataframe[
                    numerical_columns
                ]
            )

            print(
                "\nNumerical feature "
                "scaling completed."
            )

        except Exception as error:

            print(
                f"Error while scaling "
                f"numerical features: "
                f"{error}"
            )

    def save_processed_dataset(
        self,
        output_path: str
    ):

        try:

            self.dataframe.to_csv(

                output_path,

                index=False
            )

            print(

                f"\nProcessed dataset "
                f"saved successfully at:\n"
                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"processed dataset: "
                f"{error}"
            )

    def get_processed_dataframe(self):

        return self.dataframe

    def get_original_dataframe(self):

        return self.original_dataframe

    def save_scaler(
        self,
        output_path: str
    ):

        try:

            joblib.dump(
                self.scaler,
                output_path
            )

            print(
                f"\nScaler saved "
                f"successfully at:\n"
                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"scaler: {error}"
            )

    def save_label_encoders(
        self,
        output_path: str
    ):

        try:

            joblib.dump(

                self.label_encoders,

                output_path
            )

            print(

                f"\nLabel encoders "
                f"saved successfully at:\n"

                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"encoders: {error}"
            )