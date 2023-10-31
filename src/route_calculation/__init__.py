"""
File description DOCString
"""


class ClassExample:
    """
    This class is an example to the route_calculation api
    """

    def __init__(self):
        """
        Init method definition
        """
        self.class_variable_example = 0

    def class_method_example(self, param_example: float | str | int) -> float | str | int:
        """
        Class method definition

        :param param_example: param
        :return: value
        """
        return self.class_variable_example + param_example


def public_method_example(param_example):
    """
    Public method definition

    :param param_example: param
    :return: value
    """
    return param_example


def _private_method_example(param_example):
    """
    Private method example

    :param param_example: param
    :return: value
    """
    return param_example
