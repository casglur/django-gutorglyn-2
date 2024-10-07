/*globals Raphael lables getText*/

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

textGroup('trigger', getText("patrons and poets draw title"), 29, 165, 15, 85, '#fff');
textGroup('trigger2', getText("abbreviations draw title"), 29, 130, 15, 68, '#fff');

/* Slide out draw text rotation end*/
