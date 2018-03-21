#!/usr/bin/python
# Filename: 20180321_main.py

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
    
#运行20180321_main.py文件，输出的是This program is being run by itself。
#调用import 20180321_main.py 输出的则是 I am being imported from another module
