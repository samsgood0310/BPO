import plotly.graph_objects as go
from plotly.subplots import make_subplots

from app.bin_packing_solver.py3dbp_solver import (connection_bp_to_db,
                                                  const_bpa, solver)
from app.logs.app_logger import ErrorHandler, Logger


logger = Logger(__name__)

error_and_log_handler = ErrorHandler(logger)


@error_and_log_handler
def add_item_to_packing_subplot(item):
    def __resize_item_according_to_vertices(
            xmin=0, ymin=0, zmin=0, xmax=1, ymax=1, zmax=1):
        """ resize_item_according_to_vertices"""
        return {
            "x": [xmin, xmin, xmax, xmax, xmin, xmin, xmax, xmax],
            "y": [ymin, ymax, ymax, ymin, ymin, ymax, ymax, ymin],
            "z": [zmin, zmin, zmin, zmin, zmax, zmax, zmax, zmax],

            "i": [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            "j": [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            "k": [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        }

        # take a packer item and build parameters to a plotly mesh3d cube
    colors = const_bpa.colors
    ret = __resize_item_according_to_vertices(
        *item.position,
        *[sum(x) for x in
          zip(item.position, item.get_dimension())]
    )
    ret["name"] = item.name
    ret["color"] = colors[ord(item.name.split("_")[0][-1]) - ord("A")]
    # ret["flatshading"] =  True
    return ret


@error_and_log_handler
def create_cube_border_trace(item):
    xmin, ymin, zmin = item.position
    xmax, ymax, zmax = [sum(x) for x in zip(item.position, item.get_dimension())]

    border_points = [
        [xmin, ymin, zmin],
        [xmax, ymin, zmin],
        [xmax, ymax, zmin],
        [xmin, ymax, zmin],
        [xmin, ymin, zmin],
        [xmin, ymin, zmax],
        [xmax, ymin, zmax],
        [xmax, ymax, zmax],
        [xmin, ymax, zmax],
        [xmin, ymin, zmax],
        [xmax, ymin, zmax],
        [xmax, ymin, zmin],
        [xmax, ymax, zmin],
        [xmax, ymax, zmax],
        [xmin, ymax, zmax],
        [xmin, ymax, zmin]
    ]

    border_trace = {
        "type": "scatter3d",
        "x": [point[0] for point in border_points],
        "y": [point[1] for point in border_points],
        "z": [point[2] for point in border_points],
        "mode": "lines",
        "line": {
            "color": "black",
            "width": 2
        },
        "showlegend": False  # Add this line to hide the legend
    }

    return border_trace


@error_and_log_handler
def create_box_type_trace(items):
    types = set(item.name.split("_")[0] for item in items)
    colors = const_bpa.colors
    xs, ys, zs, names, colors_list = [], [], [], [], []
    for i, t in enumerate(types):
        xs.append(None)
        ys.append(None)
        zs.append(None)
        names.append(t)
        colors_list.append(colors[i])

    return go.Scatter3d(x=xs, y=ys, z=zs, mode="markers+text", text=names, marker=dict(color=colors_list))


@error_and_log_handler
def adjust_the_figure(fig):
    """
    this function create the layout of the figure on the UI.
    From here the location / size of the graph can be changed.
    things that can be added / changes:
    # autosize=True,
    # legend=dict(xanchor="center", x=0.3, y=0.1),
    """
    return fig.update_layout(
        margin={"l": 0, "r": 0, "t": 100, "b": 100},
        width=1450,
        height=len(connection_bp_to_db.get_containers_bp_format()) * 1500,
        margin_b=50,
        plot_bgcolor='#ebf7ff',
        paper_bgcolor='#ebf7ff'
    )


def modify_layout(scene):
    """
    This Function resize the 'scene' of each graph in the Figure

    Things you can change
    # Show as 3d
    # scene.camera = dict(eye=dict(x=-2, y=2, z=2),
    #                     up=dict(x=-1, y =0 ,z =1))
    # scene.yaxis.spikemode = "toaxis"
    # scene.zaxis.spikemode = "toaxis"
    """
    try:
        scene.aspectmode = 'data'

        # Show as 2d
        scene.camera = dict(eye=dict(x=0, y=0, z=4),
                            up=dict(x=-1, y=0, z=1))

        scene.xaxis.title = "X axis"
        scene.yaxis.title = "Y axis"
        scene.zaxis.title = "Z axis"
        scene.xaxis.showspikes = True
        scene.yaxis.showspikes = True
        scene.zaxis.showspikes = True
        scene.xaxis.spikesides = True
        scene.xaxis.spikethickness = 1
        scene.yaxis.spikethickness = 1
        scene.zaxis.spikethickness = 1

        return scene

    except Exception as error:
        logger.error(f"modify_layout function didn't work {error}")
        raise error


@error_and_log_handler
def general_3d_graph():
    try:
        packer = solver.bpp_solution()

        # creating the figure that will contain all the graphs
        fig = make_subplots(rows=len(packer.bins),
                            cols=1,
                            specs=[[{"type": "mesh3d"}] for _
                                   in range(len(connection_bp_to_db.get_containers_bp_format()))],
                            subplot_titles=[f"{i.name}" for i
                                            in packer.bins],
                            )

        # add a trace for each packer item
        for row, pbin in enumerate(packer.bins):
            for item in pbin.items:

                fig.add_trace(go.Mesh3d(add_item_to_packing_subplot(item)),
                              row=row + 1,
                              col=1)

                # Adding border for each item
                fig.add_trace(go.Scatter3d(create_cube_border_trace(item)),
                              row=row + 1,
                              col=1)

        fig = adjust_the_figure(fig)
        fig.for_each_scene(fn=modify_layout)

        return fig
    except Exception as error:
        logger.error(f"the general_3d_graph function is broken, error: \n {error}")
