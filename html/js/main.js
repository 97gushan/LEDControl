var _send = {

	 click : function(){
		
		var status = "";
		
		// Activate the relay and update the ON/OFF button 
		$.get("/controlScript.php", "", function(data){
			status = data;
			
			if(status == "ON"){
				document.getElementById("ON").style.display = "none";
				document.getElementById("OFF").style.display = "inline";
			}else{
				document.getElementById("ON").style.display = "inline";
				document.getElementById("OFF").style.display = "none";
			}
		});	
	
	}

};

// When the page has fully loaded, activate the correct ON/OFF button
// Depending on the status of the relay
$(document).ready(function(){
	var status = "";
		
	$.get("/statusScript.php", "", function(data){
		status = data;
		
		if(status == "ON"){
			document.getElementById("ON").style.display = "none";
			document.getElementById("OFF").style.display = "inline";
		}else{
			document.getElementById("ON").style.display = "inline";
			document.getElementById("OFF").style.display = "none";
		}
	});
	
});
