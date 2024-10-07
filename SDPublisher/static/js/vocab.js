/*globals $ languageStatus window*/

function textLabels() {
	window.labels = {
		"search for label" : {
			cym : "&nbsp;&nbsp;Chwilio am ",
			eng : "&nbsp;&nbsp;Search for "
		},
		"search button label" : {
			cym : "Chwilio",
			eng : "Search"
		},
		"show options button label" : {
			cym : "Dangos Opsiynau",
			eng : "Show Options"
		},
		"hide options button label" : {
			cym : "Cuddio Opsiynau",
			eng : "Hide Options"
		},
		"home link" : {
			cym : "Cartref",
			eng : "Home"
		},
		"poems link" : {
			cym : "Y Cerddi",
			eng : "The Poems"
		},
		"patrons and poets link" : {
			cym : "Noddwyr a Beirdd",
			eng : "Patrons and Poets"
		},
		"people and places link" : {
			cym : "Personau a Lleoedd",
			eng : "People and Places"
		},
		"top guidelines link" : {
			cym : "Canllawiau",
			eng : "Guidelines"
		},
		"title list link" : {
			cym : "Rhestr Teitlau",
			eng : "Title List"
		},
		"patron list link" : {
			cym : "Rhestr Noddwyr",
			eng : "Patron List"
		},
		"play audio button label" : {
			cym : "Chwarae sain",
			eng : "Play audio"
		},
		"pause audio button label" : {
			cym : "Sain oedi",
			eng : "Pause udio"
		},
		"show line numbers button label" : {
			cym : "Dangos dolen llinell",
			eng : "Show line numbers"
		},
		"hide line numbers button label" : {
			cym : "Cuddio dolen llinell",
			eng : "Hide line numbers"
		},
		"show name links button label" : {
			cym : "Dangos enwau priod",
			eng : "Show name links"
		},
		"hide name links button label" : {
			cym : "Cuddio enwau priod",
			eng : "Hide name links"
		},
		"lock texts button label" : {
			cym : "Cloi",
			eng : "Lock texts"
		},
		"unlock texts button label" : {
			cym : "Datgloi",
			eng : "Unlock texts"
		},
		"paraphrase tab label" : {
			cym : "Aralleiriad",
			eng : "Paraphrase"
		},
		"notes tab label" : {
			cym : "Nodiadau",
			eng : "Notes"
		},
		"manuscripts tab label" : {
			cym : "Llawysgrifau",
			eng : "Manuscripts"
		},
		"variants tab label" : {
			cym : "Amrywiadau",
			eng : "Variants"
		},
		"explanatory tab label" : {
			cym : "Esboniadol",
			eng : "Explanatory"
		},
		"textual tab label" : {
			cym : "Testunol",
			eng : "Textual"
		},
		"sources tab label" : {
			cym : "Fynonellau",
			eng : "Sources"
		},
		"transcripts tab label" : {
			cym : "Trawsysgrifiadau",
			eng : "Transcripts"
		},
		"images tab label" : {
			cym : "LLuniau",
			eng : "Images"
		},
		"stemma tab label" : {
			cym : "Stema",
			eng : "Stemma"
		},
		"show stemma button label" : {
			cym : "Stema fwy",
			eng : "Popup stemma"
		},
		"patrons and poets draw title" : {
			cym : "Noddwyr a Beirdd",
			eng : "Patrons and Poets"
		},
		"abbreviations draw title" : {
			cym : "Byrfoddau",
			eng : "Abbreviations"
		},
		"homepage welcome" : {
			cym : "Croeso i fersiwn beta gutorglyn.net",
			eng : "Welcome to the beta version of gutorglyn.net"
		},	
		"homepage disclaimer" : {
			cym : "Mae'r wefan yn dal i gael ei datblygu. Unrhyw sylwadau, os gwelwch yn dda, at " +
					"<a id='mailto' style='font-size: 10pt; font-weight: normal; color: black; text-decoration: underline;' " +
					"href='mailto:apo@cymru.ac.uk'>Guto</a>.",
			eng : "The website is still under development. " +
					"Any comments to <a id='mailto' style='font-size: 10pt; font-weight: normal; color: black; text-decoration: underline;' " +
					"href='mailto:apo@cymru.ac.uk'>Guto</a>, please." 
		},
		"slideshow poems" : {
			cym : "/static/img/options/cerddi.jpg",
			eng : "/static/img/options/poems.jpg"
		},
		"slideshow resources" : {
			cym : "/static/img/options/adnoddau.jpg",
			eng : "/static/img/options/adnoddau.jpg"
		},
		"slideshow guidelines" : {
			cym : "/static/img/options/canllawiau.jpg",
			eng : "/static/img/options/guidelines.jpg"
		},
		"slideshow gutoswales" : {
			cym : "/static/img/options/cymru.jpg",
			eng : "/static/img/options/cymru.jpg"
		},
		"slideshow guto" : {
			cym : "/static/img/options/guto_cymraeg.jpg",
			eng : "/static/img/options/guto_saesneg.jpg"
		},
		"slideshow about" : {
			cym : "/static/img/options/prosiect.jpg",
			eng : "/static/img/options/project.jpg"
		},
		"homepage footer links" : {
			cym : "<li class=\"home-page-link\"><a href=\"/gutorglyn/poem/?poem=001\">Y Cerddi</a></li>" +
						"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Am y Prosiect</a></li>" +
							"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto'r Glyn</a></li>" +
									"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Cymru Guto</a></li>" +
											"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Adnoddau</a></li>" +
													"<li class=\"home-page-link\"><a id=\"guidelines-link href=\"/static/docs/cyfarwyddiadau.htm\">Canllawiau</a></li>",
			eng : "<li class=\"home-page-link\"><a href=\"/gutorglyn/poem/?poem=001\">The Poems</a></li>" +
						"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">About the project</a></li>" +
							"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto'r Glyn</a></li>" +
									"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto's Wales</a></li>" +
											"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Resources</a></li>" +
													"<li class=\"home-page-link\"><a id=\"guidelines-link href=\"/static/docs/cyfarwyddiadau.htm\">Guidelines</a></li>"
		},
		"footer copyright" : {
			cym : "&copy;<a href=\"http://www.wales.ac.uk/en/CentreforAdvancedWelshCelticStudies/IntroductiontotheCentre.aspx\">2013 Canolfan Uwchefrydiau Cymreig a Cheltaidd</a>",
			eng : "&copy;<a href=\"http://www.wales.ac.uk/en/CentreforAdvancedWelshCelticStudies/IntroductiontotheCentre.aspx\">2013 Centre for Advanced Welsh and Celtic Studies</a>"
		}

	};
}	

textLabels();

function getText(name) {
	for (var key in labels) {
		var obj = labels[key];
		for (var prop in obj) {
			if (key === name && prop === languageStatus()) {
				//console.log(obj[prop]);
				return obj[prop];
			}
		}
	}
}

getText("home link");

function showLineLinks() {
	$(".variant-line-link-hide").css('visibility', 'visible');
	$(".variant-line-link-hide").css('font-weight', 'bold');
	
	$(".variant-line-link-show").css('color', '#000');
	$(".variant-line-link-show").css('font-weight', 'bold');
	$(".variant-line-link-show").css('text-decoration', 'underline');
	
	$(".show-hide-vlines").button("option", "label", getText("hide line numbers button label"));
}

function hideLineLinks() {
	$(".variant-line-link-hide").css('visibility', 'hidden');
	
	$(".variant-line-link-show").css('font-weight', 'normal');
	$(".variant-line-link-show").css('color', '#8B7D6B');
	$(".variant-line-link-show").css('text-decoration', 'none');
	
	$("show-hide-vlines").button("option", "label", getText("show line numbers button label"));
}

/* code to toggle visibility of variant line links on edited text */
