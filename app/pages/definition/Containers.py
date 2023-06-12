#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# Containers page of the app, part of "dash-plotly multi-page structure"
# ************************************************************************************
#
import dash_mantine_components as dmc
from dash import Input, Output, callback, dcc, html, register_page
from dash.dependencies import State

from app.assets import style_consts, app_consts
from app.components import user_defined_container
from app.logs.app_logger import Logger
from app.utils.common_functions import get_picture
from app.utils.user_table import update_table


logger = Logger(__name__)

register_page(__name__, icon="fluent:bin-full-20-regular",
              suppress_callback_exceptions=True)

try:
    load_containers = user_defined_container.get_obj("container_amount")
    containers_define = user_defined_container.get_obj("container_properties")

    page_pic = dmc.Navbar(
        fixed=True,
        width={'base': '35%'},
        position={"top": 30, "left": 1123},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            html.Img(src=get_picture("container_with_boxes"), height="30%", width="100%"),
        ]
    )

    Page_Description = dmc.Navbar(
        fixed=True,
        width={'base': '35%'},
        position={"top": 50, "left": 430},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            dmc.Divider(style={'textAlign': 'center'}),
            html.H2("Define and Load the containers", style={'textAlign': 'center'}),
            dmc.Divider(style={'textAlign': 'center'}),
            dcc.Markdown(app_consts.containers_main_page),
        ]
    )

    layout = dmc.Container([
        dcc.Store(id='containers_amount_data', data={}, storage_type='local'),
        dcc.Store(id='containers_definition_data', data={}, storage_type='local'),
        dmc.Container([
            html.Div([html.Div([Page_Description]),
                      html.Div([page_pic])
                      ]),
            dmc.Container([
                html.Div([html.Div([load_containers]),
                          html.Div([containers_define])
                          ]),
            ])
        ], fluid=False),
    ],
        style=style_consts.DEFAULT_COMPONENT_CENTER,
    )
except Exception as e:
    logger.error(f"the layout of Container page is broken, error: \n {e}")


@callback(Output('containers_amount_data', 'data'),
          Output('user-editable-containers-input', 'data'),
          Input('user-editable-containers-input', 'data'),
          Input('container-amount-add-row-button', 'n_clicks'),
          State('user-editable-containers-input', 'columns'))
def update_store_data_of_containers_amount_data(current_containers_def_df, _, __):
    return update_table(user_table=current_containers_def_df,
                        add_btn_id="container-amount-add-row-button",
                        table_name="container_amount")


@callback(Output('containers_definition_data', 'data'),
          Output('user-editable-containers-input-de', 'data'),
          Input('user-editable-containers-input-de', 'data'),
          Input('container-properties-add-row-button', 'n_clicks'),
          State('user-editable-containers-input-de', 'columns'))
def update_store_data_of_containers_amount_data(current_containers_def_df, _, __):
    return update_table(user_table=current_containers_def_df,
                        add_btn_id="container-properties-add-row-button",
                        table_name="container_properties")
