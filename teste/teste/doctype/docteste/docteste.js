// Copyright (c) 2022, TEste and contributors
// For license information, please see license.txt

frappe.ui.form.on('Docteste', {
	refresh: function(frm) {
		frm.add_custom_button('Fora da class', () => {
            frappe.call({
				method: 'teste.teste.doctype.docteste.docteste.metodo_fora',
				callback: function(r) {
					if (r.message) {
						frappe.show_alert(r.message);
					} else {
						frappe.show_alert("sem retorno");
					}
				}
			})
        })		

		frm.add_custom_button('Dentro da class', () => {
            frm.call({
				doc: frm.doc,
				method: 'metodo_dentro',
				callback: function(r) {
					if (r.message) {
						frappe.show_alert(r.message);
					} else {
						frappe.show_alert("sem retorno");
					}
				}
			})
        })		
	},
});
