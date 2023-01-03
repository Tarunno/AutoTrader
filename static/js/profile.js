let input = document.querySelectorAll('.add-car .inner-container input')
let label = document.querySelectorAll('.add-car .inner-container label')
let form = document.querySelector('.add-car form')
let errorMessage = document.querySelector('.error')

let textarea = document.querySelectorAll('.add-car .bottom textarea')
let label2 = document.querySelectorAll('.add-car .bottom label')

handleInput(input, label)
handleTextArea(textarea, label2)

function handleInput(Input, Label){
	Input.forEach((el, index) => {
		const handleLabel = (e) => {
			Label.forEach((lv, ix) => {
				lv.style.top = '28px'
				lv.style.fontSize = '15px'
				if(Input[ix].value !== ''){
					lv.style.top = '10px'
					lv.style.fontSize = '10px'
				}
			})
			if(e.type == 'focusin'){
				Label[index].style.top = '10px'
				Label[index].style.fontSize = '10px'
			}
		}
		el.addEventListener('focusin', handleLabel)
		el.addEventListener('focusout', handleLabel)
	})
}
function handleTextArea(Input, Label){
	Input.forEach((el, index) => {
		const handleLabel = (e) => {
			Label.forEach((lv, ix) => {
				lv.style.top = '28px'
				lv.style.fontSize = '15px'
				if(Input[ix].innerText !== ''){
					lv.style.top = '10px'
					lv.style.fontSize = '10px'
				}
			})
			if(e.type == 'focusin'){
				Label[index].style.top = '10px'
				Label[index].style.fontSize = '10px'
			}
		}
		el.addEventListener('focusin', handleLabel)
		el.addEventListener('focusout', handleLabel)
	})
}

// Adding Car | form submit
form.addEventListener('submit', addCarSubmit)

function addCarSubmit(e){
	e.preventDefault()
	let formData = new FormData(form)
	console.log(Array.from(formData))

	let url = '/user/add-car/'
	fetch(url, {
		method: "POST",
		body: formData
	})
	.then((res) => res.json())
	.then((data) => {
		console.log(data)
	})
}
