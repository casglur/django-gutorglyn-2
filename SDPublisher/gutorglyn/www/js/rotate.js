/*globals Raphael */
/* Slide out draw text rotation */

function textGroup(holder, text, paperWidth, paperHeight, fillWidth,
		fillHeight, fillColor) {
	var paper = Raphael(holder, paperWidth, paperHeight);
	var group = paper.set();
	group.push(paper.text(fillWidth, fillHeight, text).attr({
		'fill' : fillColor,
		'font-family' : 'georgia',
		'font-size' : '16',
		'font-weight' : 'bold',
		'letter-spacing' : '-1px'
	}));
	group.transform("r-90");
}

textGroup('trigger', 'Noddywr a Beirdd', 29, 165, 15, 85, '#fff');
textGroup('trigger2', 'Byrfoddau', 29, 110, 15, 55, '#fff');

/* Slide out draw text rotation end*/
