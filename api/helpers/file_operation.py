import pandas as pd


class FileOperation:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        data = None
        try:
            data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return data

        return data
