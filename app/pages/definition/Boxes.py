"""
____MODEL_INFO____
Need to create two pages,
One for the definition of the box, item.
And the other is for other is for amount of bins, boxes of the current problem.

This way we will have 4 dcc store for each user dataframe.
Might use definition
"""
import dash_mantine_components as dmc
from dash import Input, Output, callback, dcc, html, register_page
from dash.dependencies import State

from app.assets import style_consts, app_consts
from app.components import user_defined_container
from app.logs.app_logger import Logger
from app.utils.common_functions import get_picture
from app.utils.user_table import update_table


logger = Logger(__name__)

register_page(__name__, icon="bi:box", suppress_callback_exceptions=True)

try:
    load_boxes = user_defined_container.get_obj("box_amount")

    boxes_define = user_defined_container.get_obj("box_properties")

    Page_Description = dmc.Navbar(
        fixed=True,
        width={'base': '35%'},
        position={"top": 50, "left": 430},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            dmc.Divider(style={'textAlign': 'center'}),
            html.H2("Define and Load the Boxes",
                    style={'textAlign': 'center'}),
            dmc.Divider(style={'textAlign': 'center'}),
            dcc.Markdown(app_consts.amount_of_box),
        ]
    )

    page_pic = dmc.Navbar(
        fixed=True,
        width={'base': '35%'},
        position={"top": 30, "left": 1123},
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            html.Img(src=get_picture("boxes_in_mess"), height="30%", width="100%"),
        ]
    )

    layout = dmc.Container([
        dcc.Store(id='boxes_amount_data', data={}, storage_type='local'),
        dcc.Store(id='boxes_definition_data', data={}, storage_type='local'),
        dmc.Container([
            html.Div([html.Div([Page_Description]),
                      html.Div([page_pic])
                      ]),
            dmc.Container([
                html.Div([html.Div([load_boxes]),
                          html.Div([boxes_define])
                          ]),
            ]),
        ], fluid=False),
    ],
        style=style_consts.DEFAULT_COMPONENT_CENTER,
    )
except Exception as e:
    logger.error(f"the layout of Boxes page is broken, error: \n {e}")


@callback(Output('boxes_amount_data', 'data'),
          Output('user-editable-boxes-input', 'data'),
          Input('user-editable-boxes-input', 'data'),
          Input('add-row-box-amount', 'n_clicks'),
          State('user-editable-boxes-input', 'columns')
          )
def update_store_data_of_boxes_amount_data(current_boxes_def_df, _, __):
    return update_table(user_table=current_boxes_def_df,
                        add_btn_id="add-row-box-amount",
                        table_name="box_amount")


@callback(Output('boxes_definition_data', 'data'),
          Output('user-editable-boxes-input-de', 'data'),
          Input('user-editable-boxes-input-de', 'data'),
          Input('add-row-box-prop', 'n_clicks'),
          State('user-editable-boxes-input-de', 'columns')
          )
def update_store_data_of_boxes_amount_data(boxes_prop_df, _, __):
    return update_table(user_table=boxes_prop_df,
                        add_btn_id="add-row-box-prop",
                        table_name="box_properties")
