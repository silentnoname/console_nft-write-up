import pyzipper
import multiprocessing
import functools

def getpass():
    filename = 'wordlist.txt'
    passw = []
    with open(filename, 'r') as file:
        key=file.read().split( )

    for i in range(0, len(key)):
        for j in range(0,len(key)):
            passw.append(key[i]+"_"+key[j])
    return  passw

def hack(a,passw):
    with pyzipper.AESZipFile('8303.zip', 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as f:
        f.pwd = passw[a].encode('utf-8')
        try:
            f.extractall()
            print("\t密码是:" + passw[a])
        except Exception:
            pass


def main():
    passw=getpass()
    pool = multiprocessing.Pool(8) #数字为cpu核心数
    hackp=functools.partial(hack,passw=passw)
    pool.map(hackp, range(0, len(passw)) )
    pool.close()
    pool.join()



if __name__ == "__main__":
    main()


