#!usr/bin/python  
#-*- coding:utf-8 _*-

import xml.etree.ElementTree as et

etree = et.ElementTree()

stu = et.Element("Student1")

name = et.SubElement(stu, 'Name')
name.attrib = {'lang','en'}
name.text = 'maozedong'


age = et.SubElement(stu, 'Age')
age.text = 18

et.dump(stu)