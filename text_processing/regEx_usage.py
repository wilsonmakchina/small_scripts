# substitute ',' for '/' for my file

import re
import sys
file_name = sys.argv[1]
file = open(file_name) # read file
file2 = open(file_name + '_result.txt', 'w') # write file
for line in file.readlines():
	line = line.rstrip()
	line = re.sub('/', ',', line, count=0)
	print(line,file=file2)
file.close()
file2.close()
