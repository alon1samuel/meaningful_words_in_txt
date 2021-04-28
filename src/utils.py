# Save a dictionary into a pickle file.
import pickle
import os
import pandas as pd
import json


class SaveRead():

    @staticmethod
    def save_data_pickle(data_to_save, path_to_save):
        # saves the data
        with open(path_to_save, 'wb') as f:
            pickle.dump(data_to_save, f)

    @staticmethod
    def save_data_json(json_to_save, path_to_save):
        # saves the data
        with open(path_to_save, 'w') as f:
            json.dump(json_to_save, f, ensure_ascii=False, indent=2)

    @staticmethod
    def read_data_json(path_to_read):
        # read json data
        if not os.path.exists(path_to_read):
            raise Exception("Didn't find file in path - {}".format(path_to_read))

        with open(path_to_read) as f:
            data = json.load(f)

        return data

    @staticmethod
    def read_data_pickle(path_to_read):
        # read pickle data
        if not os.path.exists(path_to_read):
            raise Exception("Didn't find file in path - {}".format(path_to_read))

        with open(path_to_read, 'rb') as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def read_csv_to_df(csv_filepath):
        if not os.path.exists(csv_filepath):
            raise Exception(f"Didn't find file in path - {csv_filepath}")

        return pd.read_csv(csv_filepath)

