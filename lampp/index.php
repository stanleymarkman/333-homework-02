<!DOCTYPE HTML>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="application/x-www-form-urlencoded"/>
<title>MusicAppDB</title>

<link rel="stylesheet" href="styles.css">
</head>

<body>
	<?php
	$conn = new mysqli("localhost", "root", "", "music-db");

	//Try to connect to server
	if ($conn->connect_error) {
	  die("Connection failed: " . $conn->connect_error);
	}

	//User registration
	if(isset($_REQUEST["submit"])){
	  // Variables for the output and the web form below.
	  $registration_out = "";
	  $s_user = $_REQUEST['username'];
	  $s_pass = $_REQUEST['password'];

		//Try and get the user with that username
		$sql_query = "SELECT 1 FROM users WHERE username = ('$s_user')";
		$result = mysqli_query($conn, $sql_query);
		$userrow = mysqli_fetch_assoc($result);


	  //Check that user/pass aren't empty, and user doesn't exist
	  if(!empty($s_user) && !empty($s_pass) && empty($userrow)){

			$sql_query = "INSERT INTO users (username, password) VALUES ('$s_user', '$s_pass')";
			$result = mysqli_query($conn, $sql_query);
			if($result){
				$registration_out = "User ". $s_user . " successfully created!";
			}
			else{
				$registration_out = "An unknown database error occurred.";
			}

	  }
	  else {
	    $registration_out = "Error- Username invalid! <br>Either username or password are empty<br> or user already exists.";
	  }
	}

	if(isset($_REQUEST["submitsong"])){
			  $songs_out = "";

			  $s_user = $_REQUEST['raterusername'];

				$sql_query = "SELECT * FROM ratings WHERE username = ('$s_user')";
				$result = mysqli_query($conn, $sql_query);
				//$songrow = mysqli_fetch_assoc($result);
				while ($songrow = mysqli_fetch_assoc($result)) {
    			$songs_out .= $songrow["song"] . ": " . $songrow["rating"] . "<br>";
				}

	}

	$conn->close();
	?>
	<div class="forms">
	<h1> Registration </h1>
	<form method="POST" action="">
	<input type="text" name="username" placeholder="New Username" /><br>
	<input type="text" name="password" placeholder="New Password" /><br>
	<input type="submit" name="submit" value="Submit"/>
	<p><?php
	  if(!empty($registration_out)){
	    echo $registration_out;
	  }
	?></p>
	</form>

	<h1> Retrieve Songs </h1>
	<form method="POST" action="">
	<input type="text" name="raterusername" placeholder="Rater Username" /><br>
	<input type="submit" name="submitsong" value="Submit"/>

	<p><?php
	  if(!empty($songs_out)){
	    echo $songs_out;
	  }
	?></p>
	</form>
	</div>

	</body>
</html>
