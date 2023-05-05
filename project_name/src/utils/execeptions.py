"""Custom Exception Class"""

import sys


def error_message_details(error, error_detail: sys):
    """Generate Details of the Error Message

    Args:
        error (_type_): _description_
        error_detail (sys): _description_
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_meesage = f"Error Occured in python script:{file_name} in line number {exc_tb.tb_lineno} and the error_message is {str(error)}"
    return error_meesage


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error=error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
