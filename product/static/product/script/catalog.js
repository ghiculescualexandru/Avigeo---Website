const catalog = document.querySelector('.catalog')
const bgContainer = document.querySelector('.bg-container')
var myBool = true
const images = document.querySelectorAll('.image-container')

function createGlider() {
    return new Glider(document.querySelector('.glider'), {
        slidesToShow: 3,
        slidesToScroll: 1,
        draggable: true,
        dots: '.dots',
        arrows: {
            prev: '.glider-prev',
            next: '.glider-next',
        }
    })
}

window.addEventListener('load', () => {
    if (window.matchMedia('(min-width: 768px)').matches) {
        catalog.classList.add('glider-contain')
        bgContainer.classList.add('glider')
        createGlider()
        myBool = false
    }
})

window.addEventListener('resize', () => {
    if (window.matchMedia('(min-width: 768px)').matches) {
        if (!catalog.classList.contains('glider-contain')) {
            catalog.classList.add('glider-contain')
        }
        if (!bgContainer.classList.contains('glider')) {
            bgContainer.classList.add('glider')
        }
        if (myBool) {
            createGlider()
            myBool = false
        }
    } else {
        setTimeout(() => {
            if(document.querySelector('.glider-track')) {
                document.querySelector('.glider-track').setAttribute('style', 'width: 100vw')
            }
            images.forEach((image, index) => {
                image.setAttribute('style', 'width: 100%;')
            })
        }, 1)
        catalog.classList.remove('glider-contain')
        bgContainer.classList.remove('glider')
        bgContainer.classList.remove('draggable')
    }
})
