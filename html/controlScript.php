<?php	


	exec("sudo -u root python /home/pi/LEDControl/python/relayScript.py");
	$status = exec("sudo -u root python /home/pi/LEDControl/python/relayStatus.py");
	
	echo $status;

?>
