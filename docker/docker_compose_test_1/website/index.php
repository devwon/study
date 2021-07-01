<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>My Restaurant</title>
</head>
<body>
	<h1>Welcome to my restaurant</h1>
	<h2>Menu</h2>
	<ul>
		<?php
			$json = file_get_contents('http://product-service');
			$obj = json_decode($json);

			$menu = $obj -> menu;
			foreach ($menu as $food) {
				echo "<li>$food</li>";
			}
		?>
	</ul>
</body>
</html>