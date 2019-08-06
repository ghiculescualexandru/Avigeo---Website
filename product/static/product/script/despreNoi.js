const printers = document.querySelectorAll('.printer-container')
const printersReverse = document.querySelectorAll('.printer-container-reverse')

// Optiunile pentru intersection obvserver
// Pt a afla ce e intesection observer vezi IntersectionObserver pe google
let printersOptions = {
    rootMargin: '30px 0px 0px 0px',
    threshold: 0,
}

// Intersection observer pentru cele ce apar din partea stanga
const printersObserver = new IntersectionObserver((entries, printersObserver) => {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            entry.target.firstElementChild.classList.add('slide-right')   
            entry.target.firstElementChild.nextElementSibling.classList.add('slide-right')   
            entry.target.lastElementChild.classList.add('slide-left')   
            printersObserver.unobserve(entry.target)       
        } 
    })
}, printersOptions)

// Intersection observer pentru cele ce apar din partea dreapta
const printerReverseObserver = new IntersectionObserver((entries, printerReverseObserver) => {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            entry.target.firstElementChild.classList.add('slide-left')   
            entry.target.firstElementChild.nextElementSibling.classList.add('slide-left')   
            entry.target.lastElementChild.classList.add('slide-right')   
            printerReverseObserver.unobserve(entry.target)       
        } 
    })
}, printersOptions)


printers.forEach(printer => {
    printersObserver.observe(printer)
})

printersReverse.forEach(printer => {
    printerReverseObserver.observe(printer)
})




