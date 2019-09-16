import base64
import os

while True:
    print("欢迎使用 python base64 加解密系统，请选择你想要进行的操作：")
    print("1：加密")
    print("2：解密")
    print("0：退出")
    option = input()
    if option == "1":
        s = input("请输入明文：")
        encodedStr = base64.b64encode(s.encode())
        print("加密后的密文为:", encodedStr.decode())
    elif option == "2":
        try:
            s = input("请输入密文：")
            encodedStr = base64.b64decode(s.encode())
            print("解密后的明文为:", encodedStr.decode())
        except:
            print("请输入正确的 base64 编码的密文！")
    elif option == "0":
        break
    else:
        print("您输入了错误的数字，请确保您输入了 0 ~ 2 之间的整数！")
    os.system("pause")
    clear = os.system("cls")