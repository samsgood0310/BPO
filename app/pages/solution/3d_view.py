import plotly.graph_objs
from dash import callback, ctx, dcc, html, register_page
from dash.dependencies import Input, Output

from app.assets import style_consts
from app.components import report3d_boxes_types, three_d_graph
from app.logs.app_logger import ErrorHandler, Logger
from app.system_data import app_data_handler


logger = Logger(__name__)
error_and_log_handler = ErrorHandler(logger)

register_page(__name__, icon="material-symbols:3d-rotation")

try:
    layout = html.Div([
        html.Div(
            [html.H1('3D Report', style={'margin-left': '70px'}),
             html.Button('Refresh 3d Graph', id='solve-issue-button', n_clicks=0,
                         style=style_consts.BUTTON_STYLE_REF
                         ),
             ],
            style={'display': 'flex', 'align-items': 'center'}
        ),
        report3d_boxes_types.get_boxes_type_report(),
        dcc.Graph(id="3d-graph", style=style_consts.MAIN_3D_LAYOUT_STYLE)
    ],
        style={'margin-left': '70px', 'width': 1400}
    )
except Exception as e:
    logger.error(f"modify_layout function didn't work {e}")
    raise e


@callback(
    Output("3d-graph", "figure"),
    Input("solve-issue-button", "n_clicks"),
)
@error_and_log_handler
def display_3d_figure(_) -> plotly.graph_objs.Figure:
    """
    if the user click the button the graph will be showed, and the current copy of the figure will be saved locally.
    if the user didn't click the button the last figure that were saved will be returned
    :return:
    """
    if ctx.triggered_id == "solve-issue-button":
        last_fig = three_d_graph.general_3d_graph()
        app_data_handler.save_locally_pickle_file("3d_solution_figure",
                                                  last_fig)  # Saving the figure as the last fig
        report3d_boxes_types.get_boxes_type_report()
        logger.info("a new 3d_solution_figure was created and updated in the App")
    else:
        last_fig = app_data_handler.get_pickle_file("3d_solution_figure")
        if last_fig is None:
            last_fig = three_d_graph.general_3d_graph()

        logger.info("the last 3d_solution_figure was updated in the App")
    if last_fig is None:
        raise 'Cant get 3d fig'
    return last_fig
