# Riddle4 write up
## 链接 `https://console-nft.art/pro_4/`


首先打开网页是一段php代码
```
<\?php

function r() {
	$r = h('68747470733a2f2f636f6e736f6c652d6e66742e6172742f');
	$l = h('7374617277617273');
	echo $r . $l;
}
r;

function h($hex){
    $string='';
    for ($i=0; $i < strlen($hex)-1; $i+=2){
        $string .= chr(hexdec($hex[$i].$hex[$i+1]));
    }
    return $string;
}

?>
```

稍微修改运行一下
```php
<?php

function r() {
	$r = h('68747470733a2f2f636f6e736f6c652d6e66742e6172742f');
	$l = h('7374617277617273');
	echo $r . $l;
}
r();

function h($hex){
    $string='';
    for ($i=0; $i < strlen($hex)-1; $i+=2){
        $string .= chr(hexdec($hex[$i].$hex[$i+1]));
    }
    return $string;
}

?>
```

得到`https://console-nft.art/starwars`,打开显示

![disid](https://raw.githubusercontent.com/silentnoname/silent666pic/master/img/disid.jpg)
输入discord id后四位数字。

![I feel so weak](https://raw.githubusercontent.com/silentnoname/silent666pic/master/img/weakpass.jpg.jpg)

猜测可能要输入弱密码爆破，可以使用burpsuite或者写python脚本。

我使用burpsuite intruder模块爆破后得到密码是`323232`
![](https://raw.githubusercontent.com/silentnoname/silent666pic/master/img/burp.png)

输入密码后得到一个zip文件和一个wordlist，网页提示我们zip的密码是word1_word2，加密方式是AES256.
![](https://raw.githubusercontent.com/silentnoname/silent666pic/master/img/zippass.png)
构造python脚本

```python
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
```

注意要将wordlist和zip放在python脚本同一目录下。运行脚本，得到zip密码。解压后即可得到发送给console机器人的密码。