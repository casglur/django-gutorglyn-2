/*globals $ document languageLabel createCookie location readCookie window gup alert console*/

var debugStatus = gup('debug');
var searchOptionOn = gup('search-option');
var RegExOn = gup('reg-ex');
var CaseOn = gup('match-case');
var diacriticOn = gup('ignore-diacritics');
var searchVal = gup('searchVal');

if (searchOptionOn === "reg-ex") {
    $('#poem-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&reg-ex=' + RegExOn + '&mode=poemsRegEx' + '&debug=' + debugStatus);

} else {
    $('#poem-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&reg-ex=' + RegExOn + '&mode=poems' + '&debug=' + debugStatus);

}

$('#paraphrase-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=paraphrases');
$('#trans-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=translations');
$('#exp-notes-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=explanatory_notes');
$('#text-notes-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=text_notes');
$('#sources-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=sources');
$('#names-results').load('/gutorglyn/search-results-v1/?searchVal=' + searchVal + '&search-option=' + searchOptionOn + '&page-start=0&match-case=' + CaseOn + '&ignore-diacritics=' + diacriticOn + '&mode=names');


if (searchOptionOn === "reg-ex") {
//    $('#reg-ex').prop('checked', true);

    //$('#search-results > div > ul > li:eq(0)').hide();    
    $('#search-results > div > ul > li:eq(1)').hide();  
    $('#search-results > div > ul > li:eq(2)').hide();  
    $('#search-results > div > ul > li:eq(3)').hide();        
    $('#search-results > div > ul > li:eq(4)').hide();      
    $('#search-results > div > ul > li:eq(5)').hide();
    $('#search-results > div > ul > li:eq(6)').hide();  
    
    //$('#search-results > div > div:eq(0)').hide();    
    $('#search-results > div > div:eq(1)').hide();      
    $('#search-results > div > div:eq(2)').hide();  
    $('#search-results > div > div:eq(3)').hide();        
    $('#search-results > div > div:eq(4)').hide();  
    $('#search-results > div > div:eq(5)').hide();
    $('#search-results > div > div:eq(6)').hide();
}

//if (CaseOn === 'on') {
//    $('#match-case').prop('checked', true);
//}
//    
//if (diacriticOn === 'on') {
//    $('#ignore-diacritics').prop('checked', true);
//}   

/* Code to hide empty search tabs  */

var exp_note_hits, name_hits, paraphrase_hits, poem_hits, text_note_hits, trans_hits, sources_hits;

exp_note_hits = parseInt($("#exp-note-hit-count").text(), 10) || 0;
name_hits = parseInt($("#name-hit-count").text(), 10) || 0;
paraphrase_hits = parseInt($("#paraphrase-hit-count").text(), 10) || 0;
poem_hits = parseInt($("#poem-hit-count").text(), 10) || 0;
text_note_hits = parseInt($("#text-note-hit-count").text(), 10) || 0;
trans_hits = parseInt($("#trans-hit-count").text(), 10) || 0;
sources_hits = parseInt($("#sources-hit-count").text(), 10) || 0;

var hit_array = [poem_hits, paraphrase_hits, trans_hits, exp_note_hits, text_note_hits, sources_hits, name_hits];
console.log("Hit Array is " + hit_array);



//Get the max value from the array    
var maxValue = Math.max.apply(this, hit_array);
console.log("highest result value is " + maxValue);

// Get the index of the max value, through the built in function inArray
var highest_position = $.inArray(maxValue, hit_array);
console.log("highest zeroth tab position is " + highest_position);

// Hide tabs that don't contain results

$("#search-tabs").tabs({ selected: highest_position });


/* Code to hide empty search tabs end */    

$("#accordion").accordion({
    collapsible: true,
    active: false
});

$(".instance-help-text").text($("#hidden-instance-tooltip-text").text());


$(document).ajaxStop(function () {
    $("#search-tabs > div > div > .results-group").each(function (index, elem) {
        if ($.trim($(elem).html()).length === 0) {
            console.log("hidden tab index is " + index);
            $("#search-tabs").tabs("disable", [index]);
        }
    });
});