let mySwiper2 = document.querySelectorAll('.mySwiper2 img')
let mySwiper4 = document.querySelectorAll('.mySwiper4 img')
let body = document.body
let askQuestionBtn = document.querySelector('.ask-question-btn')

swiperFullImageView(mySwiper2);
swiperFullImageView(mySwiper4);
askQuestionBtn.addEventListener('click', askQuestion)


function swiperFullImageView(swiper){
	swiper.forEach((item, i) => {
		item.style.cursor = 'pointer'
		item.addEventListener('click', (e)=> {
			const imageView = document.createElement('div')
			imageView.setAttribute('class', 'overlay-view')
			const image = document.createElement('img')
			image.setAttribute('class', 'full-view-image')
			image.setAttribute('src', item.src)
			imageView.appendChild(image)
			body.appendChild(imageView)
			imageView.addEventListener('click', (e) => {
				body.removeChild(imageView)
			})
		})
	})
}

function askQuestion(){
	const askQuestionView = document.createElement('div')
	askQuestionView.setAttribute('class', 'overlay-view')
	const askQuestionForm = document.createElement('form')
	askQuestionForm.setAttribute('class', 'ask-question-form')
	askQuestionForm.innerHTML = `
	<h2>Ask a question </h2>
	<textarea></textarea>
	<button> Ask </button>`
	body.appendChild(askQuestionForm)
	body.appendChild(askQuestionView)
	document.querySelector('.ask-question-form textarea').focus()
	askQuestionView.addEventListener('click', (e) => {
		body.removeChild(askQuestionView)
		body.removeChild(askQuestionForm)
	})
}

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
window.addEventListener('resize', () => {
	if(window.innerWidth <= 830){
		var swiper5 = new Swiper(".mySwiper5", {
		        slidesPerView: 1,
		        spaceBetween: 20,
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
	}
	else{
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
	}
})
