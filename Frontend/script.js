
const input = document.getElementById('user-input')
const submitButton = document.getElementById('input-form')

console.log('We aare here')

submitButton.addEventListener('submit', e => {
    e.preventDefault()

    const userInput = input.value
    input.value = ''

    const url = 'https://regex-server.onrender.com/regex/match/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: userInput,
        // mode: 'no-cors'

    }).then((response) => {
        return response.json()
    })
    .then((response) => {
        console.log('Resp Text', response.text())
        console.log('Resp Body', response.body)
        console.log('Resp Body Data', response.body.data)
    }).catch((error) => {
        console.log(error);
    })
})