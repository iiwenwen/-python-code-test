#coding=utf-8
from sys import argv
script, filename = argv #脚本名，文件名
txt = open(filename) #将该文件打开并将内容赋值给txt
print "Here's your file %r:" % filename #打印
print txt.read() #读取txt中的内容
print "Type the filename again:" #再次输入文件命
file_aganin = raw_input(">") #将是输入的值赋值给file_aganin，并用>提示
txt_again = open(file_aganin) #打开file_aganin中的文件内容，并赋值给txt-again
print txt_again.read() #打印txt_again中的内容并打印下来
