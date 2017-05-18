#coding=utf-8
from sys import argv

script, filename = argv #将列表参数赋值给filename

print "We're going to erase %r." % filename #我们将抹去这个文件
print "If you don't want that, hit CTRL-C (^C)." #如果你不想这样，按Ctrl+c（命令行中Ctrl+c是停止运行）
print "If you do want that, hit RETURN." #如果你想继续下去就按return（回车）

raw_input("?") #提示内容是？

print "Opening the file..." #(打开这个文件)
target = open(filename,'w') #（文件打开内容赋值给 tatget）

print "Truncating the file. Goodbye!" #截断这个文件
target.truncate() #清空这个target这个值得内容

print "Now I'm going to ask you for three lines" #现在我们问你三行

line1 = raw_input("line 1:") #第一行值固执给line1 提示你
line2 = raw_input("line 2:") #第二行值固执给line2
line3 = raw_input("line 3:") #第三行值固执给line3

print "I'm going to write these to the file." #我们将三行写进文件

target.write(line1) #将line1这个值写入target这个值内
target.write("\n")  #将空格写入target这个值中
target.write(line2) #将line1这个值写入target这个值内
target.write("\n") #将空格写入target这个值中
target.write(line3) #将line1这个值写入target这个值内
target.write("\n")#将空格写入target这个值中

print "And finally, we close it."
target.close() #关闭target这个值
