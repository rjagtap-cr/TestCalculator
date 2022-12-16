import json
import os
import random
import requests


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("Dict saved in file")


class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
        self.credits = 0

    def get_age(self):
        return self.age

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits


class Student2:

    def __init__(self, name, age, branch, _credits):
        self.name = name
        self.age = age
        self.branch = branch
        self._credits = _credits

    def get_age(self):
        return self.age

    def get_credits(self):
        return self._credits


def get_topper(students):
    return max(students, key=lambda student: student.get_credits())


def is_eligible_for_degree(student):
    return student.get_credits() > 30


def roll_dice():
    print("Rolling...")
    return random.randint(1, 6)


def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You WON"
    else:
        return "You LOST"


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']
