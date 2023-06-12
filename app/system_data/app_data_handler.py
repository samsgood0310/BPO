#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# This module handles all the data changes under system_data files.
# this helps with monitoring, and understanding all the changes that are happening
# ************************************************************************************
#


import os
import pickle

import pandas as pd

from app.logs.app_logger import ErrorHandler, Logger
from app.system_data.const_system_data import input_file_path


logger = Logger(__name__)
log_and_handle_errors = ErrorHandler(logger)


abs_path = os.path.dirname(__file__)


@log_and_handle_errors
def get_csv_file(file_name):
    with open(abs_path + '/' + file_name, 'r', encoding='utf8') as f:
        df = pd.read_csv(f)
        return df.rename(columns=lambda x: x.strip())


@log_and_handle_errors
def get_csv_without_index(file_name):
    with open(abs_path + '/' + file_name, 'r', encoding='utf8') as f:
        df = pd.read_csv(f, index_col=False)
        return df.rename(columns=lambda x: x.strip())


@log_and_handle_errors
def user_input_csv(file_name, csv_file):
    logger.info(f'function user_input_csv was used with {file_name} as the file name and the value {csv_file}')
    csv_file.to_csv(f'{abs_path}/user_input_files/{file_name}',
                    index=False, header=True, encoding='utf-8-sig')


@log_and_handle_errors
def input_files_input(file_name, csv_file):
    logger.info(f'function input_files_input was used with {file_name} as the file name')
    csv_file.to_csv(f'{abs_path}/{file_name}', index=False,
                    header=True, encoding='utf-8-sig')


@log_and_handle_errors
def save_packing_results(file_name, df: pd.DataFrame):
    logger.info(f'function save_packing_results was used with {file_name} as the file name')
    df.to_csv(f"{abs_path}/packing_results/{file_name}",
              index=False, header=True, encoding='utf-8-sig')


@log_and_handle_errors
def get_files_names(dir_path=""):
    return [file for file in os.listdir(abs_path + '/' + dir_path)]


@log_and_handle_errors
def save_locally_pickle_file(name_of_object, object_to_save):
    file_to_store = open(f"{abs_path}/packing_results/{name_of_object}.pickle", "wb")
    pickle.dump(object_to_save, file_to_store)
    file_to_store.close()


@log_and_handle_errors
def get_pickle_file(file_name):
    file = open(f"{abs_path}/packing_results/{file_name}.pickle", 'rb')
    object_file = pickle.load(file)
    file.close()
    return object_file


@log_and_handle_errors
def get_keys_in_userdata(type_of_item_to_get) -> list or None:
    try:
        table_loc = input_file_path[type_of_item_to_get]
        df = get_csv_without_index(table_loc)
        return df["key"].unique()
    except Exception as e:
        logger.error(message=f"function = get_keys_in_userdata error: {e}")


@log_and_handle_errors
def get_box_types_keys():
    df = pd.read_csv(abs_path + '/user_input_files/box_properties.csv', header=0)
    column_array = df['key'].to_numpy()
    return column_array
