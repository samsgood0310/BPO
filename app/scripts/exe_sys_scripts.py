#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ************************************************************************************
# This module execture bash scripts that triggered by the app
# ************************************************************************************
#

import os
import subprocess
from pathlib import Path
from app.logs.app_logger import Logger, ErrorHandler

logger = Logger(__name__)
log_and_handle_errors = ErrorHandler(logger)


@log_and_handle_errors
def run_bash_script(bash_script_name: str) -> None:
    """ This function is used for running bash scripts from the 'scripts' directory. """
    try:
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

        # Change the permission of the script file to make it executable
        script_path = Path(__file__).parent / f"{bash_script_name}.sh"
        logger.info(f'bash script was triggered: {script_path}')
        os.chmod(script_path, 0o755)

        # Check if the scripts directory has execute permission
        if not os.access(abs_path, os.X_OK):
            raise PermissionError(f"You do not have permission to execute files in {abs_path}")

        # Construct the full path to the bash script
        bash_script_path = os.path.join(abs_path, f"{bash_script_name}.sh")

        # Check if the bash script exists and has execute permission
        if not os.path.isfile(bash_script_path):
            raise FileNotFoundError(f"Could not find {bash_script_path}")
        if not os.access(bash_script_path, os.X_OK):
            raise PermissionError(f"You do not have permission to execute {bash_script_path}")

        # Set the file mode to 755 to make the script executable
        os.chmod(bash_script_path, 0o755)

        # Run the bash script using subprocess.call
        subprocess.call(bash_script_path, shell=True)
    except Exception as error:
        logger.error(message=f"function = run_bash_script error: {error}")
