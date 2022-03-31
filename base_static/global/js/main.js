const form_cep = document.querySelector(".form__cep")
const campo_cep = document.querySelector(".text__cep")
let api_endpointer = 'https://cep.awesomeapi.com.br/json/'

async function buscar(event) {
    event.preventDefault()
    
    const input_cep = document.querySelector('[data-formcep="input"]')

    const num_cep = input_cep.value

    const response = await fetch(`${api_endpointer}${num_cep}`)

    const responseJson = await response.json()
    console.log(response)
    if (response.status == 200 ) {
        const format_cep = `Endereço: ${responseJson.address}, ${responseJson.district} - ${responseJson.state}`
    
        document.querySelector('.form__cep_container').textContent = format_cep
    } else {
        campo_cep.textContent = responseJson.message
        campo_cep.classList.add('color__error')
    }
}

form_cep.addEventListener('submit', (event) => buscar(event))