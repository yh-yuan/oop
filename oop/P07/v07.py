#!usr/bin/python  
#-*- coding:utf-8 _*-

import json

student={
    "name":"luidana",
    "age":18,
    "mobile":"1557885040"
}

print(type(student))

stu_json=json.dumps(student)
print(type(stu_json))

print("json对象：{0}".format(stu_json))
stu_dict=json.loads(stu_json)

print(type(stu_dict))
print(stu_dict)