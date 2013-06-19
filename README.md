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
