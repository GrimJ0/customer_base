var i = 0;

function duplicate() {
    var form = document.getElementById("add_form"),
        original = document.getElementById('original_form'),
        clone = original.cloneNode(true); // "deep" clone
    clone.id = "duplic" + ++i; // there can only be one element with an ID
    form.appendChild(clone);
}