def extractNumberFromString(string):
    return [int(s) for s in string.split() if s.isdigit()]
print(extractNumberFromString('ค.ศ. 2013</doc>'))

import re
s = 'ค.ศ. 2013</doc>'
print()
