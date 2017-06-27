<!DOCTYPE html>
<html lang="en">
<head>
  <title>Cat or Dog</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>
<body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="50">

<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#myPage">Cat or Dog</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-left">
        <li><a href="#myPage">HOME</a></li>
		<li><a href="#description">DESCRIPTION</a></li>
		<li><a href="#model">MODEL</a></li>
        <li><a href="#test">TEST</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- Wrapper for image -->
<div class="carousel-inner">
  <div class="item active">
	<img src="images/animals-2222007_1920.jpg" alt="Cats and Dogs" width="1200" height="700">  
  </div>
</div>

<!-- Container Description-->
<div id="description" class="container text-center">
  <h3>CAT VS. DOG</h3>
  <p>It is easy for humans to determine whether images contain either a cat or a dog while computer find it a bit more difficult.</p>
  <br>
  <div class="row">
    <div class="col-sm-4">
      <p class="text-center"><strong>Human</strong></p><br>
      <img src="images/man.png" class="img-rounded person" alt="Human" width="255" height="255">
    </div>
    <div class="col-sm-4">
      <p class="text-center"><strong>Cat vs. Dog</strong></p><br>
      <img src="images/cat_dog.png" class="img-rounded person" alt="Cat vs. Dog" width="255" height="255">
    </div>
    <div class="col-sm-4">
      <p class="text-center"><strong>Computer</strong></p><br>
      <img src="images/computer.png" class="img-rounded person" alt="Computer" width="255" height="255">
    </div>
  </div>
</div>

<!-- Container Model -->
<div id="model" class="bg-1">
<div class="container">
  <h3 class="text-center">Machine Learning</h3>
  <p class="text-center"><em>Microsoft Azure</em></p>
  <br>
  </div>
</div>

<!-- Container Test -->
<div id="test" class="container">
    <h3 class="text-center">TEST MODEL</h3>
    <p class="text-center">
        <form  method="post" enctype="multipart/form-data">
		<label id="inputPhoto" for="input_photo"> UPLOAD </label>
		<input name="fileToUpload" type="file" onchange="previewFile()" style="display:none" id="input_photo">
        <button onclick=submit() type="submit" name="submited">Test</button>
        </form>
        <br>
		your image and test the model!
	</p>
	<div class="row">
	<div class="col-md-8">
		<img id="petImage" src=""  />
    </div>
    <div class="col-md-4">
		<div id="result"></div>
    </div>
  </div>
</div>

<!-- Footer -->
<footer class="text-center">
  <a class="up-arrow" href="#myPage" data-toggle="tooltip" title="TO TOP">
    <span class="glyphicon glyphicon-chevron-up"></span>
  </a><br><br>
</footer>



<script>
$(document).ready(function(){
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
        window.location.hash = hash;
      });
	}
  });
});

function previewFile(){
   var result  = document.getElementById('result'); 
   var preview = document.getElementById('petImage');
   var file    = document.querySelector('input[type=file]').files[0]; 
   var reader  = new FileReader();

   reader.onloadend = function () {
	   preview.src = reader.result;
   }

   if (file) {
	   reader.readAsDataURL(file); 
	   preview.style.height = '300px';
	   $('#result').html("There is a <b style='color:#000'>  DOG  </b> on the picture.");
   } else {
	   preview.src = "";
	   $('#result').html("");
   }
   
}

</script>
<?php
if(isset($_POST["submited"])){
$target_dir = "../catvsdog/uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
if(isset($_POST["submited"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
        $arg=basename($_FILES["fileToUpload"]["name"]);
        echo $arg;
        $results = shell_exec('py catvsdog.py ' . $arg);
        /*$cutresults= substr($results, 1, -2);
        $arrayresults=explode( '  ', $cutresults );
        $arr=array_filter($arrayresults, function($value) { return $value !== ''; });
        //$arr=array_map('floatval', $arr);
        array_unshift($arr, "");
        var_dump($arr);
        include 'conn.php';*/
        $results= substr($results, 1, -2);
        //var_dump($results);
        if($results=="0"){
            ?>  
            <h1>Pas je</h1>
            <?php
        }
        else{
             ?>  
            <h1>Mačka je</h1>
            <?php
        }
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
}

?>
</body>
</html>

