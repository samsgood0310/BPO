# Application Structure
The BPO web-application is based on Dash-Plotly framework / packages, while the backed data-process and the solver Algorithm use mostly Pandas objects and customized modules and functions that were wrote for this app.    
with that say, each part of the app can run independently and this why other algorithms and applications with other use-cases can use this framework.    

## Dash-Plotly App

**The following is an overview of the app structure**    
bpo       
├── .venv       
│   └── *.                   
├── requirements.txt       
├── .gitignore       
├── License       
├── README.md       
├── Dockerfile       
└── app       
    ├── assets       
    │   └── *.      
    ├── bin_packing_solver       
    │   └── *.   
    ├── components       
    │   └── *.    
    ├── logs       
    │   └── *.           
    ├── pages       
    │   ├── section       
    │   │   ├── page1.py       
    │   │   └── *.            
    │   ├── home.py       
    ├── scripts       
    │   └── *.           
    ├── system_data       
    │   └── *.    
    ├── utils       
    │   └── *.           
    └── main.py

app/asserts: all the static settings, text and style of the app and the project.     
app/bin_packing_solver: the packing solvers, currently it contain only one solver and another one in dev process.             
the directory have also the data-import & aggregation module and both the export module of the solution to the system_data.      
app/components: dash components of the app, pages are using those components.                        
app/logs: all the app/system logs, it also have the module with the class of the ErrorHandle and loger that is used in the app.      
app/pages: all the pages in the app are under that directory, the subdirectories are sections that are visible on the 
sidebar component and also configured from the sidebar component.     
app/scripts: here will be all the scripts (mostly in Bash) that the app is triggered.      
app/system_data: All the files that the system/app is using, saving the user input, the solution results, and caching some objects in the app.      
app/utils: tools, and modules that the app is using.

the imports aligns with both ```Docker``` and ```.venv``` execture methods.     
Every internal import in the app should be imported from the app layer,      
for example:
``` from app.logs.app_logger import Logger   ```



### Lines of code 
git ls-files | grep '\.py' | xargs wc -l

### Delete __pycache__ files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf