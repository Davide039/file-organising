from os import listdir, chdir, mkdir
from os.path import join, splitext, isfile, exists
from shutil import move
from sys import argv

chdir(argv[1])
types = []

for file in listdir('.'):
	types.append(splitext(file)[1][1:])
types = list(set(types))

for filetype in types:
	if not exists(filetype):
		mkdir(filetype)

for file in listdir('.'):
	move(file, join('./', splitext(file)[1][1:])) if isfile(file) else ''

