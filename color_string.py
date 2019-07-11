import os
import sys
import subprocess
import glob
import zipfile

Color = {
        "BLACK"     : '\033[30m', 
        "RED"       : '\033[31m',
        "GREEN"     : '\033[32m',
        "YELLOW"    : '\033[33m',
        "BLUE"      : '\033[34m',
        "PURPLE"    : '\033[35m',
        "CYAN"      : '\033[36m',
        "WHITE"     : '\033[37m',
        "END"       : '\033[0m',
        "BOLD"      : '\038[1m',
        "UNDERLINE" : '\033[4m',
        "INVISIBLE" : '\033[08m',
        "REVERCE"   : '\033[07m'
        }
#print(Color.GREEN + "Green" + Color.END)
#print(Color.RED + "RED" + Color.END)

# 文字列に色をつける
def str_color(text, color):
    return Color[color] + text.ljust(16) + Color["END"]

# Trueなら緑色に、Falseなら赤色にする
def bool_color(f):
    if f == True:
        return str_color("True", "GREEN")
    else:
        return str_color("False", "RED")

# 一つも提出していなければ赤色に、提出していれば緑色にする
def count_color(n):
    if n == 0:
        return str_color(str(n), "RED")
    else:
        return str_color(str(n), "GREEN")

# 採点する
def check():
    output = subprocess.check_output(['python', 'sample.py'])
    print(output.decode('utf-8'))
