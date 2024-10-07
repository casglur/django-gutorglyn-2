/*globals $ document getText readCookie createCookie showLineLinks window*/

/* load remote content into div to populate pop up onClick */

function loadContent(elementSelector, sourceUrl) {
	$("" + elementSelector + "").load(
			"/static/sandbox/names/" + sourceUrl + "");
}	

/* load remote content into div to populate pop up onClick end */

/* Code to Lock Scroll Bars */

function lockScrollBars() {
    $("#edited-text").scroll(function () { 
        $("#paraphrase-tab").scrollTop($("#edited-text").scrollTop());
        $("#paraphrase-tab").scrollLeft($("#edited-text").scrollLeft());        
        $("#translation-tab").scrollTop($("#edited-text").scrollTop());
        $("#translation-tab").scrollLeft($("#edited-text").scrollLeft());
    });

    $("#paraphrase-tab").scroll(function () { 
        $("#edited-text").scrollTop($("#paraphrase-tab").scrollTop());
        $("#edited-text").scrollLeft($("#paraphrase-tab").scrollLeft());
    });

    $("#translation-tab").scroll(function () { 
        $("#edited-text").scrollTop($("#translation-tab").scrollTop());
        $("#edited-text").scrollLeft($("#translation-tab").scrollLeft());

    }); 

}

/* Code to Lock Scroll Bars end */
	

//Start of jQuery code
//
$(document).ready(function () {
/*
 * Set Text labels 
 */
	$("#search-for").html(getText("search for label"));	
	$("#search-button").attr("value", getText("search button label"));
	$(".show-menu").html(getText("show options button label"));
	$("#home-link").html(getText("home link"));
	$("#poems-link").html(getText("poems link"));
	$("#patrons-poets-link").html(getText("patrons and poets link"));
	$("#people-places-link").html(getText("people and places link"));
	$("#top-guidelines-link").html(getText("top guidelines link"));
	$("#title-list-link").html(getText("title list link"));
	$("#patron-list-link").html(getText("patron list link"));
	$(".play-audio").html(getText("play audio button label"));
	$(".pause-audio").html(getText("pause audio button label"));
	$(".show-hide-vlines").html(getText("show line numbers button label"));
	$(".show-names").html(getText("show name links button label"));
	$("#Activechk").button({ label : getText("unlock texts button label")});
	$("#paraphrase-tab-label").html(getText("paraphrase tab label"));
	$("#notes-tab-label").html(getText("notes tab label"));
	$("#manuscripts-tab-label").html(getText("manuscripts tab label"));
	$("#variants-tab-label").html(getText("variants tab label"));
	$("#explanatory-tab-label").html(getText("explanatory tab label"));
	$("#textual-tab-label").html(getText("textual tab label"));
	$("#sources-tab-label").html(getText("sources tab label"));
	$("#transcripts-tab-label").html(getText("transcripts tab label"));
	$("#images-tab-label").html(getText("images tab label"));
	$("#stemma-tab-label").html(getText("stemma tab label"));
	$("#open-stema").html(getText("show stemma button label"));
	$("#patrons-and-poets-draw-title").html(getText("patrons and poets draw title"));
	$("#abbreviations-draw-title").html(getText("abbreviations draw title"));

/*
 * Set Text labels End
 */
	if (window.location.href.indexOf("/gutorglyn/poem/") === -1) {
	    $(".show-menu").css('display', 'none');
	}

	$('.abbrev-panel-content').load('/static/abbreviations/guto-abbreviations2.htm');
		
	$(".slide-menu").css('display', 'none');
	
	$(".show-menu").toggle(function () {
		$(".slide-menu").css('display', 'normal');
		$(".slide-menu").slideDown();
		$(this).html(getText("hide options button label"));
	}, function () {
		$(".slide-menu").slideUp();
		$(this).html(getText("show options button label"));
	});
	

					
	if ($.browser.msie) {
		$("#audio").css("display", "none");
		$("#player").css("display", "normal");
	} else {
		$("#audio").css("display", "normal");
		$("#player").css("display", "none");
	}


	$("#edited-text > div > span > .name").css('text-decoration', 'none');
	
	$('#trigger').click(function () {
	    $('#link-content').toggle();
	});
	
	$('#trigger1').click(function () {
	    $('#link-content').toggle();
	});	
	

/* Start of panel content toggle code */	
// choose text for the show/hide link - can contain HTML (e.g. an image)
	var showText = 'Show';
	var hideText = 'Hide';
 
// initialise the visibility check
	var is_visible = false;
 
// append show/hide links to the element directly preceding the element with a class of "toggle"
	$('.toggle').prev().append(' (<a href="#" class="toggleLink">' + showText + '</a>)');
 
// hide all of the elements with a class of 'toggle'
	$('.toggle').hide();
 
// capture clicks on the toggle links
	$('a.toggleLink').click(function () {
 
// switch visibility
		is_visible = !is_visible;
 
// change the link depending on whether the element is shown or hidden
		$(this).html((!is_visible) ? showText : hideText);
 
// toggle the display - uncomment the next line for a basic "accordion" style
//$('.toggle').hide();$('a.toggleLink').html(showText);
		$(this).parent().next('.toggle').toggle('slow');
 
// return false so any link destination is not followed
		return false;
		 
	});
	
/* End of panel content toggle code */		


/* code to toggle visibility of variant line links on edited text */	

	$(".show-hide-vlines").toggle(function () {
			var linesState = readCookie('gutorglynlines');
			if (linesState === 'off') {
				createCookie('gutorglynlines', 'on');
				$(".variant-line-link-hide").css('visibility', 'visible');
				$(".variant-line-link-hide").css('font-weight', 'bold');
				
				$(".variant-line-link-show").css('color', '#000');
				$(".variant-line-link-show").css('font-weight', 'bold');
				$(".variant-line-link-show").css('text-decoration', 'underline');
				
				$(this).button("option", "label", getText("hide line numbers button label"));	
			
			} else { 
				createCookie('gutorglynlines', 'off');
				$(".variant-line-link-hide").css('visibility', 'hidden');
				
				$(".variant-line-link-show").css('font-weight', 'normal');
				$(".variant-line-link-show").css('color', '#8B7D6B');
				$(".variant-line-link-show").css('text-decoration', 'none');
				
				$(this).button("option", "label", getText("show line numbers button label"));
			}	
		}, function () {
			var linesState = readCookie('gutorglynlines');
			if (linesState === 'on') {
				createCookie('gutorglynlines', 'off');
				$(".variant-line-link-hide").css('visibility', 'hidden');
				
				$(".variant-line-link-show").css('font-weight', 'normal');
				$(".variant-line-link-show").css('color', '#8B7D6B');
				$(".variant-line-link-show").css('text-decoration', 'none');
				
				$(this).button("option", "label", getText("show line numbers button label"));	
			} else {
				createCookie('gutorglynlines', 'on');
				$(".variant-line-link-hide").css('visibility', 'visible');
				$(".variant-line-link-hide").css('font-weight', 'bold');
				
				$(".variant-line-link-show").css('color', '#000');
				$(".variant-line-link-show").css('font-weight', 'bold');
				$(".variant-line-link-show").css('text-decoration', 'underline');
				
				$(this).button("option", "label", getText("hide line numbers button label"));
			}
		});


/* code to toggle visibility of variant line links on edited text */

/* code to toggle visibility of name links on edited text */	

	$(".show-names").toggle(function () {
		$("#edited-text > div > span > .name").css('text-decoration', 'underline');
		$(this).button("option", "label", getText("hide name links button label"));
		$(".variant-line-link-hide").css('font-weight', 'bold');
	}, function () {
			$("#edited-text > div > span > .name").css('text-decoration', 'none');
			$(this).button("option", "label", getText("show name links button label"));
		});


/* code to toggle visibility of name links on edited text */

/* lock scrollbars on page load */

	lockScrollBars();

/* lock scrollbars on page load end */

/* code to change state of sync button state when clicked and sync contents of 2 columns*/
    
    var $activechk = $("#Activechk");
    $activechk.button({ icons : { primary: 'ui-icon-locked' } });

    $activechk.click(function (event) {
		var element = this;
		if (this.checked) {
			$(this).button("option", "icons", {
				primary : 'ui-icon-locked'
			});
			$(this).button({
				label : getText("unlock texts button label")
			});
			lockScrollBars();
		} else {
			$(this).button("option", "icons", {
				primary : 'ui-icon-unlocked'
			});
			$(this).button({
				label : getText("lock texts button label")
			});
			$("#edited-text").unbind();
			$("#paraphrase-tab").unbind();
			$("#translation-tab").unbind();
		}
    });

 
/* code to change state of sync button state when clicked and sync contents of 2 columns end */

/* code to turn links into buttons */
    
    $('.show-hide-vlines').button();
    $('.show-names').button();
    
/* code to turn links into buttons end */

/* code for tabs */
  

    $("#tabs").tabs();

/* code for tabs  end */

/* code to show variant line links if variant lines tab is selected */

	$('#tabs').tabs({
	    select: function (event, ui) {
	        var theSelectedTab = ui.index;
	        if (theSelectedTab === 4) {
	            showLineLinks();
	            createCookie('gutorglynlines', 'on');
	        }
	    }
	});

/* code to show variant line links if variant lines tab is selected end */

/* code to select manuscript sources tab from hyperlink */

	$(".manuscript-tab-call").click(function () {
		$("#tabs").tabs('select', '#transcriptions-tab');
	});

/* code to select manuscript sources tab from hyperlink end */

/* change contents of transcription tab based on dropdown menu selection */

	$("#transcription-select").live("change keyup", function () {
	    var id = $(this).prop('selectedIndex');
	    var transName = $('#transcription-select')[0].options[id].value; 
	    var selectedTab = $("#transcriptions-tab").tabs().tabs("option", "selected");
	    var href = $("#tabs a").get(selectedTab);
	    var poemID = $('#poemID').val();
	    var url = "/gutorglyn/transcripts/";
	    var newUrl = url + "?transcript=" + transName + "&poem=" + poemID + "&index=" + id;
	    $("#transcriptions-tab").tabs().tabs("url", selectedTab, newUrl);
	    $("#transcriptions-tab").tabs().tabs("load", selectedTab);   
	
	});	

/* change contents of transcription tab based on dropdown menu selection end */

/* change contents of transcription Images tab based on dropdown menu selection */

	$("#transcription-images-select").live("change keyup", function () {
	    var id = $('#transcription-images-select').prop('selectedIndex');
	    var transName = $('#transcription-images-select')[0].options[id].value; 
	    var selectedTab = $("#transcriptions-tab").tabs().tabs("option", "selected");
	    var href = $("#tabs a").get(selectedTab);
	    var poemID = $('#poemID').val();
	    var url = "/gutorglyn/transcriptimages/";
	    var newUrl = url + "?transcript=" + transName + "&poem=" + poemID + "&index=" + id;
	    $("#transcriptions-tab").tabs().tabs("url", selectedTab, newUrl);
	    $("#transcriptions-tab").tabs().tabs("load", selectedTab);   
	
	});	

/* change contents of transcription Images tab based on dropdown menu selection end */

/* select notes tab on load unless other value is hashed in the URL */
	if (document.location.hash !== '') {
		// get the index from URL hash
		var tabSelect = '';
		tabSelect = document.location.hash.substr(1,
				document.location.hash.length);
		$("#tabs").tabs('select', tabSelect - 1);
	} else {
		$("#tabs").tabs('select', '#notes-tab');
	}

/*select notes tab on load unless other value is hashed in the URL end */

/* code for tabs within tabs */

	$("#notes-tab").tabs();
	
	$("#transcriptions-tab").tabs();

/* code for tabs within tabs */

/* code for left flyout 'draws' */

	$(".trigger").click(function () {
			$(".panel").toggle("slow");
			$(this).toggleClass("active");
			return false;
		});
	
	$(".trigger2").click(function () {
		$(".panel2").toggle("slow");
		$(this).toggleClass("active");
		return false;
	});

/* code for left flyout 'draws' end */
            
/* code to autosubmit poem dropdown */

	$("#poem").live("change keyup", function () {
					//var location = '';
					//location.href = location.href.replace(location.hash, '') + '&x=y' + location.hash;
	                $("#poem-select").submit();
	            });	

/* code to autosubmit poem dropdown end */

/* code to autosubmit first-line dropdown */
	$("#first-line").live("change keyup", function () {
		var firstLine = document.getElementById("first-line");
		var poemNum = document.getElementById("poem");
		var lineChoice = firstLine.options[firstLine.selectedIndex].value;
		for (var i = 0; i < poemNum.options.length; i++) {
			if (poemNum.options[i].value === lineChoice) { //change .value to .text to match on text value
			    poemNum.selectedIndex = i;
			    break;
			}
		}
	    $("#poem-select").submit();
	});	

/* code to autosubmit first-line dropdown end */

/* code to style icon hover state */

	$('#dialog_link, ul#icons li').hover(function () {
		$(this).addClass('ui-state-hover');
	}, function () {
		$(this).removeClass('ui-state-hover');
	});

/* code to style icon hover state end */

/* code for stema image dialog box */
	$("#stema-dialog").dialog({
		autoOpen: false
	});

	$("#open-stema").click(function () {
		$("#stema-dialog").dialog("open");
		return false;
	});
/* code for stema image dialog box End*/

/* Code to Send Poem Number and line Number to Variant Lines Tab */

	$("#variant-lines-tab").load('/gutorglyn/variant-lines/?p=001&l=1');

	$(".variant-line-link-show").click(function () {
		var poemLine = $(this).attr('href');
		poemLine = poemLine.split(",");
		var poem = poemLine[0];
		var line = poemLine[1];
		$("#variant-lines-tab").load('/gutorglyn/variant-lines/?p=' + poem + '&l=' + line);
		$("#tabs").tabs('select', 4);
		return false;	
	});	

	$(".variant-line-link-hide").click(function () {
		var poemLine = $(this).attr('href');
		poemLine = poemLine.split(",");
		var poem = poemLine[0];
		var line = poemLine[1];
		$("#variant-lines-tab").load('/gutorglyn/variant-lines/?p=' + poem + '&l=' + line);
		$("#tabs").tabs('select', 4);
		return false;	
	});	

/* Code to Send Poem Number and line Number to Variant Lines Tab end */

/* jquery end */
}); 
