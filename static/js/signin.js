let input = document.querySelectorAll('.signup input')
let label = document.querySelectorAll('.signup label')
let form = document.querySelector('.signup form')
let error = document.querySelector('.error')
let showPasswordBtn = document.querySelector('#show-password')

handleInput(input, label, showPasswordBtn)
handleSubmit(form, input, error)

function handleInput(input, label){
	let showPassword = false
	showPasswordBtn.addEventListener('click', (e) => {
		if(showPassword){
			input[1].type = 'password'
			showPassword = false
			showPasswordBtn.className = 'fas fa-eye-slash'
		}
		else{
			input[1].type = 'text'
			showPassword = true
			showPasswordBtn.className = 'fas fa-eye'
		}
	})
	input.forEach((el, index) => {
		const handleLabel = (e) => {
			label.forEach((lv, ix) => {
				lv.style.top = '28px'
				lv.style.fontSize = '15px'
				if(input[ix].value !== ''){
					lv.style.top = '10px'
					lv.style.fontSize = '10px'
				}
			})
			if(e.type == 'focusin'){
				label[index].style.top = '10px'
				label[index].style.fontSize = '10px'
			}
		}
		el.addEventListener('focusin', handleLabel)
		el.addEventListener('focusout', handleLabel)
	})
}

function handleSubmit(form, input, error){
	form.addEventListener('submit', (e) => {
		e.preventDefault()
		let errorFlag = false
		let errorMessage = ''
		input.forEach((el) => {
			if(el.value == ''){
				el.style.background = 'rgba(255, 0, 0, .05)'
				errorFlag = true
				errorMessage = 'Empty fields'
			} else {
				el.style.background = 'white'
			}
		})
		if(errorFlag){
			error.innerHTML = errorMessage
			error.style.borderLeft = '2px solid red'
		}
		else{
			error.innerHTML = ''
			error.style.borderLeft = 'none'
		}
	})
}
