#!/bin/bash

## --------------------------------------------------------------------------------
## Format user data, deleting all user data and replacing it with the default user data
## --------------------------------------------------------------------------------

INIT_PATH_LOC=$(pwd)

if [ "$(pwd)" = "/app" ]; then
  LOG_FILE_PATH="/app/app/logs/app_logs/system_logs.log"
  RESULTS_FILES_LOC="/app/app/system_data/"
  EXE_ENV_IS="Docker"
else
  LOG_FILE_PATH="$(pwd)/logs/app_logs/system_logs.log"
  RESULTS_FILES_LOC="system_data/"
  EXE_ENV_IS="Venv"
fi

# Log starting message
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.restore_user_files - INFO - Starting script." >> "$LOG_FILE_PATH"

# cd to system_data
cd "$RESULTS_FILES_LOC"
echo " current env is $EXE_ENV_IS"


# log start of script execution
echo "$now - scripts.restore_user_files - INFO - reformatting all user files with the default user input data" >> "$LOG_FILE_PATH"

# Copy all files from the source directory to the destination directory,
# overwriting any existing files with the same name
if [ -d "default_user_input_files" ]; then
    cp -fr default_user_input_files/*.csv user_input_files/
    cp -fr default_user_input_files/packing_results/* packing_results/
else
    # log error if default_user_input_files directory does not exist
    now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
    echo "error!!"
    echo "$now - scripts.restore_user_files - ERROR - default_user_input_files directory not found" >> "$LOG_FILE_PATH"
    exit 1
fi

cd "$INIT_PATH_LOC"
# log successful script execution
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.restore_user_files - INFO - successfully reformatted all user files" >> "$LOG_FILE_PATH"
