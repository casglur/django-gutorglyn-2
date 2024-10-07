/*globals $ languageStatus*/

var labels = {
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
	}
};

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
