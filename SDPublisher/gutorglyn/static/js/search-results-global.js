/*globals $ document languageLabel createCookie location readCookie window gup alert console*/


var currentPage = "{{ pageNumber }}";
currentPage = parseInt(currentPage, 10);
var ignoreDiacritics = gup('ignore-diacritics');
var matchCase = gup('match-case');
var pageNumberValues = "{{ pageNumberValues }}";
var resultsEnd = "{{ pageEnd }}";
resultsEnd = parseInt(resultsEnd, 10);
var resultsStart = "{{ pageStart }}";
resultsStart = parseInt(resultsStart, 10);
var regEx = gup('reg-ex');
var searchVal = gup('searchVal');
var totalPages = pageNumberValues.length;
var totalPages = totalPages - 2;
var totalResults = "{{ searchNum }}";
totalResults = parseInt(totalResults, 10);


var nextPageStart = pageNumberValues[currentPage];    

if (nextPageStart > totalResults) {
    $('.{{ searchMode }}-next-page-link').hide();
    $('.{{ searchMode }}-next-page-link').removeAttr('onClick');
    $('.{{ searchMode }}-last-page-link').hide();
    $('.{{ searchMode }}-last-page-link').removeAttr('onClick');
}

var previousPageStart = pageNumberValues[currentPage - 2];

if (currentPage <= 1) {
    $('.{{ searchMode }}-previous-page-link').hide();
    $('.{{ searchMode }}-previous-page-link').removeAttr('onClick');
}

if (currentPage <= 1) {
    $('.{{ searchMode }}-first-page-link').hide();
    $('.{{ searchMode }}-first-page-link').removeAttr('onClick');
    $('.{{ searchMode }}-previous-page-link').hide();
    $('.{{ searchMode }}-previous-page-link').removeAttr('onClick');
}

var pageStart = readCookie('{{ searchMode }}_page_start');

createCookie('explanatory_notes_page_start', pageStart);
createCookie('patrons_page_start', pageStart);
createCookie('paraphrases_page_start', pageStart);
createCookie('poems_page_start', pageStart);
createCookie('texts_page_start', pageStart);
createCookie('translations_page_start', pageStart);
createCookie('sources_page_start', pageStart);  

var resultsPerPage = 10;
var lastPageIndex = parseInt(resultsPerPage, 10) * totalPages;    

console.log('{{ searchMode }} page number values: ' + pageNumberValues);
console.log('{{ searchMode }} current page: ' + currentPage);
console.log('{{ searchMode }} next page start value: ' + nextPageStart);
console.log('{{ searchMode }} previous page start value: ' + previousPageStart);
console.log('{{ searchMode }} last page number value: ' + lastPageIndex);
console.log('{{ searchMode }} total pages: ' + totalPages);

function {{ searchMode }}GetFirstPage() {    
    $("#{{ searchMode }}-search-results-container").hide();
    $("#{{ searchMode }}-results-wait").show();

    $.get("gutorglyn/search-results-v1/?searchVal=" + searchVal
            + "&ignore-diacritics=" + ignoreDiacritics + "&match-case="
            + matchCase + "&reg-ex=" + regEx + "&per-page=" + resultsPerPage
            + "&page-start=" + 0  + "&mode={{ searchMode }}", function(data) {
        $("#{{ searchMode }}-search-results-container").replaceWith(data);
        $("#{{ searchMode }}-results-wait").hide();
    });
}

function {{ searchMode }}GetLastPage() {    
    $("#{{ searchMode }}-search-results-container").hide();
    $("#{{ searchMode }}-results-wait").show();

    $.get("gutorglyn/search-results-v1/?searchVal=" + searchVal
            + "&ignore-diacritics=" + ignoreDiacritics + "&match-case="
            + matchCase + "&reg-ex=" + regEx + "&per-page=" + resultsPerPage
            + "&page-start=" + lastPageIndex + "&mode={{ searchMode }}", function(data) {
        $("#{{ searchMode }}-search-results-container").replaceWith(data);
        $("#{{ searchMode }}-results-wait").hide();
    });
}

function {{ searchMode }}GetPreviousPage() {    
    $("#{{ searchMode }}-search-results-container").hide();
    $("#{{ searchMode }}-results-wait").show();

    $.get("gutorglyn/search-results-v1/?searchVal=" + searchVal
            + "&ignore-diacritics=" + ignoreDiacritics + "&match-case="
            + matchCase + "&reg-ex=" + regEx + "&per-page=" + resultsPerPage
            + "&page-start=" + previousPageStart + "&mode={{ searchMode }}", function(data) {
        $("#{{ searchMode }}-search-results-container").replaceWith(data);
        $("#{{ searchMode }}-results-wait").hide();
    });
}

function {{ searchMode }}GetNextPage() {    
    $("#{{ searchMode }}-search-results-container").hide();     
    $("#{{ searchMode }}-results-wait").show();
    
    $.get("gutorglyn/search-results-v1/?searchVal=" + searchVal
            + "&ignore-diacritics=" + ignoreDiacritics + "&match-case="
            + matchCase + "&reg-ex=" + regEx + "&per-page=" + resultsPerPage
            + "&page-start=" + nextPageStart + "&mode={{ searchMode }}", function(data) {
        $("#{{ searchMode }}-search-results-container").replaceWith(data);
        $("#{{ searchMode }}-results-wait").hide();             
    });
}

/* code to highlight found search terms  */
var terms = decodeURI(searchVal);
terms = terms.replace("+", " ", 'g');
var regExGlobalFlag = 'g';
var regExCaseFlag = 'i';
if (gup('match-case') === 'on') {
    var regExCaseFlag = '';
    var regExGlobalFlag = '';
}
var regExJS = new RegExp(terms, regExGlobalFlag + regExCaseFlag);
console.log(terms);
console.log(regExJS);
$('.search-results-line').each(function() { 
    $(this).html($(this).html().replace(regExJS, "<span class='found'>$&</span>"));
    $(".found").parents(".search-results-line").css("color", "#222222");        
    });
$('p').each(function() { 
    $(this).html($(this).html().replace(regExJS, "<span class='found'>$&</span>"));
    }); 

/* code to highlight found search terms End */