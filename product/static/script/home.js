const chartElements = document.querySelectorAll('.chart')
const secondImageContainer = document.querySelector('.landing-second')
const boxes = document.querySelectorAll('.chart-container')

function createPieChart() {
    chartElements.forEach((element, index) => {
        let duration = 3000
        if (index == 1) {
            duration = 5000
        }
        if (index == 2) {
            duration = 2500
        }
        var chart = new EasyPieChart(element, {
            barColor: function (percent) {
                let ctx = this.renderer.getCtx();
                let canvas = this.renderer.getCanvas();
                let gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
                gradient.addColorStop(0, "#ffe57e");
                gradient.addColorStop(1, "#de5900");
                return gradient;
            },
            scaleLength: 0,
            size: 90,
            animate: {
                duration,
                enabled: true,
            },
        });
        let updates = [17, 500, 13]
        chart.update(100)

        let i = 1;
        // let dataPercent = element.getAttribute('data-percent')
        let dataPercent = updates[index]
        let loader = setInterval(() => {            
            element.firstElementChild.innerHTML = i
            if (i == dataPercent) {
                clearInterval(loader)
            }
            i++
        }, duration / dataPercent)
    })
}


secondImageContainerOptions = {
    rootMargin: '100px 0px 0px 0px',
    threshold: 0.4,
}

const secondImageContainerObserver = new IntersectionObserver((entries, secondImageContainerObserver) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            boxes.forEach(box => {
                createPieChart()
                box.classList.add('bounce-in')
            })
            secondImageContainerObserver.unobserve(entry.target)
        }
    })

}, secondImageContainerOptions)

secondImageContainerObserver.observe(secondImageContainer)



