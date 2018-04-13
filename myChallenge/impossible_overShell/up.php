<?php

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
