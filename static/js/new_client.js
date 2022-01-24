var i = 1;
const array = [];

function duplicate() {
    var form = document.getElementById("add_form"),
        original = document.getElementById('original_form'),
        el1 = document.getElementsByClassName("original_form").length,
        el2 = document.getElementsByClassName("form_duplic").length,
        sum = el1 + el2;
    if (original === null && i >= 1) {
        original = document.getElementById('form_duplic')
    }

    var clone = original.cloneNode(true); // "deep" clone
    ++i;
    clone.id = "form_duplic"; // there can only be one element with an ID
    clone.className = 'original_form form_' + i;
    document.querySelector('input.first_name').value = ""
    document.querySelector('input.last_name').value = ""
    document.querySelector('input.phone').value = "+7"
    document.querySelector('input.price').value = ""
    var o = 0
    for (let j in clone.children) {

        if (o == 0) {
            clone.children[j].children[0].childNodes[3].childNodes[3].id = 'validationCustom' + sum + 1
            clone.children[j].children[0].childNodes[5].childNodes[3].id = 'validationCustom' + sum + 2
        } else if (o == 1) {
            clone.children[j].children[0].childNodes[1].childNodes[3].id = 'validationCustom' + sum + 3
            clone.children[j].children[0].childNodes[3].childNodes[3].id = 'validationCustom' + sum + 4
        }
        ++o;

    }
    form.appendChild(clone);
    if (sum === 3) {
        var save = document.getElementById("add_save"),
            save_original = document.getElementById('save'),
            save_clone = save_original.cloneNode(true);
        save_clone.id = "save_duplic";
        save.appendChild(save_clone);
    }
    var elems = document.getElementsByClassName("del");
    if (elems.length > 1) {
        for (var j = 0; j < elems.length; j++) {
            elems[j].disabled = false;
        }
    }

}

function deleteRow(obj) {
    var row = obj.parentNode.parentNode.parentNode.parentNode.closest('div'),
        el1 = document.getElementsByClassName("original_form").length,
        el2 = document.getElementsByClassName("form_duplic").length,
        sum = el1 + el2;
    if (sum > 2) {
        var del_rov = row.childNodes[3].childNodes[1].childNodes[1].childNodes[3].id,
            index = array.indexOf(del_rov);
        if (index > -1) {
            array.splice(index, 1);
        }
        row.parentNode.removeChild(row);
    }

    var elems = document.getElementsByClassName("del"),
        save_elem = document.getElementById('save_duplic');
    if (elems.length < 2) {
        for (var j = 0; j < elems.length; j++) {
            elems[j].disabled = true;
        }
    }
    if (elems.length < 4) {
        save_elem.remove()
    }
}


function all(iterable) {
    for (var index = 0; index < iterable.length; index++) {
        if (!iterable[index]) return false;
    }
    return true;
}

function addclasses(div, obj, cls) {
    if (obj.parentNode.getElementsByClassName(cls).length <= 0) {
        $(div).insertAfter(obj);
    }

}

function delclasses(obj, cls) {
    var chil = obj.parentNode.querySelector(cls)
    if (chil != null) {
            obj.parentNode.removeChild(chil)
    }
}

function check() {
    var elems_phone = document.getElementsByClassName('phone'),
        elems_price = document.getElementsByClassName('price');
    for (var i = 0; i < elems_phone.length; i++) {
        var phone = elems_phone[i].value,
            ph_valid = [false, false, false],
            pr_valid = false,
            div_p1 = document.createElement('div'),
            div_p2 = document.createElement('div'),
            div_p3 = document.createElement('div');
        const digits_only = string => [...string].every(c => '0123456789'.includes(c));
        if (phone.slice(0, 2) != '+7') {
            elems_phone[i].classList.add('is-invalid')
            elems_phone[i].classList.remove('is-valid')
            div_p2.className = 'invalid-feedback div_p2'
            div_p2.innerHTML = 'Вместо +7 вы ввели ' + phone[0]
            addclasses(div_p2, elems_phone[i], 'invalid-feedback div_p2')
            var del_rov = elems_phone[i].id,
                index = array.indexOf(del_rov);
            if (index > -1) {
                array.splice(index, 1);
            }
            ph_valid[0] = false
        } else {
            delclasses(elems_phone[i], '.invalid-feedback.div_p2')
            ph_valid[0] = true
        }
        if (!digits_only(phone.slice(2)) || phone.slice(2).length <= 0) {
            elems_phone[i].classList.add('is-invalid')
            elems_phone[i].classList.remove('is-valid')
            div_p1.className = 'invalid-feedback div_p1'
            div_p1.innerHTML = 'Введите телефон в цифрах'
            addclasses(div_p1, elems_phone[i], 'invalid-feedback div_p1')
            var del_rov = elems_phone[i].id,
                index = array.indexOf(del_rov);
            if (index > -1) {
                array.splice(index, 1);
            }
            ph_valid[1] = false
        } else {
            delclasses(elems_phone[i], '.invalid-feedback.div_p1')
            ph_valid[1] = true
        }
        if (phone.length != 12) {
            elems_phone[i].classList.add('is-invalid')
            elems_phone[i].classList.remove('is-valid')
            div_p3.className = 'invalid-feedback div_p3'
            div_p3.innerHTML = 'Длина телефона не совпадает'
            addclasses(div_p3, elems_phone[i], 'invalid-feedback div_p3')
            var del_rov = elems_phone[i].id,
                index = array.indexOf(del_rov);
            if (index > -1) {
                array.splice(index, 1);
            }
            ph_valid[2] = false
        } else {
            delclasses(elems_phone[i], '.invalid-feedback.div_p3')
            ph_valid[2] = true
        }
        if (all(ph_valid)) {
            elems_phone[i].classList.remove('is-invalid')
            elems_phone[i].classList.add('is-valid')
            div_p3.className = 'valid-feedback div_p3'
            div_p3.innerHTML = 'Все хорошо'
            addclasses(div_p3, elems_phone[i], 'valid-feedback div_p3')
        }
        var div_pr1 = document.createElement('div');
        if (!digits_only(elems_price[i].value) || elems_price[i].value.length <= 0) {
            elems_price[i].classList.add('is-invalid')
            elems_price[i].classList.remove('is-valid')
            div_pr1.className = 'invalid-feedback div_pr1'
            div_pr1.innerHTML = 'Введите прайс в цифрах'
            addclasses(div_pr1, elems_price[i], 'invalid-feedback div_pr1')
            var del_rov = elems_price[i].id,
                index = array.indexOf(del_rov);
            if (index > -1) {
                array.splice(index, 1);
            }
            pr_valid = false
        } else {
            elems_price[i].classList.remove('is-invalid')
            elems_price[i].classList.add('is-valid')
            div_pr1.className = 'valid-feedback div_pr1'
            div_pr1.innerHTML = 'Все хорошо'
            addclasses(div_pr1, elems_price[i], 'valid-feedback div_pr1')
            pr_valid = true

        }
        if (all(ph_valid) && pr_valid) {
            if (!array.includes(elems_phone[i].id))
                array.push(elems_phone[i].id)
            if (!array.includes(elems_price[i].id))
                array.push(elems_price[i].id)
        }

    }
}

function checkform() {
    var el1 = document.getElementsByClassName("original_form").length,
        el2 = document.getElementsByClassName("form_duplic").length,
        sum = el1 + el2;
    if (array.length == (sum - 1) * 2) {
        return true
    } else {
        return false
    }
}

