import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_dataset(self) -> pd.DataFrame:
        
        try:
            df = pd.read_csv(self.file_path)

            if df.empty:
                raise ValueError("Dataset is empty.")
            
            return df
        
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Dataset file not found at path: {self.file_path}"
            )
        
        except pd.errors.EmptyDataError:
            raise ValueError("Dataset file is empty")
        
        except pd.errors.ParserError:
            raise ValueError("Error Parsing CSV File")
        
        except Exception as error:
            raise Exception(
                f"Unexpected error while loading dataset: {error}"
            )

        