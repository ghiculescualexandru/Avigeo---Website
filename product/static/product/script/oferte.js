const pas1 = document.querySelector('#oferte-container-pas1')
const pas2 = document.querySelector('#oferte-container-pas2')
const pas3 = document.querySelector('#oferte-container-pas3')
const pret = document.querySelector('.value-pret')
const tva = document.querySelector('.value-tva')
const total = document.querySelector('.value-total')
const oferte = document.querySelector('.oferte-container-pret')
const buttonLink = document.querySelector('.generate-price')

pas1.addEventListener('change', () => {
    checkValue(pas1)
    if (pas1.value != '0') {
        pas2.disabled = false;
    } else {
        pas2.disabled = true;
        pas2.value = '0'
        pas3.disabled = true;
        pas3.value = ''
    }
    pas2.focus()
})

pas2.addEventListener('change', () => {
    checkValue(pas2)

    if (pas2.value != '0') {
        pas3.disabled = false;
    } else {
        pas3.disabled = true;
        pas3.value = ''
    }
    pas3.focus()
})

pas3.addEventListener('change', () => {
    if(pas3.value != '') {
        buttonLink.href = '#pret'
    } else {
        buttonLink.href = '#'
    }
})


function setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(event => {
        textbox.addEventListener(event, () => {
            if (inputFilter(pas3.value)) {
                pas3.oldValue = pas3.value;
                pas3.oldSelectionStart = pas3.selectionStart;
                pas3.oldSelectionEnd = pas3.selectionEnd;
            } else if (pas3.hasOwnProperty("oldValue")) {
                pas3.value = pas3.oldValue;
                pas3.setSelectionRange(pas3.oldSelectionStart, pas3.oldSelectionEnd);
            }
        });
    });
}

// Restrict input to digits and '.' by using a regular expression filter.
setInputFilter(pas3, value => {
    return /^\d*$/.test(value)
})

function checkValue(pas) {
    if(pas.value == 0) {
        pas.setAttribute('id', "border-color")
    } else {
        pas.setAttribute('id', "")
    }
}

// generate price
buttonLink.addEventListener('click', () => {
    if(pas3.value != '') {
        buttonLink.href = '#pret'
        if(!oferte.classList.contains('fade-in')) {
            oferte.classList.add('fade-in')
        }
    }

    checkValue(pas1)
    checkValue(pas2)
    checkValue(pas3)
    // if(pas1.value == 0) {
    //     pas1.style.borderColor = "red"
    // }
    // if(pas2.value == 0) {
    //     pas2.style.borderColor = "red"
    // }
    // if(pas3.value == 0) {
    //     pas3.style.borderColor = "red"
    // }
})


