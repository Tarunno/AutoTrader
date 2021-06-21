let nav = document.querySelector('nav')
let humburger = document.querySelector('#humburger-menu')

let menuOpen = false
humburger.addEventListener('click', (e) => {
	if(menuOpen){
		nav.style.display = 'none';
		menuOpen = false
	}
	else{
		nav.style.display = 'block';
		menuOpen = true
	}
})
