# Asis 2018 Writeups

## Buy flag
這題似乎是這次比賽裡最簡單的，我卻沒有做出來 :(  
首先是要**養成看request的習慣**，之前都懶惰沒有把burp開出來代理一下，可能做題會更有方向  
比賽時拿到js的代碼開始審計時就一直在找頁面上的注入點...
```js
$(document).ready(function() {
  $('#pay').click(function() {
    var coupon = btoa($('#coupon').val());  // encode string into base64
    var flags = ['fake1', 'fake2', 'asis'];
    var card = [];
    for (var i in flags) {
      if ($('#' + flags[i]).is(":checked")) {
        card.push({name:flags[i], count:1});  // 放進陣列
      }
    }
    $.ajax({
      type: 'POST',
      url :'/pay', 
      data: JSON.stringify({card: card, coupon: coupon}),
      contentType: 'application/json',
      success: function(result) {
        alert(result.result);      // you credit not enough
      }
    })
  });
})
```
以上是題目的js代碼，下面是payload：  
![buy-flag](https://github.com/shinmao/CTF-writeups/blob/master/Asis2018/screenshoot/buy-flag.png)  
`{"card":[{"name":"asis","count":1}],"coupon":""}`裡面可以修改的點只有count了，但是如果把count改0的話會出現必須大於0的警告。為了讓flag的credit降低為0，經過一番折騰終於找到了`NaN`，不被json所識別的東西，被轉成0給處理了！  

## Nice Code
這題第一關是找源碼，剛開始覺得實在太猜了，怎麼可以長在`/index.php/index.php`，賽後發現不斷發送request時`/admin/admin`的URL會不斷疊加，我想這大概就是提示吧:)  
接下來的源碼才是這題的重點：  
```php
<?php
include('oshit.php');
$g_s = ['admin','oloco'];
$__ni = $_POST['b'];
$_p = 1;
if(isset($_GET['source'])){
    highlight_file(__FILE__);
        exit;
}
if($__ni === $g_s & $__ni[0] != 'admin'){
    $__dgi = $_GET['x'];
    $__dfi = $_GET;
    foreach($__dfi as $_k_o => $_v){
        if($_k_o == $k_Jk){
            $f = 1;
        }
        if($f && strlen($__dgi)>17 && $_p == 3){
            $k_Jk($_v,$_k_o); //my shell :)
        }
        $_p++;
    }
}else{    
    echo "noob!";
}
```
在繞陣列的if時第一個scope就給卡住了，根據源碼要求，我們要給一個跟`$g_s`一樣的**順序和值都一樣**陣列，這就是強等於。這個好說：立馬給個`b[0]=admin&b[1]=oloco`的payload，可是這樣就無法滿足了第二個條件，於是就等到賽後的wp出來...  
原來是利用了php5.5.9舊版本的bug：在舊版本的library裡面，如果比較的型態為陣列，會將二者陣列的`key`值做相減並且存入一個`result`裡面。這下問題就來了，`key`相減後得到的值真的能存入`result`裡面嗎？相減後的值若大到必須要用64位元來存，這時`result`卻還是32位元的數，**integer overflow**就這樣發生了!  
這題第一個scope利用的正是這個bug，於是我在post中隨便構造了個32位元無法存的整數：`b[68719476736]=admin&b[1]=oloco`  
接下來的關卡就簡單多了，我們先不用管`$k_Jk`是什麼鬼，看到第二個scope：`strlen($__dgi)>17 && $_p==3`，`x`的要求是大於17個字的長度，要讓`$_p==3`我們要讓整個迴圈跑三次，也就是`$_GET`裡面要有三個參數。  
於是除了胡亂補上一個參數，剩下一個我就在裡面構造了shell  
這邊有個小問題，關於`$k_Jk`是在做啥我無從猜測，所以只能依照他的提示來試  
![](https://github.com/shinmao/CTF-writeups/blob/master/Asis2018/screenshoot/nice_code.png)  
好一個藏在`/var/flag`的`ASIS{f52c5a0cf980887bdac6ccaebac0e8428bfb8b83}`  
這邊我特別推薦這部教學影片 [Vlog #003: old PHP and array===array](https://www.youtube.com/watch?v=8fGigwN_E-U)  
以下是PHP的修補紀錄 [PHP #69892](https://bugs.php.net/bug.php?id=69892)

## Reference
* [Vlog #003: old PHP and array===array](https://www.youtube.com/watch?v=8fGigwN_E-U)  
* [PHP #69892](https://bugs.php.net/bug.php?id=69892)
