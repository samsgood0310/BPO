from dash import html

from app.assets import style_consts
from app.components.three_d_graph import const_bpa
from app.system_data import app_data_handler


def __background_color(key):
    colors = const_bpa.colors
    color = colors[ord(key.split("_")[0][-1]) - ord("A")]
    return color


def __style_object(key):
    color_obj = {'backgroundColor': __background_color(key)}
    color_obj.update(style_consts.LEGEND_COLOR)
    return color_obj


def get_boxes_type_report():
    return html.Div(style=style_consts.LEGEND_DIV_WRAPPER,
                    children=[
                        html.Div(style=style_consts.LEGEND_ITEM_WRAPPER,
                                 children=[
                                     html.Div(item),
                                     html.Div(children=" ", style=__style_object(item))
                                 ]) for item in app_data_handler.get_box_types_keys()
                    ])
