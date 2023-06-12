#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# Solver page of the app, part of "dash-plotly multi-page structure"
# ************************************************************************************
#
import base64
import datetime
import io

import dash_mantine_components as dmc
import pandas as pd
from dash import (Input, Output, callback, ctx, dash_table, dcc, html,
                  register_page)
from dash.dependencies import State

from app.assets import style_consts, app_consts
from app.logs.app_logger import Logger
from app.scripts import exe_sys_scripts
from app.system_data import app_data_handler, const_system_data
from app.utils.common_functions import get_picture


logger = Logger(__name__)

register_page(__name__, icon="grommet-icons:configure", suppress_callback_exceptions=True)


def get_reports_names() -> list:
    """
    Using this function to get the user input files from the local system data storage.
    Taking only the csv files from that directory by the if statement that check the end of the filenames.
    """
    return [val for val in app_data_handler.get_files_names("user_input_files") if val.endswith(".csv")]


def process_user_data(contents, filename, date) -> html.Div:
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            raise "Fail to upload the file, make sure your files are csv or xls formats"
        app_data_handler.user_input_csv(filename, df)

        return html.Div([
            html.H5(filename),
            html.H6("last updated " + str(datetime.datetime.fromtimestamp(date))),
            dash_table.DataTable(df.to_dict('records'), [{'name': i, 'id': i} for i in df.columns]),
            html.Hr()])
    except Exception as error:
        logger.error(f"process_user_data function in the solver page is broken, error: \n {e}")
        raise error


try:
    user_solver_params = dmc.Navbar(
        fixed=False,
        position={"top": 0, "left": 500},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            dmc.Divider(style={'textAlign': 'center'}),
            html.H2("Set the Solver", style={'textAlign': 'center'}),
            dmc.Divider(style={'textAlign': 'center'}),
            dcc.Markdown(app_consts.solver_main_page),
            html.Br(),
            dcc.Markdown(app_consts.solver_options_table,
                         link_target="_blank",
                         ),
            html.Div([
                dash_table.DataTable(
                    id='user-datatable-solver-params',
                    columns=[{'name': i, 'id': i} for i in
                             app_data_handler.get_csv_without_index(
                                 const_system_data.input_file_path.get('user_algorithm_params')).columns],
                    editable=True,
                    row_deletable=False,
                    style_header=style_consts.DATATABLE_HEADER_STYLE,
                    style_data=style_consts.USER_BOX_DATATABLE_STYLE,
                    page_size=5,  # we have fewer data in this example, so setting to 20
                    # style_table=style_consts.STYLE_TABLE_BOX
                )],
                # style=style_consts.DEFAULT_COMPONENT_CENTER
            ),
            dcc.Markdown("""
            #### Restore to default user files
            Something went wrong? want to make sure your data was deleted from he machine?     
            Use this button and all the files that you uploaded, or files that generated using your data will be deleted
            """),
            html.Button('Restore files', id='restore-default-user-files', n_clicks=0,
                        style=style_consts.BUTTON_STYLE),

            dmc.Space(h=60),
            dcc.Markdown("#### Import the user-files as CSV"),
            dcc.Markdown(app_consts.solver_page_user_files_import),
            dcc.Upload(
                id='user-upload-data-file',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style=style_consts.DROP_FILES_AREA_STYLE,
                multiple=True
            ),
            html.Div(id='output-of-user-upload-data-file'),
            html.Div(id='container-button-timestamp'),
            html.Br(),
        ]
    )

    Img_sidebar = dmc.Navbar(
        fixed=True,
        width={"base": "25%"},
        position={"top": 200, "left": 1365},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            html.Img(
                src=get_picture("organize_boxes"), height="70%", width="100%",
            ),
        ]
    )
    layout = dmc.Container([
        dcc.Store(id='solver-params', data={}, storage_type='local'),
        user_solver_params,
        Img_sidebar,

    ], style=style_consts.MAIN_LAYOUT_STYLE, ml="10%"
    )

except Exception as e:
    logger.error(f"the layout of Solver page is broken, error: \n {e}")
    raise e


@callback(Output('output-of-user-upload-data-file', 'children'),
          Input('user-upload-data-file', 'contents'),
          State('user-upload-data-file', 'filename'),
          State('user-upload-data-file', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates) -> list:
    if list_of_contents is not None:
        return [process_user_data(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]


@callback(Output('solver-params', 'data'),
          Output('user-datatable-solver-params', 'data'),
          Input('user-datatable-solver-params', 'data'),
          State('user-datatable-solver-params', 'columns'))
def update_store_data_of_boxes_amount_data(solver_params_df, _):
    try:
        if not solver_params_df:
            solver_params_df = app_data_handler.get_csv_without_index(
                const_system_data.input_file_path.get("user_algorithm_params")).to_dict('records')
        else:
            solver_params_df = pd.DataFrame(solver_params_df).to_dict('records')
            app_data_handler.input_files_input(const_system_data.input_file_path.get(
                "user_algorithm_params"), pd.DataFrame(solver_params_df))
        return solver_params_df, solver_params_df

    except Exception as error:
        logger.error(message=f"function = update_store_data_of_boxes_amount_data error: {error}")
        raise error


@callback(
    Output('container-button-timestamp', 'children'),
    Input("restore-default-user-files", "n_clicks"),
)
def restore_user_files(_):
    """
    if the user click the button the graph will be showed, and the current copy of the figure will be saved locally.
    if the user didn't click the button the last figure that were saved will be returned
    :return:
    """
    try:
        if "restore-default-user-files" == ctx.triggered_id:
            exe_sys_scripts.run_bash_script("restore_user_files")
            logger.info("Restore the data button was triggered ")
            msg = "Restore the data"
        else:
            msg = ""

        return html.Div(msg)

    except Exception as error:
        logger.error(message=f"function = restore_user_files error: {error}")
        raise error
