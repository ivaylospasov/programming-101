#!/usr/bin/env python3


def reduce_file_path(path):
    path_parts = []
    path = path.split('/')
    for index, part in enumerate(path):
        if not (path[index] == "" or path[index] == "."):
            path_parts.append(path[index])
    for index, part in enumerate(path_parts):
        if path_parts[index] == '..':
            del path_parts[(index - 1)]
    for index, part in enumerate(path_parts):
        if path_parts[index] == '..':
            del path_parts[index]
    for index, parts in reversed(list(enumerate(path_parts))):
        path_parts.insert(index, '/')
    new_path = ''.join(path_parts)
    return new_path


def main():
    print(reduce_file_path("/home//radorado/code/../tasks/./hackbulgaria/week0/../"))

if __name__ == '__main__':
    main()
