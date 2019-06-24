## bnv
The source (`post.js`) is very easy to understand. It would send json format to `/api/search` and get response.  

I figure it out as a challenge for XXE very soon.  
```js
if (xhr.getResponseHeader('Content-Type') == "application/json; charset=utf-8") 
...
else {
    document.getElementById('database-data').value = xhr.responseText;
}
```
It still would return the result. So, how if Content-Type isn't json? Before the world of json, most of the data is transmitted by XML on internet. Therefore, I try to send POST with XML again, and it works!! Following is the story of XXE.  
