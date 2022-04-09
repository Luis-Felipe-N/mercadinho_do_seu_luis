const inputImagem = document.querySelector('[data="inputImage"]')
const imageName = document.querySelector('[data="imageName"]')

const handleNameFile = (event) => {
    const nameImage = event.target.files[0].name
    const nameFormated = `${nameImage.slice(0, 10)}...`

    imageName.textContent = nameImage
}

inputImagem.addEventListener('change', handleNameFile)