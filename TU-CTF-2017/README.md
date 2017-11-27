### Vuln chat  
For vuln chat, I got confused at first because I cannot overwrite the return address because **%30s limit of scanf**.  
However, we can overwrite the second format string of scanf.  
So, we just need to change the %30s to bigger one then we can overwrite the return address!  
  
### Vuln chat 2.0  
I think this is a very simple program.  
I don't need to overwrite the whole address, but 2 bytes are enough!!  

### Guestbook  
[My friend Kaibro's writeup](https://github.com/w181496/CTF/tree/master/tuctf-2017)  
[Other's writeup](https://aufarg.github.io/tuctf-2017-guestbook-250.html)  
For guestbook, I didn't successfully make it because I didn't care for the crash on argument in program.  
I would like to recommend with my friend's writeup and another one found on other's blog.  
They all explain the details of the program.
