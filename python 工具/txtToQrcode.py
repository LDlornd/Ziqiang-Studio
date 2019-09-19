import qrcode
import os

def txtToQrcode():
    try:
        f = open(s + ".txt")
    except:
        print("您输入的文件不存在，请检查文件路径或文件名是否正确")
    else:
        jpg = qrcode.make(f.read())
        jpg.save(s + ".jpg")
        print("二维码生成成功！")
        f.close()

def main():
    while True:
        os.system("cls")
        print("欢迎使用 python 二维码生成系统，本系统可将 txt 文件转换为二维码，请选择您要进行的操作：")
        print("欢迎使用 python 二维码生成系统，本系统可将 txt 文件转换为二维码，请输入文件名（不带后缀），或者输入 0 以退出系统：")
        print("注意：若使您想直接输入文件名，而不带上路径的话，您需要将文件放在程序运行目录下")
        try:
            s = input()
        except:
            print("请输入正确的文件名或者 0 !")
        else:
            if s == "0":
                break
            else:
                txtToQrcode()
        os.system("pause")

if __name__ == "__main__":
    main()