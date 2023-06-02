import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html

from app.utils import calculate_kpis


def create_bar_chart(chart_title, data):
    all_items = list(data.keys())
    percentages = [int(x.split('%')[0]) for x in data.values()]
    num_items = [int(x.split('(')[1].split('/')[0]) for x in data.values()]
    num_used_items = [int(x.split('/')[1].split(')')[0]) for x in data.values()]
    result = [b - a for a, b in zip(num_items, num_used_items)]

    # Create the text labels for the top of each bar
    labels = [f"{p}% ({n}/{m})" for p, n, m in zip(percentages, num_used_items, num_items)]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=all_items, y=num_items, name='Used items', text=labels, textposition='auto'))
    fig.add_trace(go.Bar(x=all_items, y=result, name='Unused items'))

    fig.update_layout(
        title={
            'text': chart_title,
            'font': {
                'size': 20
            }
        },        xaxis_title="Types of items",
        yaxis_title="Number of items",
        barmode='stack',
        plot_bgcolor='#ebf7ff',
        paper_bgcolor='#f1f7fd'
    )

    return dcc.Graph(figure=fig)


def __item_format_in_kpis(item_name, item):
    return html.Div(children=[
        html.H4(children=item_name),
        html.Div(children=item)
    ], className='kpi-card', style={'margin-right': '30px'})


def __parse_boxes_packed_per_box_type(boxes_packed_per_box_type_dict):
    result = []
    for box, data in boxes_packed_per_box_type_dict.items():
        ratio, ratio_str, num_packed, total = data.split(' ')
        result.append({'Box Type': box, 'Packed Ratio': float(ratio.rstrip('%')) / 100, 'Packed Items': int(num_packed),
                       'Total Items': int(total)})
    return result


def display_bins_kpis():
    bins_total_items, bins_unpacked_items, bins_percent_packed, boxes_packed_per_box_type, \
        overview_total_packed_weight, overview_total_input_boxes_wight, overview_total_input_bins_wight, \
        bins_utilizations, bins_total_utilization_str = calculate_kpis.collect_kpis_to_report()

    boxes_packed_per_box_type_dict = pd.Series(boxes_packed_per_box_type).to_dict()
    bin_utilization_bars = create_bar_chart('Container Utilisation', bins_utilizations)
    boxes_utilization_bars = create_bar_chart('Boxes Utilisation', boxes_packed_per_box_type_dict)

    # create HTML div
    return html.Div(
        children=[
            # Total KPIs
            html.Div(children=[
                __item_format_in_kpis('Packed Boxes', str(int(bins_percent_packed * 100)) + "% " + "(" +
                                      str((bins_total_items - bins_unpacked_items)) + "/" + str(bins_total_items) + ")"),
                __item_format_in_kpis('Number of Boxes', bins_total_items),
                __item_format_in_kpis('Unpacked Boxes', bins_unpacked_items),
                __item_format_in_kpis('Packed Weight', overview_total_packed_weight),
                __item_format_in_kpis('Input Boxes Weight', overview_total_input_boxes_wight),
                __item_format_in_kpis('Input Containers Weight', overview_total_input_bins_wight),
                __item_format_in_kpis('Containers Utilization', bins_total_utilization_str)
            ], className='kpi-container', style={'display': 'flex'}),

            html.Div(children=[boxes_utilization_bars], className='my-bar'),
            html.Div(children=[bin_utilization_bars], className='my-bar-chart'),
        ],
    )
