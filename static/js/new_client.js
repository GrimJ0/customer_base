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
}
