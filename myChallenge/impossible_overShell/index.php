<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
  <title>1pwnch dashboard</title>
</head>
<body class="p-3 mb-2 bg-dark text-white">

<div class="container">
  <h1>Please upload your file</h1>
  <p>Welcome Admin!</p>
  <p>Hint: Extend what you learn today!</p>
</div>

<form action="up.php" method="post" enctype="multipart/form-data">
  <div class="form-group">
    <label>File:</label>
    <input type="file" class="form-control" name="file" id="file"  placeholder="Upload your pwnch">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

<div class="container">
  <h2>This hint is not available until you try uploading file...</h2>
  <p>-rw-r--r-- 1 www-data staff   20 Apr 11 15:52 hello.php</p>
  <p>-rw-r--r-- 1 root     root  1458 Apr 11 06:08 index.php</p>
  <p>-rw-r--r-- 1 root     root   998 Apr 11 15:50 up.php</p>
</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>

</body>
</html>
