<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Granblue Bookkeeper</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="GBFBKcss.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"> </script>   
		<![endif]-->
	</head>
	<body> <div id="wrapper">
		<h1></h1>
		<nav> <ul>
			<li> <a href="index.php">	 	Home 		</a> </li>
			<li> <a href="prelim.php">		Prelims 	</a> </li>
			<li> <a href="bot_info.php"> 	Bot Info	</a> </li>
		</ul> </nav>
		<main>
		<p class="center">
			
				<?php
						include 'db-connect.php';
						
						$conn = new mysqli($servername, $username, $password, $dbname);
						echo "This is the list of cutoff scores for prelims <br>";
						if($conn->connect_error){
							die("connection failed: ". $conn->connect_error);
						}
						$sql = "SELECT * FROM Scores 
									WHERE Day_Number = 0 
									ORDER BY GW_Number DESC, Team_Name ASC";
						$result = $conn->query($sql);
						if($result->num_rows > 0){
							echo " <table style ='width:80%'>
								<tr>
									<th> GW Number </th>
									<th> Tier </th>
									<th> Cutoff </th>
									<th> Element </th>
								</tr>";
							while($row=$result->fetch_assoc()){
							echo " <tr>
										<td>".$row["GW_Number"]."</td>
										<td>".$row["Team_Name"]."</td>
										<td>".$row["Scores_Score"]."</td>
										<td>".$row["Element_type"]."</td>
								";		
							}
						}else{
							echo "no results here<br>";
						}
						?>
	</p>
		</main>
		
		<footer>
		<p>
		</p>
		</footer>
	</div> </body>
</html> 