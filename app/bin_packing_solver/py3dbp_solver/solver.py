#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# This module contain the Bin Packing solver and create the 3d fig.
# The code is based on the following example
# https://stackoverflow.com/questions/71318810/interactive-3d-plot-with-right-aspect-ratio-using-plotly
# ************************************************************************************
#


from py3dbp import Bin, Item, Packer

from app.bin_packing_solver.py3dbp_solver import (connection_bp_to_db,
                                                  solution_publisher)
from app.logs.app_logger import ErrorHandler, Logger

logger = Logger(__name__)
error_and_log_handler = ErrorHandler(logger)


@error_and_log_handler
def packing_algorithm():
    packer = Packer()
    new_packing = f"""
    New Packing calculation: 
    # Containers = {connection_bp_to_db.get_containers_bp_format()}
    Items = {connection_bp_to_db.get_boxes_bp_format().items()}
    Solver_Params = {connection_bp_to_db.get_user_algorithm_parameters()}
    """
    logger.info(new_packing)

    # Adding bins to the solver
    for name, width, height, depth, max_weight in connection_bp_to_db.get_containers_bp_format():
        packer.add_bin(Bin(name=name,
                           width=width,
                           height=height,
                           depth=depth,
                           max_weight=max_weight
                           ))

    # Adding containers to the solver
    for name, cfg in connection_bp_to_db.get_boxes_bp_format().items():
        for i in range(cfg["n"]):
            packer.add_item(Item(f"{name}_{i}",
                                 *cfg["s"]))

    # Setting the parameters of the solver
    solver_params = connection_bp_to_db.get_user_algorithm_parameters()
    packer.pack(bigger_first=solver_params['bigger_first'],
                distribute_items=solver_params['distribute_items'],
                number_of_decimals=solver_params['number_of_decimals'])

    return packer


@error_and_log_handler
def bpp_solution():
    packer = packing_algorithm()
    solution_publisher.export_results_to_report(packer)
    return packer
