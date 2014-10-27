import requests
import json


def hack_request():
    return requests.get('https://hackbulgaria.com/api/students/',
                        verify=False)


def hack_data():
    return hack_request().json()


def get_courses():
    courses_names = []
    for student in hack_data():
        for course in range(len(student['courses'])):
            courses_names.append(student['courses'][course]['name'])
    courses = set(courses_names)
    return list(courses)


def participation():
    participation = []
    for student in hack_data():
        for course in range(len(student['courses'])):
            if student['available'] is True:
                participation.append([
                                     student['name'],
                                     student['courses'][course]['name'],
                                     student['courses'][course]['group']
                                     ])
    return participation


if __name__ == '__main__':
    print(get_courses())
    print(participation())
