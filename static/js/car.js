let mySwiper2 = document.querySelectorAll('.mySwiper2 img')
let mySwiper4 = document.querySelectorAll('.mySwiper4 img')
let body = document.body


mySwiper2.forEach((item, i) => {
	item.style.cursor = 'pointer'
	item.addEventListener('click', (e)=> {
		const imageView = document.createElement('div')
		imageView.setAttribute('class', 'image-view')
		const image = document.createElement('img')
		image.setAttribute('src', item.src)
		imageView.appendChild(image)
		body.appendChild(imageView)
		imageView.addEventListener('click', (e) => {
			body.removeChild(imageView)
		})
	})
})
mySwiper4.forEach((item, i) => {
	item.style.cursor = 'pointer'
	item.addEventListener('click', (e)=> {
		const imageView = document.createElement('div')
		imageView.setAttribute('class', 'image-view')
		const image = document.createElement('img')
		image.setAttribute('src', item.src)
		imageView.appendChild(image)
		body.appendChild(imageView)
		imageView.addEventListener('click', (e) => {
			body.removeChild(imageView)
		})
	})
})

// Swiper JS | Interior Slider
var swiper = new Swiper(".mySwiper", {
  loop: true,
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
  loop: true,
  spaceBetween: 10,
  navigation: {
	nextEl: ".swiper-button-next",
	prevEl: ".swiper-button-prev",
  },
  thumbs: {
	swiper: swiper,
  },
});

// Swiper JS | Exterior Slider
var swiper3 = new Swiper(".mySwiper3", {
  loop: true,
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper4 = new Swiper(".mySwiper4", {
  loop: true,
  spaceBetween: 10,
  navigation: {
	nextEl: ".swiper-button-next",
	prevEl: ".swiper-button-prev",
  },
  thumbs: {
	swiper: swiper3,
  },
});

// Swiper JS | Q&A Slider
var swiper5 = new Swiper(".mySwiper5", {
        slidesPerView: 2,
        spaceBetween: 30,
        slidesPerGroup: 1,
        loop: false,
        loopFillGroupWithBlank: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      });
