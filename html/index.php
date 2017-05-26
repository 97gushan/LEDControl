<DOCTYPE html>

<html>

	<head>
		<title>You should not be here</title>
		
		<meta charset="utf-8"/>
		<meta name="viewport" content="width=device-width 
									height=device-height 
									initial-scale=1.0"/>

		
	
	</head>
	
	<body style="background: #222222;">
		<form>

			<input type='button' id='ON' value='Turn ON' onclick='_send.click();' 
						style='
						height: 100%;
						width: 100%;
						font-size: 32px;
						color: #3d3d3d;
						background-color: #4CAF50;
						border: none;
						display: none;
						text-align: center;
						text-decoration: none;'/>
			
			<input type='button' id='OFF'  value='Turn OFF' onclick='_send.click();' 						style='
						height: 100%;
						width: 100%;
						font-size: 32px;
						color: #3d3d3d;
						background-color: #ff3232;
						border: none;
						display: none;
						text-align: center;
						text-decoration: none;'/>
			
		</form>
		
		<script src="js/jquery.js"></script>
		<script src="js/main.js"></script>
	</body>
</html>
