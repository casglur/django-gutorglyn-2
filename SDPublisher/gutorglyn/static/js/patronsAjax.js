/*globals readCookie $ */
function patronAutoComplete() {
	var lang = readCookie('gutorglynlang');
	$.getJSON("/gutorglyn/patrons-json/?lang=" + lang, function (data) {
		$("#name").autocomplete({
			source: data.patrons,
			autoFocus: true,
			minLength: 3,
			select: function (event, ui) {
				$("input#name").val(ui.item.label);
				$("input#n").val(ui.item.value);
				$("#searchForm").submit();
			}
		});
	});
}
