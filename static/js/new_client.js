var i = 0;

function duplicate() {
    var form = document.getElementById("add_form"),
        original = document.getElementById('original_form'),
        clone = original.cloneNode(true); // "deep" clone
    clone.id = "duplic" + ++i; // there can only be one element with an ID
    document.getElementById('id_last_name').value = ""
    document.getElementById('id_first_name').value = ""
    document.getElementById('id_phone').value = "+7"
    document.getElementById('id_price').value = ""
    form.appendChild(clone);
    if (i == 3) {
        var save = document.getElementById("add_save"),
            save_original = document.getElementById('save'),
            save_clone = save_original.cloneNode(true);
        clone.id = "duplic";
        save.appendChild(save_clone);
    }

}

