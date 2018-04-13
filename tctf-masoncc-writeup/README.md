# TCTF v2 
TCTF v2 is the CTF practice platform for MasonCC, and I have put up some web challenge on it. It is pity that I cannot keep all challenges running on server. Therefore, I would give my writeup of web challenge here. Welcome to take source code of challenges if you are interested in anyone.  
*  [Cover Peasy](#cover-peasy)  
*  [Giv mE a Creativ shell](#giv-me-a-creativ-shell)  
*  [PHP un-Siri ME](#php-un-siri-me)  
*  [Evil Config Writing](#evil-config-writing)  
*  [Unicorn && Lion](#unicorn-and-lion)  
*  [Shorter shell](#shorter-shell)  

## Cover Peasy
see source code in ./easypeasy.txt  
```php
<meta charset="utf-8">
<?php

error_reporting(0);
if (empty($_GET['str'])) {
    echo "see source code in ./easypeasy.txt";
    die();
}else{
    $flag = trim(file_get_contents('xxxxxxxxxxx.php'));
    $url = "www.1pwnch.org";
    $str = $_GET['str'];
    $pwnch = "enjoyIt";
    @parse_str($str);
    if ($url[0] != 'QNKCDZO' && md5($url[0]) == md5('QNKCDZO')) {
        extract($_GET);
        if($pwnch == $flag){
            echo "masoncc{xxxxxxxxxxx}";
        }else{
            echo "Good! But it's not enough!";
        }
    }else{
        exit('Try angain :-)');
    }
}
?>
```

## PHP un Siri ME

## Evil Config Writing

## Unicorn and Lion
This is a very classic challenge for Union-based mysql injection.  
I won't keep source code of file in this place.  
You need to find each answer of problem from the **faq.php**.  
What's worth paying attention to is that you need to separate each results of answer.  
Here is the trick ```group_concat(column name separator 'x')```  
that ```x``` can help you separate each results.

## Shorter shell
[Enjoy my writeup on my blog](https://shinmao.github.io/2018/02/20/A-tiny-shell/)

