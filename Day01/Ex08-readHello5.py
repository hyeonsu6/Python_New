'''
파일명 : Ex08-readHello5.py
'''
import sys
with open('./Python_New/Day01/hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list)