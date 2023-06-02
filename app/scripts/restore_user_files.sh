#!/bin/bash

## --------------------------------------------------------------------------------
## Format user data, deleting all user data and replacing it with the default user data
## --------------------------------------------------------------------------------


# Set the path to the log file
if [ "$(pwd)" = "/" ]; then
  LOG_FILE_PATH="/app/logs/app_logs/system_logs.log"
  APP_DATA_PATH="/app/system_data/"
else
  LOG_FILE_PATH="$(pwd)/logs/app_logs/system_logs.log"
  APP_DATA_PATH="system_data/"
fi

# Log starting message
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.restore_user_files - INFO - Starting script." >> "$LOG_FILE_PATH"

# cd to system_data
cd "$APP_DATA_PATH"

# log start of script execution
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.restore_user_files - INFO - reformatting all user files with the default user input data" >> $LOG_FILE_PATH

# Copy all files from the source directory to the destination directory,
# overwriting any existing files with the same name
if [ -d "default_user_input_files" ]; then
    cp -fr default_user_input_files/*.csv user_input_files/
    cp -fr default_user_input_files/packing_results/* packing_results/
else
    # log error if default_user_input_files directory does not exist
    now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
    echo "error!!"
    echo "$now -  scripts.restore_user_files - ERROR - default_user_input_files directory not found" >> $LOG_FILE_PATH
    exit 1
fi


# log successful script execution
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.restore_user_files - INFO - successfully reformatted all user files" >> $LOG_FILE_PATH