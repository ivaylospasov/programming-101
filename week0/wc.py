#!/usr/bin/env python3

from sys import argv
from re import sub

script, command, filename = argv

file = open(filename, 'r')
content = file.read()

if command == 'lines':
    lines_list = content.split('\n')
    print(len(lines_list))

if command == 'words':
    no_points = sub('\.', ' ', content)
    no_new_lines = sub('\n', '', no_points)
    words_only = []
    words_and_spaces = no_new_lines.split(' ')
    for index, word in enumerate(words_and_spaces):
        if len(word) != 0:
            words_only.append(word)
    print(len(words_only))

if command == 'chars':
    count_chars = 0
    no_points = content.split('.')
    no_points_string = ' '.join(no_points)
    for char in no_points_string:
        count_chars += 1
    print(count_chars)

file.close()
