#!/usr/bin/python3

"""
演示如何操作python命令行参数
"""

import sys  # 导入sys模块，使用sys.argv获取命令行参数
import getopt  # 导入getopt模块，使用getopt解析命令行参数

print('参数个数:', len(sys.argv))
print('参数列表:', str(sys.argv))

# 使用getopt模块解析命令行参数
opts, args = getopt.getopt(sys.argv[1:], "n:u:")

print('opts:', opts)
print('args:', args)
