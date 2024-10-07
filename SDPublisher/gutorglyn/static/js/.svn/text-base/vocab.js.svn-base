/*globals $ languageStatus window console*/


var convertedLanguageStatus = languageStatus();
convertedLanguageStatus = convertedLanguageStatus.replace('-GB', '');

function textLabels() {
	window.labels = {
		"show options button label" : {
			cy : "Dangos Opsiynau",
			en : "Show Options"
		},
		"hide options button label" : {
			cy : "Cuddio Opsiynau",
			en : "Hide Options"
		},
		"play audio button label" : {
			cy : "Chwarae sain",
			en : "Play audio"
		},
		"pause audio button label" : {
			cy : "Sain oedi",
			en : "Pause audio"
		},
		"show line numbers button label" : {
			cy : "Dangos dolen llinell",
			en : "Show line numbers"
		},
		"hide line numbers button label" : {
			cy : "Cuddio dolen llinell",
			en : "Hide line numbers"
		},
		"show name links button label" : {
			cy : "Dangos enwau priod",
			en : "Show name links"
		},
		"hide name links button label" : {
			cy : "Cuddio enwau priod",
			en : "Hide name links"
		},
		"lock texts button label" : {
			cy : "Cloi sgrolio",
			en : "Lock scrolling"
		},
		"unlock texts button label" : {
			cy : "Datgloi scrolio",
			en : "Unlock scrolling"
		},		
		"patrons and poets draw title" : {
			cy : "Noddwyr a Beirdd",
			en : "Patrons and Poets"
		},
		"abbreviations draw title" : {
			cy : "Byrfoddau",
			en : "Abbreviations"
		},
		"slideshow poems" : {
			cy : "/static/img/options/cerddi.jpg",
			en : "/static/img/options/poems.jpg"
		},
		"slideshow resources" : {
			cy : "/static/img/options/adnoddau.jpg",
			en : "/static/img/options/adnoddau.jpg"
		},
		"slideshow guidelines" : {
			cy : "/static/img/options/canllawiau.jpg",
			en : "/static/img/options/guidelines.jpg"
		},
		"slideshow gutoswales" : {
			cy : "/static/img/options/cymru.jpg",
			en : "/static/img/options/cymru.jpg"
		},
		"slideshow guto" : {
			cy : "/static/img/options/guto_cymraeg.jpg",
			en : "/static/img/options/guto_saesneg.jpg"
		},
		"slideshow about" : {
			cy : "/static/img/options/prosiect.jpg",
			en : "/static/img/options/project.jpg"
		},
		"homepage footer links" : {
			cy : "<li class=\"home-page-link\"><a href=\"/gutorglyn/poem\">Y Cerddi</a></li>" +
						"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Am y Prosiect</a></li>" +
							"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto'r Glyn</a></li>" +
									"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Cymru Guto</a></li>" +
											"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Adnoddau</a></li>" +
													"<li class=\"home-page-link\"><a id=\"guidelines-link href=\"/static/docs/cyfarwyddiadau.htm\">Canllawiau</a></li>",
			en : "<li class=\"home-page-link\"><a href=\"/gutorglyn/poem\">The Poems</a></li>" +
						"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">About the project</a></li>" +
							"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto'r Glyn</a></li>" +
									"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Guto's Wales</a></li>" +
											"<li class=\"home-page-link\"><a href=\"/gutorglyn/\">Resources</a></li>" +
													"<li class=\"home-page-link\"><a id=\"guidelines-link href=\"/static/docs/cyfarwyddiadau.htm\">Guidelines</a></li>"
		},

	};
}	

textLabels();

function getText(name) {
	var labels = window.labels;
	for (var key in labels) {
		var obj = labels[key];
		for (var prop in obj) {
			if (key === name && prop === convertedLanguageStatus) {
				console.log(obj[prop]);
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
