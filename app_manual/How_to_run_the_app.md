## How to run the app?
There are two ways to run the app:

### Running the app using Docker
Option A: Run the container using Docker-Hub run [this script](scripts/run_app_from_dockerhub.sh)
```BASH
/bin/bash ./scripts/run_app_from_dockerhub.sh
```
Option B: Run the container by using the dockerfile and building the image locally use [this document](Docker+Dash.md)
```BASH
/bin/bash ./scripts/dockerize_app.sh
```

#### Running the app using virtual environment
```
#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/Asaf95/bpo.git

# Navigate to the cloned project directory
cd repository

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
source venv/scripts/activate
# On macOS/Linux:
# source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Run the app
python app/main.py  # Replace app_file.py with the main Python file that starts the app
```
