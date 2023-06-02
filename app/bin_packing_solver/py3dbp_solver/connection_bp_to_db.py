"""
The purpose of this module is to translate and connect the solver and the user input.
The user uploads csv files that are easy to read (and write), and the algorithm need to get information in a certain way
So the module solved the gap with the above functions.
It's also important to keep as undefended and modular each file / module, for that reason all the calls from the
bin_packing_solver to the system data will be using this module.
"""
import pandas as pd

from app.logs.app_logger import ErrorHandler, Logger
from app.system_data import app_data_handler, const_system_data


logger = Logger(__name__)

error_and_log_handler = ErrorHandler(logger)


@error_and_log_handler
def get_containers_bp_format() -> pd.DataFrame:
    """
    formatting the containers to the bin format of the solver, it's done by aggregating the relevant user files and
    taking the part of that new DataFrame (that was created to aggregate the data).
    :return:
    """
    containers_merged = pd.merge(
        app_data_handler.get_csv_file(const_system_data.input_file_path['container_properties']),
        app_data_handler.get_csv_file(const_system_data.input_file_path['container_amount']),
        on=["key"])
    containers_merged_named = containers_merged.rename(columns=lambda col_name: col_name.strip())
    repeated_df = containers_merged_named.reindex(
        containers_merged_named.index.repeat(containers_merged_named.amount))

    # taking only the columns that are needed for the solver
    return repeated_df[["key", "x", "y", "z", "w"]].values.tolist()


@error_and_log_handler
def get_containers_bp_name():
    container = app_data_handler.get_csv_file(const_system_data.input_file_path['container_amount'])
    container_name = container['name'].to_numpy()
    return container_name


@error_and_log_handler
def get_boxes_bp_format() -> dict:
    """
    formatting the boxes to the item format of the solver, it's done by aggregating the relevant user files and
    taking the part of that new DataFrame (that was created to aggregate the data).
    :return:
    """
    boxed_val = app_data_handler.get_csv_file(const_system_data.input_file_path['box_amount'])
    boxed_prop = app_data_handler.get_csv_file(const_system_data.input_file_path['box_properties'])

    # Sort the boxes according to priority
    boxed_val = boxed_val.sort_values(by=['priority'])
    merged_df = boxed_val.merge(boxed_prop, on='key')
    result_dict = {row['key']: {'n': row['amount'], 's': [row['x'], row['y'], row['z'], row['w']]} for index, row in
                   merged_df.iterrows()}
    return result_dict


@error_and_log_handler
def transform_results(name: str, df: pd.DataFrame) -> None:
    app_data_handler.save_packing_results(name + ".csv", df)


@error_and_log_handler
def get_user_algorithm_parameters() -> dict:
    """
    Turning the user input for the algorithm parameters to a dict that the solver is using
    :return: A dict similar to
    {'bigger_first': True,
    'distribute_items': True,
    'number_of_decimals': 3}
    """
    df_algo_params = app_data_handler.get_csv_file(const_system_data.input_file_path['user_algorithm_params'])

    # Transforming the dataframe to list with bool value for fil
    dict_algo_params = {
        row['Property']: bool(row['Value']) if isinstance(row['Value'], bool)
        else False if str(row['Value']).lower() == 'false'
        else True if str(row['Value']).lower() == 'true'
        else row['Value']
        for _, row in df_algo_params.iterrows()
    }

    # Turning number_of_decimals field value from string to int
    dict_algo_params['number_of_decimals'] = int(dict_algo_params['number_of_decimals'])

    return dict_algo_params
