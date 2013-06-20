import re
from datetime import datetime, timedelta
import unittest


class _DateTimeGeneration(object):

    def get_formatted_time(self, format=r"%Y-%m-%dT%H:%M:%SZ", offset="+0d"):
        """Return current date and time in your format according
        - *format* defined in http://docs.python.org/2/library/time.html#time.strftime .
        - *offset* (optional) define in format [+-]<number>[mhdw]
        --   m - minutes
        --   h - hours
        --   d - days
        --   w - weeks

        Example:
        | ${necessary_time} | Get Formatted Time | | |
        | ${necessary_time} | Get Formatted Time | %H:%M:%SZ | |
        | ${necessary_time} | Get Formatted Time | %H:%M:%SZ | -1d |
        | ${necessary_time} | Get Formatted Time | %Y-%m-%dT | +1h |
        | ${necessary_time} | Get Formatted Time | %Y-%m-%dT | +360m |
        | ${necessary_time} | Get Formatted Time | "%Y-%m-%dT%H:%M:%SZ | +40w |
        """

        format, offset = format.strip(), offset.strip()

        delta_format = {
            "d": "days",
            "m": "minutes",
            "h": "hours",
            "w": "weeks"
        }

        operator, offset, offset_type = re.findall(
            r'^([\+\-])?(\d+)?(\w)?$', offset)[0]

        if not (format and operator and offset and offset_type):
            operator, offset, offset_type = "+", "0", "d"

        # todo: add error handling
        time = eval("%s %s timedelta(%s=%s)"
                    % ("datetime.today()",
                        operator,
                        delta_format[offset_type],
                        offset))

        return time.strftime(format)


class TestDateTimeGeneration(unittest.TestCase):
    # todo: add more sophisticated test cases to check right format

    def test_get_formated_time(self):
        self.assertIsInstance(_DateTimeGeneration().get_formatted_time(), str)

    def test_get_time_with_format(self):
        self.assertIsInstance(
            _DateTimeGeneration().get_formatted_time(r'%H:%M:%SZ'), str)

    def test_get_time_with_format_and_offset(self):
        self.assertIsInstance(
            _DateTimeGeneration().get_formatted_time(r'%H:%M:%SZ', ' +40w'), str)


if __name__ == '__main__':
    unittest.main()
