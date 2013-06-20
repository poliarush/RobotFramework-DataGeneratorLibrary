__version__ = '1.0'
__author__ = 'Mykhailo Poliarush'

from strings import _StringDataGeneration
from date import _DateTimeGeneration


class DataGeneratorLibrary(_StringDataGeneration, _DateTimeGeneration):

    """
    Data Generator Library intended to generate data by pattern upon situation
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
