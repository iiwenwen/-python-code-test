#coding=utf-8
from sys import argv
from os. path import exists #使用 exists这个函数

scipt, from_file, to_file = argv # 脚本，变量from_file（源文件），变量to_file新文件

print "Copying from %s to %s" % (from_file, to_file) #打印“复制从from到to”

# we could do these two on one line, how?

in_file = open(from_file) #将from_file文件打开并将内容赋值给in_file
indata = in_file.read() #将in_file的内容读取并赋值给indata

print "The input file is %d bytes long" % len(indata) #打印“这个输入文件是几个字节长，len计算indata的字节”

print "Does the output file exist? %r" % exists(to_file) # 这个输出文件存在吗？exists命令将文件名字符串作为参数
print "Ready, hit RETURN to continue,CTRL-C to abort." #准备好，回车继续，Ctrl-C中断
raw_input() #输入回车

out_file = open(to_file,'w') #将新文件打开并将内容赋值给out_file
out_file.write(indata) #将indata的内容写入out_file

print "Alrigt, all done." #好了，所有的

out_file.close() #关闭out_file文件
in_file.close() #关闭in_file文件
