import json
import re
import os
import sys

dictionary = {}
reverseDictionary = {}
tip = "非大括号行的输入格式为 \"key\" + 空格 + : + 空格 + \"value\" + ,，如 \" \"a\" : \"b\", \""

def dictionaryReverse():
    dictionary.clear()
    reverseDictionary.clear()
    print("请输入您的原始字典：")
    print("建议您第一行输入左大括号，最后一行输入右大括号")
    print("注意：" + tip)
    while True:
        try:
            s = input()
        except:
            break
        if s == "{": continue
        elif s == "}": break
        else:
            if re.match("\".+\"\\s:\\s\".+\",", s) == None:
                print("请注意您的输入格式" + tip)
            else: 
                key, val = s.split(" : ")
                key = key[1 : len(key) - 1]
                val = val[1 : len(val) - 2]
                dictionary[key] = val
    for i in dictionary:
        if reverseDictionary.get(dictionary[i]):
            reverseDictionary[dictionary[i]].append(i)
        else:
            reverseDictionary[dictionary[i]] = [i]
    for i in reverseDictionary:
        if len(reverseDictionary[i]) == 1:
            reverseDictionary[i] = reverseDictionary[i][0]
    print(json.dumps(reverseDictionary, indent = 4))

def inputERROR():
    print("请确保您的输入为 0 或 1")

def main():
    while True:
        os.system("cls")
        print("欢迎使用 python 字典反转系统，请选择您要进行的操作：")
        print("1: 反转字典")
        print("0: 退出")
        try:
            option = input()
        except:
            inputERROR()
        else:
            if option == "0":
                break
            elif option != "1":
                inputERROR()
            else:
                dictionaryReverse()
        os.system("pause")

if __name__ == "__main__":
    main()

'''
{
"a" : "1",
"b" : "1",
}
'''