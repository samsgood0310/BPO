"""
**************************************************************
****              ABOUT COMPONENTS DIRECTORY              ****
**************************************************************
This Directory hold all dash components that the app use.
"""

##
try:
    from logs.app_logger import ErrorHandler, Logger
except ImportError:
    from app.logs.app_logger import ErrorHandler, Logger
