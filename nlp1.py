import os


def call():
    print(os.getcwd())


def data():
    text_file = open("text-data/data.txt",'r')
    print(text_file.read())
data()