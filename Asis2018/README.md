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

## Reference
