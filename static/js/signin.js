let input = document.querySelectorAll('.signin input')
let label = document.querySelectorAll('.signin label')
let form = document.querySelector('.signin form')
let errorMessage = document.querySelector('.error')
let showPasswordBtn = document.querySelector('#show-password')

handleInput(input, label, showPasswordBtn)
handleSubmit(form, input, errorMessage)

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
		var formData = new FormData(form)
		console.log(Array.from(formData))
		const url = "/user/signin/"
		fetch(url, {
			method: "post",
			body: formData
		})
		.then((res) => res.json())
		.then((data) => {
			console.log(data);
			if(data.message == "success"){
				input.forEach((field) => handleInputError(field, false, "", errorMessage))
				errorMessage.innerHTML = "Logged in successfully"
				errorMessage.style.borderLeft = '2px solid green'
				errorMessage.style.color = "green"
				form.reset()
				window.location.replace('/user/profile/' + data.userID)
			}
			else{
				let error = "";
				let errorFields = [false, false]
				console.log(message);
				for(const [key, value] of Object.entries(message)){
					input.forEach((field, index) => {
						if(field.name == key){
							handleInputError(field, true)
							errorFields[index] = true
							error = value
						}
					})
				}
				for(let i=0; i<2; i++){
					if(errorFields[i] === false){
						handleInputError(input[i], false)
					}
				}
				console.log(error[0])
				if(error[0] != ""){
					errorMessage.innerHTML = error[0]
					errorMessage.style.color = 'red'
					errorMessage.style.borderLeft = '2px solid red'
				}
			}
		})
	})
}

function handleInputError(field, error ){
	if(error){
		field.style.background = 'rgba(255, 0, 0, .05)'
	}
	else{
		field.style.background = 'white'
	}
}
