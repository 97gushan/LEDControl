<?php	

	$status = exec("sudo -u root python /home/pi/lEDControl/python/relayStatus.py");
	echo "$status";
	
?>
