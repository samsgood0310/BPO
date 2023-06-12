#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# This module write to a local file the solution on the solver.
# The local file will contain a record per each bin with the items that will be stored in them.
# In addition to that each item in the bin will have his location in the bin (x,y,z).
# The User will be able to download the file.
# ************************************************************************************
#

import pandas as pd

from app.bin_packing_solver.py3dbp_solver import connection_bp_to_db
from app.components import three_d_graph
from app.logs.app_logger import ErrorHandler, Logger
from app.scripts import exe_sys_scripts


logger = Logger(__name__)

error_and_log_handler = ErrorHandler(logger)


@error_and_log_handler
def transform_bins_to_dataframe(packer) -> pd.DataFrame:
    """
    Containing the bin's as a dataframe give options to create better graphs and reports.
    :param packer:
    :return:
    """
    return pd.DataFrame(
        [
            {
                "bin_name": b.name,
                "bin_index": i,
                **three_d_graph.add_item_to_packing_subplot(item),
                **{d: v for v, d in zip(item.get_dimension(), list("hwl"))},
                **{d + d: v for v, d in zip(item.position, list("xyz"))},
            }
            for i, b in enumerate(packer.bins)
            for item in b.items
        ]
    )


@error_and_log_handler
def create_bins_report(packer) -> pd.DataFrame:
    """
    this function create a dataframe with each row contain info about a bin
    """
    bins_info = []  # This list will be used to add dict per each bin with information about what he contains
    for row, pbin in enumerate(packer.bins):
        packed_items = [item.name for item in pbin.items]
        unpacked_items = [item.name for item in pbin.unfitted_items]
        bin_info = {
            'bin_name': pbin.name,
            'bin_weight': pbin.get_total_weight(),
            'number_of_items_in_bin': len(packed_items),
            'items_in_bin': [packed_items],
            'number_of_items_not_in_bin': len(unpacked_items),
            'items_not_in_bin': [unpacked_items]
        }
        bins_info.append(bin_info)
    return pd.DataFrame(bins_info)


@error_and_log_handler
def export_results_to_report(packer) -> None:
    """
    This function create the plotly graph using the packing function.
    The results are transformed to
    """
    # Removing old packing results.
    exe_sys_scripts.run_bash_script("delete_last_packing_results")
    all_packed_items = transform_bins_to_dataframe(packer)  # create items report

    bins_report = create_bins_report(packer)  # create bins report

    # saving the reports as local csv files
    connection_bp_to_db.transform_results("All Bins", bins_report)
    connection_bp_to_db.transform_results("All Packed Items", all_packed_items)
