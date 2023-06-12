
## What can be a box and container?
In the context of the bin packing problem, a **box** is an item that needs to be packed into the containers or bins. 
A box is a storage object that typically has properties such as x, y, z, and weight (w). These properties define the
dimensions and weight of the box. For example, a box may have a length (x), width (y), height (z), and weight (w),
which are used to describe its size and mass.

A **container** refers to the bins or objects in which the boxes are placed. It serves as a storage unit for holding the boxes.
In the bin packing problem, a container can be any object or structure that provides space to accommodate the boxes. 
The container must have properties like x, y, z, and weight (w) to define its dimensions and weight restrictions. 
The size and weight capacity of the container determine how many and which boxes can fit inside it.

It's important to note that in the bin packing problem, the terms "box" and "container" are used interchangeably. 
The main objective is to find an optimal packing arrangement, considering the dimensions and weight of the boxes, 
to minimize wasted space and efficiently utilize the containers.

By treating the storage object as a container and the items to be stored as boxes, the bin packing problem allows for 
flexible representations of the objects involved. This flexibility enables the problem to be applied to a wide range of 
scenarios where various types of objects need to be packed into different kinds of storage units,
maximizing space utilization and minimizing the number of containers required.

### Boxes Colors

#### According to what the items get there color?
In the [three_d_graph.py](../app/components/three_d_graph.py)
We have this line of code 
```
ret["color"] = colors[ord(item.name.split("_")[0][-1]) - ord("A")]
```
This line of code is assigning a color value to the "color" key in a dictionary named ret.

The color value is determined based on the last character of the first part of an item name. The item name is split into two parts separated by an underscore "_", and the first part's last character is used to determine the index of the color in the colors list.

Here's a breakdown of the line:

1. item.name.split("_")[0]: This splits the item's name into two parts separated by an underscore and selects the first part. 
2. item.name.split("_")[0][-1]: This selects the last character of the first part of the item's name. 
3. ord(item.name.split("_")[0][-1]) - ord("A"): This converts the selected character to its ASCII code and subtracts the ASCII code of "A" from it. This gives a zero-based index of the color to use. 
4. colors[ord(item.name.split("_")[0][-1]) - ord("A")]: This selects the color from the colors list based on the index calculated in step 3. 
5. ret["color"] = colors[ord(item.name.split("_")[0][-1]) - ord("A")]: This assigns the selected color to the "color" key in the ret dictionary.
