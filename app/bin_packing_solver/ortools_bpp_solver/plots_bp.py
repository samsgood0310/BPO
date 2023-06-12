"""
WORK IN PROGRESS
"""

import plotly.express as px

# Define the data for the bins and the items
bins_data = [
    {"x": (0, 100), "y": (0, 200), "z": (0, 300), "name": "Bin 1"},
    {"x": (100, 200), "y": (0, 200), "z": (0, 300), "name": "Bin 2"},
    # ...
]
items_data = [
    {"x": 50, "y": 100, "z": 150, "name": "Item 1", "bin": "Bin 1"},
    {"x": 150, "y": 100, "z": 150, "name": "Item 2", "bin": "Bin 2"},
    # ...
]

# Create a figure with the bins and items
fig = px.scatter_3d(
    bins_data + items_data,
    x="x",
    y="y",
    z="z",
    color="name",
    title="Bins and items"
)

# Add a custom data label for each item
for item in items_data:
    fig.add_annotation(
        x=item["x"],
        y=item["y"],
        z=item["z"],
        text=item["name"],
        font=dict(color="white")
    )

# Show the figure
fig.show()
