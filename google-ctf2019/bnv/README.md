## bnv
The source (`post.js`) is very easy to understand. It would send json format to `/api/search` and get response.  
![](https://github.com/shinmao/CTF-writeups/blob/master/google-ctf2019/bnv/json.png)
I figure it out as a challenge for XXE very soon. Take a look at the following part of source:  
```js
if (xhr.getResponseHeader('Content-Type') == "application/json; charset=utf-8") 
...
else {
    document.getElementById('database-data').value = xhr.responseText;
}
```
It still would return the result. So, how if Content-Type isn't json? Before the world of json, most of the data is transmitted by XML on internet. Therefore, I try to send POST with XML again, and it works!! Following is the story of XXE.  
![](https://github.com/shinmao/CTF-writeups/blob/master/google-ctf2019/bnv/no_result_1.png)
I declare the entity and try to get the content of sensitive file; however, it only return with the message of `No result found`. It seems that it would return user-defined message when an existing file content is leaked by XXE! Then, I can only try the error-based XXE. Spending a while on constructing the payload, I leaked the content of `/etc/passwd` from error message.  
![](https://github.com/shinmao/CTF-writeups/blob/master/google-ctf2019/bnv/pwd.png)
For my payload, it's an attacking chain from 1 ~ 3. After I call `PWD` to dynamically declare the entities of `file` and `eval`:  
1. I call `eval` to dynamically declare the entity of `error`.  
2. I call `error`. It tries to load the resource but end up with invalid URI, then the parameter entity in the error message would also be showed.  

> This is why we use it as parameter entity. We want to call it in another entity which is also in DTD.  

Now we just need to change the path to `file://flag`
![](https://github.com/shinmao/CTF-writeups/blob/master/google-ctf2019/bnv/got_damn_flag.png)
GAME OVER ~ `CTF{0x1033_75008_1004x0}` !!
