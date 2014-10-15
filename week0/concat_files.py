#!/usr/bin/env python3

from sys import argv

all_content = []

for index in range(1, len(list(enumerate(argv)))):
    file = open(argv[index])
    content = file.read()
    all_content.append(content)
    file.close()

# Add new line after the last string
all_content[-1] = all_content[-1] + '\n'

content_for_append = '\n\n'.join(all_content)

file = open('megatron.txt', 'a')
file.write(content_for_append)
file.write('\n')
file.close()


def main():
    pass

if __name__ == '__main__':
    main()
