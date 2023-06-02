## What are Boxes and Containers?
The bin packing problem is a classic optimization problem in computer science and mathematics that involves packing a set
of items into a minimum number of containers or bins of a given size. The problem is to find the best way to pack the items
into the bins while minimizing the number of bins used and without exceeding the capacity of the bins.



### Boxes Colors

#### According to what the items get there color?
In the [three_d_graph.py](bpo/app/bin_packing_solver/py3dbp_solver/three_d_graph.py)
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
