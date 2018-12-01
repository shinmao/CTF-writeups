# BCTF 2018
https://ctftime.org/event/708  

## checkin
Category: Web  
Exploit:  
I have known that the website is based on the beego framework, but I try sql injection or command injection on the `gosessionid` and still find nothing.  
Here, what I need to know is to **LFI with sessionid**. If I can inject something such like `../`. It is possible for me to try including another uploaded session file, which contained serialized data such like `username: admin`!.  
[A famous example of CVE-2018-18925](https://github.com/vulhub/vulhub/tree/master/gogs/CVE-2018-18925)  
generate the session file with gob and include it, and when you direct to the path `/admin_panel`, you will find that you have privilege to the see the flag.

## SimpleVN
Category: Web  
Exploit: Code review and I have put the source code in same directory.  
There are two kinds of functionalities in the website:  
1. screenshot: I can use this to see the screenshot of the subpage of the website.  
2. upug: upload the pug template, but can only use alphanumeric and dot character.  
I have tried SQL injection for knex and SSTI on the functionality of upug in the competition, but SQL injection is rejected by the encryption of the website and I also not know how to leak the information I want with so limited character in `node.js`.  
So, here is my lack of knowledge about `node.js`. I already know that `FLAG_PATH` and `FLAGFILENAME` are both set to global environment variables. **I am able to use `process.env.FLAG_PATH` and `process.env.FLAGFILENAME` to leak the information of flag**. Now, screenshot should help me to get the content of the flag file. However, when I follow to the screenshot of flag file, the screenshot is not big enough to contain the flag part.  
Here comes another interesting knowledge: `Range: bytes=xxxx~xxxx` of http-header to specify where do you want to show of the file.
