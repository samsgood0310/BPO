
#
# All Markdown text in the app exported from this file
#

########################################################################################################################
# ---- How To Use Home Page ----"
########################################################################################################################

how_to_use_main = """
## Welcome to BPO Software

Thank you for choosing BPO Software for solving your packing problems!

### What is Bin Packing Optimization?

Bin Packing Optimization (BPO) is a free, open-source software for solving optimization packing problems. With BPO, 
you can use advanced optimization algorithms and a simple, easy-to-use app to solve your packing problem in minutes, 
saving you time, space, and money.

The solution will be presented in 3D and can be downloaded to your local machine.

### What are Bins and Items?

- Bins: These are multiple containers that represent a space that can hold items. Bins can be any shape or size, 
as long as they have a length, width, and height. - Items: These are the items that you want to pack in the bins. 
Items can be any shape or size, as long as they have a length, width, and height.

### But my bins and items are not Rectangles! What can I do?

The BPO algorithm can only solve problems with rectangular quadrilaterals with four right angles. However, 
you can "calculate" your shapes by finding the minimal rectangle that your bin or item can fit into.

### Core Packages

BPO is a flask application built using the Plotly Dash framework. It uses open-source algorithms and tools to solve 
hard packing problems.

- Plotly-Dash: Used for creating the BPO app
- py3dbp: The solver engine for BPO    
---
"""

########################################################################################################################
# Solver Page
########################################################################################################################
solver_main_page = """
Now, you can set your solver!
As default, you don't have to change any setting here.    

"""
solver_options_table = """

"""
solver_page_user_files_import = """
Advance usage, you can add the files directly to the SW using this 'drag and drop space'.           
Do it only if you know what you are doing :)    
"""

########################################################################################################################
#  containers Page
########################################################################################################################
containers_main_page = """The containers are the "bins" were the packages will be stored. They have the same 
properties as the boxes, and configuration of them are the same as the boxes, except their is no priorities First 
step of solving the packing problem, we need to define the containers that will be loaded to the bins. In the right 
table you will define the sizes and the weight. In the left table you will need to write how many from each container 
you have (and the their rooty)."""

amount_of_containers = """
#### Add the containers to pack
You need to write which kind of container, how many of that item and the priority of them.    
The items will be added to the according to the the priority that you had set, if there won't be any more space.       
containers with low priority won't be conclude in the final pack.
"""

sizes_of_containers = """
#### Set the properties of the Containers types
Here you will set the properties of the containers, the sizes (x,y,z) and the weight (w) of each type of container.      
It's important to name the container in the format of con_(X) were X can be any letter, the name is converted to a 
number for the algorithm.        
"""

########################################################################################################################
# Boxes Page
########################################################################################################################

box_main_page = """
#### Set how many boxes from each type        
The boxes are the items you want to add to your packing problem that will be packed in the containers.
Set how many boxes from each type nad the priority of each bundle (row). The boxes will be added to the according to the
priority that you had set.   
"""

amount_of_box = """  
The boxes are the items you want to add to your packing problem that will be packed in the containers.          
Those items have x, y, z, w and you can set each 'type' in the right table. And in the left table you can set the number
of boxes per each type, and the priority of those boxes.         
"""

sizes_of_box = """
#### Set the properties of the boxes types
Here you will set the properties of the boxes, the sizes (x,y,z) and the weight (w) of each type of box.     
It's important to name the boxes in the format of box(X) were X can be any letter, the name is converted to a ID number 
for the algorithm.        
 
"""

############################################################################################################
# DATA TABLES
############################################################################################################


new_line_for_tables = {
    "box_amount": {
        "key": "boxA",
        "amount": 1,
        "priority": 1,
    },

    "box_properties": {
        "key": "boxA",
        "x": 1,
        "y": 1,
        "z": 1,
        "w": 1,
    },

    "container_properties": {
        "key": "con_a",
        "x": 1,
        "y": 1,
        "z": 1,
        "w": 1,
    },

    "container_amount": {
        "key": "con_a",
        "amount": 1,
        "name": "blue container",

    }
}


OBJECTS_PROP = {
    "container_amount": {
        "button_id": "container-amount-add-row-button",
        "obj_position": {"top": 300, "left": 430},
        "obj_width": {'base': '35%'},
        "table_id": "user-editable-containers-input",
        "obj_description": amount_of_containers
    },

    "container_properties": {
        "button_id": "container-properties-add-row-button",
        "obj_position": {"top": 300, "left": 1123},
        "obj_width": {'base': '35%'},
        "table_id": "user-editable-containers-input-de",
        "obj_description": sizes_of_containers

    },

    "box_amount": {
        "button_id": "add-row-box-amount",
        "obj_position": {"top": 300, "left": 430},
        "obj_width": {'base': '35%'},
        "table_id": "user-editable-boxes-input",
        "obj_description": amount_of_box

    },
    "box_properties": {
        "button_id": "add-row-box-prop",
        "obj_position": {"top": 300, "left": 1123},
        "obj_width": {'base': '35%'},
        "table_id": "user-editable-boxes-input-de",
        "obj_description": sizes_of_box
    },

}


TABLES_PROP = {
    "container_amount": {
        "button_id": "container-amount-add-row-button",
        "obj_position": {"top": 300, "left": 430},
        "obj_width": {'base': '35%'},
        "table_id": "ca-table",
        "delete_row_button_id": "ca-delete-row-btn",
        "add_row_button_id": "ca-add-row-btn",
        "columnDefs": [
            {"headerName": "key", "field": "key", "rowDrag": True, "checkboxSelection": True},
            {"headerName": "amount", "field": "amount", "type": "rightAligned", "filter": "agNumberColumnFilter"},
            {"headerName": "name", "field": "name", "type": "rightAligned", "filter": "agNumberColumnFilter"},
        ]
    },
}