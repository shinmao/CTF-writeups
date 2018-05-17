# Defcon 2018
這是我第一次打defcon的初賽，雖然web的水準還是很高，但是感覺多了些出壞的題目:sweat:

# sbva
這題的web page在用官方給的帳密登入後，會跳出`Incompatible browser detected.`的畫面。  
看到這個之後我就開始試`user-agent`的爆破了，但比賽時我卻漏掉很重要的一點，那就是提示...  
response:  
```php
<html>
    <style scoped>
        h1 {color:red;}
        p {color:blue;} 
    </style>
    <video id="v" autoplay> </video>
    <script>
        if (navigator.battery.charging) {
            console.log("Device is charging.")
        }
    </script>
</html>
```
我居然一股腦兒得在做爆破卻不理會這個提示  
賽後我才知道這是一個`navigator.battery`的API，在以前一些版本的瀏覽器有作支援，知道這個線索後再做爆破，這題就秒解了...

# PHP Eval White-List
這道題目的頁面是在說，他們做了很厲害的`eval`白名單，除了extension，他們還有開啟`open_basedir`來避免我們去執行別的目錄下的`flag`。  
看到這邊我就起手研究如何繞過`open_basedir`囉～  
首先看看目錄下的檔案：  
```php
// eval()
echo `ls`;
```
網頁根目錄下有這些檔案：  
```
bootstrap.min.css
index.php
source.php
source.txt
tmp/
websec_eval_wl.so
```
再來是看看我們只能**訪問**哪個目錄：  
```php
echo ini_get('open_basedir')
```
回傳得到的是`/var/www/html`  
好，為啥說這道題目不太U呢，其實我最後根本沒試著繞過`open_basedir`，我最後在瞎試`echo exec('../flag')`時就成功了！  
這題的flag就是`OOO{Fortunately_php_has_some_rock_solid_defense_in_depth_mecanisms,_so-everything_is_fine.}`  

# exzendtential-crisis
這題我在透過LFI拿到源碼後就卡住了，有線索知道用username為`sarte`的使用者登入就有權限看到flag，但是有太多疑惑了...  
1. 漏洞在哪兒？看起來很像`sqlinj`，但是哪一種sql會影響到怎麼bypass  
2. 有些未知的function，像是`login.php`裡的`check_credentials`，我只有看到呼叫，沒有看到內容的src，可以推測內容就在他給的extension裡，可是我跟逆向不合啊:sweat:  
賽後再看過我朋友的wp後了解了一下思路：  
透過`php.ini`找一下`mydb.so`的位置，並且用LFI把它載下來  
逆向後會發現引擎是`sqlite`和`sarte`被加密過的帳密  
接下來更是pwn的範疇，做了個overflow  

# Feedback
蠻多人覺得這次題目出壞了，以我個人的角度而言，這次的比賽的確放了太多需要猜測以及暴力破解的題目。不過這次比賽卻激發出我新的想法：原來web和其他領域可以結合成這麼有創意的題目，也因此我這次做題目上總是很快就不知如何下手....  
