"""
Logging and Error classes :)
"""
import functools
import inspect
import logging
import os


class Logger:
    """
    This class creates a logger with the specified 'name' and initializes different logging handlers based on the
    'log_mode' parameter. It sets the logging level to 'INFO' by default. You can then use the logging methods to
    log messages with different severity levels.

    Usage example:
    >>> logger = Logger('my_logger')
    >>> logger.info('Informational message.')
    >>> logger.warning('Warning message.')
    >>> logger.error('Error message.')

    If an error occurs during execution, it will be logged with a custom error message that includes the module, the
    function name, and the line number, along with the error message.

    To specify a different log level, pass the level as a parameter to the logging method as shown in the example
    below:
    >>> logger.debug('Debugging message.')
     This class creates a logger with the specified 'name' and sets the logging level to 'INFO'. It also creates a
     'FileHandler' that writes log messages to a file called 'log.txt' and sets the formatting for the log messages.

     You can use this class by creating an instance of it and calling the info method to log a message:
     (e.g., 'debug', 'warning', 'error') or to use different logging handlers (e.g., 'StreamHandler', 'SMTPHandler').

     module_name = inspect.stack()[0][0].f_globals['__name__']
     function name = inspect.stack()[0][3]
     line_number = inspect.stack()[1][2]
     arg_names = inspect.getfullargspec(function_name).args
     arg_values = locals().copy()
     arg_values.pop('self', None)
     arg_values = {arg: arg_values[arg] for arg in arg_names}

     except Exception as e:
         logger.error(f"{module_name}:{inspect.stack()[0][3]}() function failed at line {line_number}: {e}")

    """
    def __init__(self, name, log_mode="app"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        logs_relative_path = "./logs/app_logs"

        current_path = os.getcwd()
        if current_path == "/":
            logs_relative_path = "./app/logs/app_logs"
        if log_mode == "app":
            handler = logging.FileHandler(f'{logs_relative_path}/all_logs.log')
        elif log_mode == "system":
            handler = logging.FileHandler(f'{logs_relative_path}/system_logs.log')
        elif log_mode == "user":
            handler = logging.FileHandler(f'{logs_relative_path}/user_logs.log')

        else:
            raise ValueError(f"Invalid logging mode '{log_mode}' selected.")
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(handler)

    def custom_error_message(self, message):

        module_name = inspect.stack()[1][1]
        try:
            function_name = inspect.stack()[1][3]
        except Exception as e:
            function_name = f'Not function {e}'

        line_number = inspect.stack()[1][2]

        error_message = f"{module_name}:{function_name}() failed at line {line_number}: {message}"
        self.logger.error(error_message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        def error_message_format(error_message):
            return f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!        THE BELOW ERROR CASED THE APP TO FAIL        !!!!!!!!!!!
{error_message}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

        print(error_message_format(message))
        return -1

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)


class ErrorHandler:
    """
    this class is used as function wraps in other modules.
    this class adds logs and try and except, similar to use the following function in the module.
    def log_and_handle_errors(func, logger):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f'function {func.__name__} was used with {args} and {kwargs} as parameters')
                return result
            except Exception as e:
                logger.error(e)
                raise
        return wrapper
    """
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                # prevent some functions to print there args, instead print there types
                if func.__name__ in ['3d_solution_figure', 'adjust_the_figure', 'save_locally_pickle_file']:
                    self.logger.info(f"""
                    function {func.__name__} and used with args types {[type(arg) for arg in args]} and {kwargs} as 
                    parameters""")
                else:
                    self.logger.info(f'function {func.__name__} was used with {args} and {kwargs} as parameters')

                return result
            except Exception as e:
                self.logger.error(e)
                raise e

        return wrapper
