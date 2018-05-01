# Asis 2018 Writeups

## Buy flag
這題似乎是這次比賽裡最簡單的，我卻沒有做出來 :(  
首先是要養成看request的習慣，之前都懶惰沒有把burp開出來代理一下，可能做題會更有方向  
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
![buy-flag]()  

## Reference
