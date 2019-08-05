# SSRFme
It was embarrassing that I always got the result liked:  
```
{"code": 200, "data": "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final/"}
```
when I used `http://0.0.0.0/flag.txt` in `urllib.urlopen()`.  

Finally, I found the reason.  
```
urllib.urlopen("http://139.180.128.86/flag.txt").read()
```
would return with
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n
```

I couldn't use `file://` but I could use `urllib.urlopen("flag.txt")` directly and got the flag.
