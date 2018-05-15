 #!/usr/bin/php-cgi
<?php

if (isset($_GET['source']))
{
   show_source(__FILE__);
   exit();
}

$link = mysqli_connect('localhost', 'shellql', 'shellql', 'shellql');   // server, username, password, db

if (isset($_POST['shell']))
{
   if (strlen($_POST['shell']) <= 1000)
   {
      echo $_POST['shell'];
      shellme($_POST['shell']);
   }
   exit();
}



?>

<html>

<form action="index.php" method=POST>
shell <input type=text name=shell required><br>   
<input type=submit value="shell me">
</form>   

<a href="?source">debug me</a> <br>

</html>    