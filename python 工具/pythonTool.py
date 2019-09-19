import cryption
import dictionary
import txtToQrcode
import os

def inputERROR():
    print("您输入了错误的数据，请确保您输入的数据为 0 ~ 3 之间的整数！")
    os.system("pause")

def main():
    while True:
        os.system("cls")
        print("欢迎使用有 lornd 倾心制作的 Python 小工具，请选择您要使用的工具：")
        print("1：字符串 base64 加解密工具")
        print("2：字典反转工具")
        print("3：文本转化为二维码工具")
        print("0：退出")
        try:
            option = input()
        except:
            inputERROR()
        else:
            if option == "1":
                cryption.main()
            elif option == "2":
                dictionary.main()
            elif option == "3":
                txtToQrcode.main()
            elif option == "0":
                break
            else:
                inputERROR()

if __name__ == "__main__":
    main()