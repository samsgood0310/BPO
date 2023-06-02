from dash import Input, Output, callback, html, register_page

from app.assets import style_consts
from app.components import packed_bins_grid_table, report_kpis
from app.logs.app_logger import Logger


logger = Logger(__name__)
register_page(__name__, icon="iconoir:stats-report", suppress_callback_exceptions=True)

try:
    layout = html.Div([
            html.Div(
                [html.H1('KPI Dashboard', style={'margin-left': '70px'}),
                 html.Button(
                     'Refresh KPI Report', id='kpis-report-button', n_clicks=0,
                     style=style_consts.BUTTON_STYLE_REF
                    ),
                 ],
                style={'display': 'flex', 'align-items': 'center'}
            ),
            html.Div(id="kpis-report-out", style=style_consts.MAIN_3D_LAYOUT_STYLE),
        ],
        style={'margin-left': '70px', 'width': 1400}
    )
except Exception as e:
    logger.error(f"the layout of 3d_figure page is broken, error: \n {e}")


@callback(Output("kpis-report-out", "children"), [Input("kpis-report-button", "n_clicks")])
def display_3d_figure(_):
    """
    If the user clicks the button, the graph will be shown, and the current copy of the figure will be saved locally.
    If the user doesn't click the button, the last figure that was saved will be returned.
    """
    return [
            html.Div(report_kpis.display_bins_kpis()),
            html.Div([packed_bins_grid_table.get_grid()])
        ]
