/*globals $ */
function patronAutocomplete() {
	$('#patronVal').autocomplete({        
		source: function (request, response) {
			$.ajax({
				url: "http://localhost:8000/gutorglyn/patrons-json/?lang=cym",
				dataType: "json",
				maxRows: 12,
				name_startsWith: request.term,
				success: function (data) {
					response($.map(data.patrons, function (item) {
						return {
							label: item.name,
							value: item.value
						};
					}));
				}
			});
		}
	});
}
