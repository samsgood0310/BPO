"""
This module creates the application framework.
It contains all containers for each component in the app and the style configuration for it
"""
import dash
import dash_mantine_components as dmc
from dash import Dash, dcc, html

from app.assets import style_consts
from app.components import app_sidebar
from app.logs.app_logger import Logger

logger = Logger(__name__)
logger_s = Logger(__name__, log_mode="system")

"----------------------------------------------------  Application  ---------------------------------------------------"
# If you want to use a  theme, refactor the assets dir to assets, the dbc.themes.LUX is located there by default
# And don't forget to import dash_bootstrap_components as dbc first
app = Dash(__name__, use_pages=True)
server = app.server
app.title = 'BPO'

"---------------------------------------------  Application Main layout  ----------------------------------------------"
app.layout = html.Div(style=style_consts.MAIN_APP_STYLE,
                      children=[dmc.Container(
                          [
                              dcc.Store(id='memory-output', storage_type='session'),
                              dcc.Store(id='all_user_files', data={}, storage_type='session'),
                              dmc.Header(
                                  height=30,
                                  style=style_consts.APP_TOP_MARGIN,
                                  fixed=True,
                              ),
                              app_sidebar.get_sidebar(),
                              dmc.Container(
                                  dash.page_container,
                                  pt='3%',
                                  ml='20%',
                                  style=style_consts.LAYOUT_CONTENT_STYLE,
                              ),
                          ],
                          fluid=True,
                          style=style_consts.MAIN_LAYOUT_STYLE,
                      )]
                      )


###############################################################
# Comment out everything below if you want to dockerized the app
###############################################################
def main():
    try:
        app.run_server(debug=True, port=8881)
        logger_s.info("up was started using debug=True, port=8881")
    except Exception as Error:
        raise f"Main App Startup didn't worked!! Check the following Error: \n {Error}"


if __name__ == "__main__":
    main()
