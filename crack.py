from unrar import rarfile
import sys

def crack_pwd():
    fp = rarfile.RarFile(rarFile)
    with open(passDic,'r',encoding='utf-8') as f:
        for str in f:
            str = str.strip()
            try:
                fp.extractall('result', pwd=str.encode('gbk').decode('cp437'))
                print('Success, password is:', str)
                break
            except Exception as e:
                print(e)

if __name__ == "__main__":
    try:
        rarFile = sys.argv[1]
        passDic = sys.argv[2]
        crack_pwd()
    except:
        print('Author: zR00t1')
        print('Usage: python crack.py encrypted.rar pass.txt')
        print('Tips: The code of pass.txt file must be UTF-8')