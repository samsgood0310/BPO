
import dash_mantine_components as dmc
from dash import dcc, html, register_page

from app.assets import style_consts, app_consts
from app.utils.common_functions import get_picture


register_page(__name__, path="/", icon="ant-design:home-filled")


Img_sidebar = dmc.Navbar(
    fixed=True,
    width={"base": "25%"},
    position={"top": 260, "left": 1365},
    style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
    children=[
        html.Img(
            src=get_picture("containers_in_blue"), height="70%", width="100%",
        ),
    ]
)
Main_MD = dmc.Navbar(
    fixed=True,
    width={"base": "50%"},
    position={"top": 50, "left": 400},
    style=style_consts.MAIN_LAYOUT_STYLE,  # backgroundColor for the menu
    children=[
        dmc.Title("Bin Packing Optimization ",
                  style={'textAlign': 'center'}),
        html.H3("let's solve your packing problem!",
                style={'textAlign': 'center'}),
        dmc.Space(h=2),
        dmc.Divider(),
        dmc.Space(h=5),
        dcc.Markdown(
            app_consts.how_to_use_main,
            link_target="_blank",
        ),
        dmc.Divider(),
    ]
)

layout = dmc.Container([
        dmc.Divider(),
        Main_MD,
        Img_sidebar,
], style=style_consts.MAIN_LAYOUT_STYLE, ml="10%")
