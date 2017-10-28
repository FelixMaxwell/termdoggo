import sys

if len(sys.argv) != 2:
	print("{} <ifile>".format(sys.argv[0]))

part = []
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		part += [line[:-1]]

print(part)
