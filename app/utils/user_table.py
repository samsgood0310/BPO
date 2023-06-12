#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from dash import ctx

from app.system_data import app_data_handler, const_system_data
from app.assets import app_consts
from app.logs.app_logger import Logger, ErrorHandler

logger = Logger(__name__)
log_and_handle_errors = ErrorHandler(logger)


@log_and_handle_errors
def update_table(user_table, add_btn_id, table_name):
    try:
        if not user_table:
            user_table = app_data_handler.get_csv_without_index(
                const_system_data.input_file_path.get(table_name)).to_dict('records')

        elif ctx.triggered_id == add_btn_id:
            new_line = pd.DataFrame(app_consts.new_line_for_tables[table_name], index=[0])
            user_table = pd.concat([pd.DataFrame(user_table), new_line], ignore_index=True)
            user_table = user_table.to_dict("records")

        else:
            user_table = pd.DataFrame(user_table).to_dict('records')
            app_data_handler.input_files_input(const_system_data.input_file_path.get(
                table_name), pd.DataFrame(user_table))
        return user_table, user_table

    except Exception as error:
        logger.error(message=f"function = update_store_data_of_boxes_amount_data error: {error}")
