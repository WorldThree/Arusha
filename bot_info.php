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
			The prefix to use this bot is !GW. So to use a command type "!GW `command`" <br>
			When a command requires user input it will be noted by a ` surrounding it. Do not include the ` <br>
			The commands are case sensitive, so type them as they are typed here. 
			<table style ='width:80%'>
				<tr>
					<th> Command </th>
					<th> Output </th>
				</tr>
				<tr>
					<td> scores 						</td>
					<td> Retrieves the latest scores for each team 	</td>
				</tr>
				<tr>
					<td> north  							</td>
					<td> Retrieves the latest 4 scores for North and gives the mean change 	</td>
				</tr>
				<tr>
					<td> south  							</td>
					<td> Retrieves the latest 4 scores for South and gives the mean change 	</td>
				</tr>
				<tr>
					<td> east  							</td>
					<td> Retrieves the latest 4 scores for East and gives the mean change 	</td>
				</tr>
				<tr>
					<td> west  							</td>
					<td> Retrieves the latest 4 scores for West and gives the mean change 	</td>
				</tr>
				<tr>
					<td> prelim 							</td>
					<td> Displays the prelim cutoffs for the GW 	</td>
				</tr>
				<tr>
					<td> means 							</td>
					<td> Displays mean change in score for the past 4 scores of each team 	</td>
				</tr>
				<tr>
					<td> submit `north` `west` `east` `south`			</td>
					<td> Enters each of he scores into the database  	</td>
				</tr>
				<tr>
					<td> submit_prelim `A cutoff` `B cutoff  `C cutoff`							</td>
					<td> Changes the element when submitting Prelim and daily scores. 	</td>
				</tr>
				<tr>
					<td> set_day `day`						</td>
					<td> Changes the day to submit and look at scores 	</td>
				</tr>
				<tr>
					<td> set_ele `element`  							</td>
					<td> Changes the element when submitting Prelim and daily scores. 	</td>
				</tr>
				<tr>
					<td> set_GW `GW number`  							</td>
					<td> Changes the GW used to submit and retreive scores. 	</td>
				</tr>
	</p>
		</main>
		
		<footer>
		<p>
		</p>
		</footer>
	</div> </body>
</html> 