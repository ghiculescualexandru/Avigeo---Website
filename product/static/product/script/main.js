const burger = document.querySelector('#menu-checkbox')
const menu = document.querySelector('.menu')
const MAIN = document.querySelector('main')

// Dropdown
const dropdownButton = document.querySelectorAll('.dropdown-btn-mobile')
const dropdownButton1 = document.querySelector('.dropdown-btn1')
const dropdownButton2 = document.querySelector('.dropdown-btn2')
const dropdownContent = document.querySelectorAll('.dropdown-content')
const menuLinks = document.querySelectorAll('.menu-item a')

window.addEventListener('resize', () => {
    if (window.matchMedia('(min-width: 768px)').matches) {
        menu.classList.remove('menu-open')
        burger.checked = false
        closeDropdowns()
    }
    if (window.matchMedia('(max-width: 768px)').matches) {
        menu.classList.remove('menu-open')
        burger.checked = false
        closeDropdowns()
        menu.style.display = 'none'
        setTimeout(() => {
            menu.style.display = 'block'
        }, 1)
    }
    if (window.matchMedia('(min-width: 1024px)').matches) {
        dropdownContent.forEach(el => {
            el.style.display = 'none'
            setTimeout(() => {
                el.style.display = 'block'
            }, 50)
        })
    }
    if(window.matchMedia('(max-height: 560px').matches) {
        menuLinks.forEach(link => {
            link.style.maxHeight = "56px"
        })
    }
})

burger.addEventListener('change', () => {
    if (burger.checked) {
        menu.classList.add('menu-open')
    } else {
        menu.classList.remove('menu-open')
        closeDropdowns()
    }
})

MAIN.addEventListener('click', () => {
    burger.checked = false
    menu.classList.remove('menu-open')
    closeDropdowns()
})

function collapseSection(el) {
    let sectionHeight = el.scrollHeight

    let elementTransition = el.style.transition;
    el.style.transition = '';

    requestAnimationFrame(() => {
        el.style.height = sectionHeight + 'px';
        el.style.transition = elementTransition;

        requestAnimationFrame(() => {
            el.style.height = 0 + 'px';
        });
    });

    el.setAttribute('data-collapsed', 'true');
}

function expandSection(el) {
    var sectionHeight = el.scrollHeight;

    el.style.height = sectionHeight + 'px';

    el.addEventListener('transitionend', function (e) {
        el.removeEventListener('transitionend', arguments.callee);
        el.style.height = null;
    });

    el.setAttribute('data-collapsed', 'false');
}

function closeDropdowns() {
    dropdownContent.forEach(el => {
        collapseSection(el)
    })
}

// Close dropdowns on page load
closeDropdowns()


dropdownButton.forEach((el, index) => {
    el.addEventListener('click', () => {
        let sibling = el.parentElement.nextElementSibling
        // let otherElement;
        if (index == 0) {
            // otherElement = dropdownButton2.parentElement.nextElementSibling
        } else {
            otherElement = dropdownButton1.parentElement.nextElementSibling
        }
        // if (otherElement.getAttribute('data-collapsed') === 'false')
        //     collapseSection(otherElement)
        if (sibling.getAttribute('data-collapsed') === 'true')
            expandSection(sibling);
        else collapseSection(sibling)
    })
})


/* ********* Media *********/
