import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dash_table, dcc, html

from app.assets import style_consts, app_consts
from app.logs.app_logger import ErrorHandler, Logger
from app.system_data import app_data_handler, const_system_data

logger = Logger(__name__)
error_and_log_handler = ErrorHandler(logger)
TABLES_PROP = app_consts.TABLES_PROP
OBJECTS_PROP = app_consts.OBJECTS_PROP


def __get_grid(input_container_name):
    df = app_data_handler.get_csv_without_index(
        const_system_data.input_file_path.get(input_container_name))
    return dag.AgGrid(
        id=OBJECTS_PROP[input_container_name].get("table_id"),
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        defaultColDef={"resizable": True, "sortable": True, "filter": True, "editable": True, "minWidth": 125},
        columnSize="sizeToFit",
    )


def __get_datatable(input_container_name):
    return dash_table.DataTable(
        id=OBJECTS_PROP[input_container_name].get("table_id"),
        columns=[{'name': i, 'id': i} for i in
                 app_data_handler.get_csv_without_index(
                     const_system_data.input_file_path.get(input_container_name)).columns],
        editable=True,
        row_deletable=True,
        style_header=style_consts.DATATABLE_HEADER_STYLE,
        style_data=style_consts.USER_BOX_DATATABLE_STYLE,
        page_size=5,
        style_table=style_consts.STYLE_TABLE_BOX
    )


@error_and_log_handler
def get_obj(input_container_name):
    return dmc.Navbar(
        width=OBJECTS_PROP[input_container_name].get("obj_width"),
        fixed=True,
        position=OBJECTS_PROP[input_container_name].get("obj_position"),
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            html.Br(),
            dcc.Markdown(OBJECTS_PROP[input_container_name].get("obj_description"), link_target="_blank"),
            dbc.Button("Add Row", n_clicks=0, id=OBJECTS_PROP[input_container_name].get("button_id"), size="sm",
                       style=style_consts.BUTTON_STYLE),
            html.Div([
                # __get_grid(input_container_name)
                __get_datatable(input_container_name)
            ],
                style=style_consts.DEFAULT_COMPONENT_CENTER),
        ]
    )


def __create_ad_grid_dag(input_container_name):
    """
    this function create the content of a AdGrid table (dag)
    :return:
    """
    df = app_data_handler.get_csv_without_index(
        const_system_data.input_file_path.get(input_container_name))
    return dag.AgGrid(
        id=TABLES_PROP[input_container_name].get("table_id"),
        className="ag-theme-alpine-dark",
        columnDefs=TABLES_PROP[input_container_name].get("table_id"),
        rowData=df.to_dict("records"),
        defaultColDef={"filter": True, "floatingFilter": True, "resizable": True, "sortable": True, "editable": True,
                       "minWidth": 150},
        columnSize="sizeToFit",
        dashGridOptions={"undoRedoCellEditing": True}
    )


def get_ad_grip_table(input_container_name):
    return dmc.Navbar(
        width=TABLES_PROP[input_container_name].get("obj_width"),
        fixed=True,
        position=TABLES_PROP[input_container_name].get("obj_position"),
        style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
        children=[
            html.Br(),
            dcc.Markdown(app_consts.amount_of_containers, link_target="_blank"),
            dbc.Button("Add Row", n_clicks=0, id=TABLES_PROP[input_container_name].get("button_id"), size="sm",
                       style=style_consts.BUTTON_STYLE),
            html.Div(
                [
                    dbc.CardBody(
                        [
                            __create_ad_grid_dag(input_container_name),
                            html.Span(
                                [
                                    dbc.Button("Delete row",
                                               id=TABLES_PROP[input_container_name].get("delete_row_button_id"),
                                               color="secondary",
                                               size="md", className='mt-3 me-1'),
                                    dbc.Button("Add row", id=TABLES_PROP[input_container_name].get("add_row_button_id"),
                                               color="primary", size="md",
                                               className='mt-3')
                                ]
                            ),
                        ]
                    ),
                ],
                style={"margin": 20},
            ),
        ]
    )
