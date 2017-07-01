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
</div>

<!-- Container Model -->
<div id="model" class="bg-1">
<div class="container">
  <h3 class="text-center">Machine Learning Model</h3>
  <p class="text-center"><em>Microsoft Azure</em></p>
  <br>
  </div>
</div>
<!-- Container Test -->
<div id="test" class="container">
    <h3 class="text-center">TEST MODEL</h3>
    <p class="text-center">
        <form  id="uploadImage" action="" method="post" enctype="multipart/form-data">
			<input name="fileToUpload" type="file" onchange="previewFile()" style="display:none" id="input_photo">
			<br>
			<div id="upload_and_test">
				<label id="inputPhoto" for="input_photo">UPLOAD</label>  
				your image and 
				<button type="submit" class="button" name="submited" value="insert" id="btnTest">TEST</button>the model!
			</div>
		</form>
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
$(document).ready(function(e){
	$("#uploadImage").on('submit',function(e){
		e.preventDefault();
		$.ajax({
			url: "conn.php", 
			type: "POST",             
			data: new FormData(this), 
			contentType: false,       
			cache: false,             
			processData:false,        
			success: function(response)   
			{
				alert(response);
				if((response + '').length < 4)
					$("#result").html("There is a <b style='color:#000'>  "+ response +"  </b> on the picture.");
				else {
					$("#result").html("");
					alert(response);
				}
			}
		});
})});

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
   var preview = document.getElementById('petImage');
   var file    = document.querySelector('input[type=file]').files[0]; 
   var reader  = new FileReader();
   reader.onloadend = function () {
	   preview.src = reader.result;
   }
   if (file) {
	   reader.readAsDataURL(file); 
	   preview.style.height = '300px';
   } else {
	   preview.src = "";
   }
   
}
</script>
</body>
</html>

