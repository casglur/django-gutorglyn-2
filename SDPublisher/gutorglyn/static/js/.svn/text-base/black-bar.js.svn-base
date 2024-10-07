/*globals $ document languageLabel createCookie location readCookie window gup*/
$(".language-switch").text(languageLabel);
$(".language-switch").click(function () {
	//console.log("language lable is " + languageLabel);
	if (languageLabel === "English") {
		createCookie('gutorglynlang', 'en-GB', 3650);
	} else {
		createCookie('gutorglynlang', 'cy-GB', 3650);
	}	
	location.reload();
});


var lang = readCookie('gutorglynlang');
if (lang === 'en-GB') {
    $('#poem-selection').load('/gutorglyn/dropdown-titles-en');
} else {
    $('#poem-selection').load('/gutorglyn/dropdown-titles-cy');
}

//Set value of dropdown text based on URL parameter
var desiredValue;
var currentURL = window.location.href;

$(document).ajaxComplete(function () {
    if (currentURL.indexOf("/poem/") > -1) {
        if (gup('poem-selection')) {
            desiredValue = gup('poem-selection');
        } else {
            desiredValue = readCookie('gutorglynpoem');
        }
        var titleElement = document.getElementById("poem-selection");
        for (var titleIndex = 0; titleIndex < titleElement.options.length; titleIndex++) {
            if (titleElement.options[titleIndex].value === desiredValue) { //change title menu index to match poem-selection
                titleElement.selectedIndex = titleIndex;
                break;
            }
        }
        var firstLineElement = document.getElementById("first-line");
        for (var firstLineIndex = 0; firstLineIndex < firstLineElement.options.length; firstLineIndex++) {
            if (firstLineElement.options[firstLineIndex].value === desiredValue) { //change first line menu index to match poem-selection
                firstLineElement.selectedIndex = firstLineIndex;
                break;
            }
        }
    }
});

