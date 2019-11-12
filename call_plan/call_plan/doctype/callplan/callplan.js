// Copyright (c) 2019, Handoko and contributors
// For license information, please see license.txt

frappe.ui.form.on('Callplan',{
	on_submit: function(frm) {
		var ischecked = [];
		$('input[type=checkbox]').each(function (i, v) {
			if(this.checked && i < 7){
				ischecked.push(1);
			}
		});

		if(ischecked.length < 1){
			alert("Coverage should be checked")
			validate = false;
			return false;
		}
	},
	// refresh: function(frm) {

	// }
});
