#!/bin/bash

## --------------------------------------------------------------------------------
## Purpose: deleting all csv files under system_data/packing_results
##
## Set the path to the log file
## When the script runs from the docker container, it runs from /, so the log file will be //logs/app_logs/system_logs.log
## which is not a valid path.
## --------------------------------------------------------------------------------

if [ "$(pwd)" = "/app" ]; then
  LOG_FILE_PATH="/app/app/logs/app_logs/system_logs.log"
  RESULTS_FILES_LOC="/app/app/system_data/packing_results"
  EXE_ENV_IS="Docker"
else
  LOG_FILE_PATH="$(pwd)/logs/app_logs/system_logs.log"
  RESULTS_FILES_LOC="system_data/packing_results"
  EXE_ENV_IS="Venv"
fi

SCRIPT_NAME="delete_last_packing_results"


# Log starting message
now=$(date +"%Y-%m-%d %H:%M:%S,%3N")
echo "$now - scripts.$SCRIPT_NAME - INFO - Starting script." >> "$LOG_FILE_PATH"

# Delete old csv packing_results
if [ -d "$RESULTS_FILES_LOC" ]; then
  rm -rf "$RESULTS_FILES_LOC"/*.csv
else
  # Log error if packing_results directory does not exist
  echo "error!!"
  echo "$now -  scripts.$SCRIPT_NAME - ERROR - system_data/packing_results directory not found"
  echo "Running method: $EXE_ENV_IS and PWD is: $pwd. ls is $ls"
  echo "$now -  scripts.$SCRIPT_NAME - ERROR - system_data/packing_results directory not found" >> "$LOG_FILE_PATH"
  exit 1
fi

# Log successful script execution
echo "$now - scripts.$SCRIPT_NAME - INFO - files were deleted" >> "$LOG_FILE_PATH"
