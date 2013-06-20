RobotFramework-DataGeneratorLibrary
===================================

Library to generate data by pattern


Strings
===================================

*Generate random string by pattern:*

Examples:
| ${string} | Get Random String By Pattern | ddd*10d-c*2ccc-d*2-cc*2-w-w*5ww |

Description:
- d - digit
- c - char
- w - word, digits and chars
- * - produce preceding char multiple times


Data and time 
===================================
*Get formatted time:*

Return current date and time in your format according
- *format* defined in http://docs.python.org/2/library/time.html#time.strftime .
- *offset* (optional) define in format [+-]<number>[mhdw]
--   m - minutes
--   h - hours
--   d - days
--   w - weeks

Example:
| ${necessary_time} | Get Formatted Time | "%Y-%m-%dT%H:%M:%SZ | +40w |
