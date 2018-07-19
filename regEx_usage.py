import re
file = open('bp_go_enrichment.txt') # read file
file2 = open('result.txt', 'w') # write file
for line in file.readlines():
	line = line.rstrip()
	line = re.sub('/', ',', line, count=0)
	print(line,file=file2)
file.close()
file2.close()