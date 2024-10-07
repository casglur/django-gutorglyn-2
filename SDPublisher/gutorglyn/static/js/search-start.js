/*globals $ document languageLabel createCookie location readCookie window gup alert console*/

$("#ignore-diacritics").prop("checked", true);

$("#reg-ex").click(function () {
    $("#match-case").prop("checked", !$("#match-case").prop("checked", false));
    $("#match-case").prop("disabled", !$("#match-case").prop("disabled"));
    
    $("#ignore-diacritics").prop("checked", !$("#ignore-diacritics").prop("checked"));
    $("#ignore-diacritics").prop("disabled", !$("#ignore-diacritics").prop("disabled"));
});  

$("#ignore-diacritics").click(function () {
    if ($("#match-case").is(':checked')) {
        $("#match-case").prop("checked", false);
    } else {
        $("#match-case").prop("checked", true);
    }
});  

$("#match-case").click(function () {
    if ($("#ignore-diacritics").is(':checked')) {
        $("#ignore-diacritics").prop("checked", false);
    } else {
        $("#ignore-diacritics").prop("checked", true);
    }
}); 

/* Code to select search option based on cookie */

var searchOptionValue;
if (readCookie('search_option')) {
    searchOptionValue = readCookie('search_option');
} else {
    searchOptionValue = "ignore-diacritics";
}

var searchSelectElement = document.getElementById("search-option-selection");
for (var searchSelectIndex = 0; searchSelectIndex < searchSelectElement.options.length; searchSelectIndex++) {
    if (searchSelectElement.options[searchSelectIndex].value === searchOptionValue) { //change title menu index to match poem-selection
        searchSelectElement.selectedIndex = searchSelectIndex;
        break;
    }
}

/* Code to select search option based on cookie end */