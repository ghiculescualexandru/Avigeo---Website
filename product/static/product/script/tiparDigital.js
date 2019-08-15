const catalogImages = document.querySelectorAll('.catalog-img')
const pageName = document.querySelector('#page')
let linksList = []

function loadList() {
    catalogImages.forEach(img => {
        linksList.push(img.firstElementChild.getAttribute('href'))
    })
}

function removeAttributes() {
    catalogImages.forEach((img, index) => {
        img.firstElementChild.removeAttribute('href')
        img.firstElementChild.removeAttribute('data-lightbox')
    })
}

function addAttributes() {
    catalogImages.forEach((img, index) => {
        img.firstElementChild.setAttribute('href', linksList[index])
        img.firstElementChild.setAttribute('data-lightbox', 'mygallery')
    })
}

window.addEventListener('load', () => {
    loadList()

    lightbox.option({
        'resizeDuration': 50,
        'wrapAround': true,
        'showImageNumberLabel': false,
        'positionFromTop': 120,
        'disableScrolling': true,
        'fadeDuration': 300,
        'imageFadeDuration': 350
    })

    if (!window.matchMedia('(min-width: 768px)').matches) {
        removeAttributes()
    }
})

window.addEventListener('resize', () => {
    if (!window.matchMedia('(min-width: 768px)').matches) {
        removeAttributes()
    } else {
        addAttributes()
    }
})