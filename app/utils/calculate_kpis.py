"""
This module is used for calculating the KPI's of the
"""

import ast
from collections import Counter

import pandas as pd

from app.system_data import app_data_handler, const_system_data


def __get_pecked_formatted_bin_df():
    bins_df = app_data_handler.get_csv_file(const_system_data.result_file_path['all_bins'])
    bins_df['items_not_in_bin'] = bins_df['items_not_in_bin'].apply(lambda x: ast.literal_eval(x)[0])
    bins_df['items_in_bin'] = bins_df['items_in_bin'].apply(lambda x: ast.literal_eval(x)[0])
    return bins_df


def __get_input_containers_df():
    containers_merged = pd.merge(
        app_data_handler.get_csv_file(const_system_data.input_file_path['container_properties']),
        app_data_handler.get_csv_file(const_system_data.input_file_path['container_amount']),
        on=["key"])
    containers_merged_named = containers_merged.rename(columns=lambda col_name: col_name.strip())
    return containers_merged_named


def __get_input_boxes_df():
    containers_merged = pd.merge(
        app_data_handler.get_csv_file(const_system_data.input_file_path['box_properties']),
        app_data_handler.get_csv_file(const_system_data.input_file_path['box_amount']),
        on=["key"])
    containers_merged_named = containers_merged.rename(columns=lambda col_name: col_name.strip())
    return containers_merged_named


def calc_bins_kpis():
    # calculate the KPIs
    df = __get_pecked_formatted_bin_df()
    total_items = (df["number_of_items_in_bin"] + df["number_of_items_not_in_bin"])[0]
    unpacked_items = df['number_of_items_not_in_bin'].min()
    percent_packed = round((total_items - unpacked_items) / total_items, 2)
    return total_items, unpacked_items, percent_packed


def calc_boxes_packed_ratio():
    def __calc_boxes_in_bins_per_box_type():
        df = __get_pecked_formatted_bin_df()
        # number_of_packed_items_of_box_type = pd.concat([pd.Series(x) for x in df['items_in_bin']]).tolist()
        number_of_packed_items_of_box_type = pd.concat([pd.Series(x, dtype=str) for x in df['items_in_bin']]).tolist()
        items_without_duplicates = list(dict.fromkeys(number_of_packed_items_of_box_type))
        items_without_id = [''.join(item.split('_')[:-1]) for item in
                            items_without_duplicates]  # removing the _id substring
        return dict(Counter(items_without_id))

    input_boxes = __get_input_boxes_df()
    input_boxed_keys_and_amount = dict(zip(input_boxes['key'], input_boxes['amount']))

    packed_boxes_keys_and_amount = __calc_boxes_in_bins_per_box_type()

    results = {}
    for box_type in input_boxed_keys_and_amount:
        if box_type in packed_boxes_keys_and_amount:
            ratio = packed_boxes_keys_and_amount[box_type] / input_boxed_keys_and_amount[box_type] * 100
            results[
                box_type] = f"{ratio:.0f}% ({packed_boxes_keys_and_amount[box_type]}/{input_boxed_keys_and_amount[box_type]})"
        else:
            results[box_type] = f"0% (0/{input_boxed_keys_and_amount[box_type]})"

    return results


def calc_weight_ratio():
    def __calc_weight(items_df):
        return (items_df['w'] * items_df['amount']).sum()

    total_input_boxes_weight = __calc_weight(__get_input_boxes_df())
    total_input_bins_weight = __calc_weight(__get_input_containers_df())
    packed_bins = __get_pecked_formatted_bin_df()
    total_packed_boxes_weight = packed_bins['bin_weight'].sum()
    return total_packed_boxes_weight, total_input_boxes_weight, total_input_bins_weight


def calculate_bin_utilization():
    packed_bins_df = __get_pecked_formatted_bin_df()
    input_bins_df = __get_input_containers_df()

    # count the total input bins for each key
    total_bins_by_key = {}
    bin_groups = input_bins_df.groupby('key')
    for bin_name, group in bin_groups:
        total_bins_by_key[bin_name] = group['amount'].sum()

    # count the total packed bins for each key
    packed_bins_by_key = {}
    packed_bin_groups = packed_bins_df.groupby('bin_name')
    for bin_name, group in packed_bin_groups:
        packed_bins_by_key[bin_name] = len(group.index)

    # calculate the utilization for each key and store it in a dictionary
    utilizations = {}
    for bin_name, total_bins in total_bins_by_key.items():
        packed_bins = packed_bins_by_key.get(bin_name, 0)
        utilization = packed_bins / total_bins
        utilization_str = f"{int(utilization * 100)}% ({packed_bins}/{total_bins})"
        utilizations[bin_name] = utilization_str

    # calculate the total utilization for all bins and store it as a string
    total_bins = sum(total_bins_by_key.values())
    total_packed_bins = sum(packed_bins_by_key.values())
    total_utilization = round(total_packed_bins / total_bins, 2)
    total_utilization_str = f"{int(total_utilization * 100)}% ({total_packed_bins}/{total_bins})"

    return utilizations, total_utilization_str


def collect_kpis_to_report():
    """
    This function collects all the calculation functions and formats their outputs into one dictionary with all the
    KPIs.
    :return: A dictionary containing all the calculated KPIs.
    """
    bins_total_items, bins_unpacked_items, bins_percent_packed = calc_bins_kpis()
    boxes_packed_per_box_type = calc_boxes_packed_ratio()
    overview_total_packed_weight, overview_total_input_boxes_wight, overview_total_input_bins_wight = calc_weight_ratio()
    bins_utilizations, bins_total_utilization_str = calculate_bin_utilization()

    return bins_total_items, bins_unpacked_items, bins_percent_packed, boxes_packed_per_box_type,\
        overview_total_packed_weight, overview_total_input_boxes_wight, overview_total_input_bins_wight, \
        bins_utilizations, bins_total_utilization_str
