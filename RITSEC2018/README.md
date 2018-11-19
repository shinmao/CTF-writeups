# RITSEC2018
https://ctftime.org/event/682  

## Space Forces(100)
Category: Web  
Exploit: Simple `or ''` SQL injection  
Flag: `RITSEC{hey_there_h4v3_s0me_point$_3ny2Lx}`  

## The Tangled Web(200)
Category: Web  
Exploit: Use `dirsearch` to find interesting link and base64 decode the string  
Flag: `RITSEC{AR3_Y0U_F3371NG_1T_N0W_MR_KR4B5?!}`  

## Crazy Train(250)
Category: Web  
Exploit: After making sure that the post can not be xss, open the burpsuite then find the hidden input field. Following `article[title]` and `article[text]`, there is also a field of `article[a]`.  
![]()  
My browser extension showed that the site might be based on the rails, so let's try some SSTI of ruby on rails and it success. Therefore, I start making some code injection to find the place of the flag. First, I use `Dir.pwd` to get the currently path name which is `/blog`. Second, I use `Dir.entries('/blog')` then find there is `flag.txt`. The last step, just like I read the file `/etc/passwd`, I use `File.open('/blog/flag.txt').read` to get the flag.  
Flag: `RITSEC{W0wzers_who_new_3x3cuting_c0de_to_debug_was_@_bad_idea}`

