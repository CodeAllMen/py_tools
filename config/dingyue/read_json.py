"""
Create by yy on 2019/9/23
"""


def read_json(file_name):
    with open(file_name, "rb") as f:
        data = f.read().decode("utf-8")
    return data
