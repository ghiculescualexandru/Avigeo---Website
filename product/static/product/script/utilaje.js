function createGlider(glider, firstButton, secondButton, buttons) {
    return new Glider(glider, {
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        dots: buttons,
        arrows: {
            prev: firstButton,
            next: secondButton,
        }
    })
}

window.addEventListener('load', () => {
    createAllGliders()
})

const gliders = document.querySelectorAll('.glider')

function createAllGliders() {
    gliders.forEach(glider => {
        createGlider(glider, glider.nextElementSibling, glider.nextElementSibling.nextElementSibling, glider.nextElementSibling.nextElementSibling.nextElementSibling)        
    })
    
}



