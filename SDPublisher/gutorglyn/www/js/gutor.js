/*globals document */
/* Cookie Code */

function createCookie(name, value, days) {
	var expires = "";
	if (days) {
		var date = new Date();
		date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		expires = "; expires=" + date.toGMTString();
	}
	document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) === ' ') {
			c = c.substring(1, c.length);
		}
		if (c.indexOf(nameEQ) === 0) {
			return c.substring(nameEQ.length, c.length);
		}
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name, "", -1);
}

/* Cookie Code End */

/* code to set cookies and language switch  */	

createCookie('gutorglynlines', 'off');
//console.log(document.cookie);

function languageStatus() {
	var currentLang = readCookie("gutorglynlang");
	if (currentLang) {
		return currentLang;
	} else {
		return 'cym';
	}
	
}

var languageLabel = (languageStatus() === 'eng') ? 'Cymraeg' : 'English';

/* code to set cookies and language switch end */	

/* Code for name pop up */

function popUp(URL) {
	var day = new Date();
	var id = day.getTime();
	eval("page" + id + " = window.open(URL, '" + id + "', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=1,width=400,height=180');");
}
/* Code for name pop up end*/
