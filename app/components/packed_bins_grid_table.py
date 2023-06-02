"""
This module is a dash component of the AG-grid table.
It's adjusted for the packed bins table in the report

"""

import ast

import dash_ag_grid as dag

from app.system_data import app_data_handler, const_system_data


def __get_pecked_formatted_bin_df():
    bins_df = app_data_handler.get_csv_file(const_system_data.result_file_path['all_bins'])
    bins_df['items_not_in_bin'] = bins_df['items_not_in_bin'].apply(lambda x: ast.literal_eval(x)[0])
    bins_df['items_in_bin'] = bins_df['items_in_bin'].apply(lambda x: ast.literal_eval(x)[0])

    return bins_df


def get_grid():
    columns_to_show = ['bin_name', 'bin_weight', 'number_of_items_in_bin', 'items_in_bin']
    df = __get_pecked_formatted_bin_df()

    return dag.AgGrid(
        id="quickstart-grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in columns_to_show],
        defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 3},
        columnSize="responsiveSizeToFit",
        getRowId="params.data.State"
    )
