#!/usr/bin/env python
from pwn import *

host = "csie.ctf.tw"
port = 10133
r.remote(host,port)

flag = 0x600ba0

r.interactive()
