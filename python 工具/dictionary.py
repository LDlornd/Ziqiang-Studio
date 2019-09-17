import json
import re
import os

dictionary = {}
reverseDictionary = {}
tip = "输入格式为 \"key\" + 空格 + : + 空格 + \"value\" + ,，如 \" \"a\" : \"b\", \""

print("欢迎使用 python 字典反转系统，请输入您的原始字典：")
print("注意：" + tip)
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == '{': continue
    elif s == '}': break
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
os.system("pause")

'''
{
"a" : "1",
"b" : "1",
}
'''