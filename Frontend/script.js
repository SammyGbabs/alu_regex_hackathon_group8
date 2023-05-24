
const input = document.getElementById('user-input')
const submitButton = document.getElementById('input-form')

console.log('We aare here')

submitButton.addEventListener('submit', e => {
    e.preventDefault()

    const userInput = input.value
    input.value = ''

    const url = 'http://127.0.0.1:4000/regex/match/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: userInput,
        // mode: 'no-cors'

    }).then((response) => {
        console.log(response.text())
    }).catch((error) => {
        console.log(error);
    })
})