
const input = document.getElementById('user-input')
const submitButton = document.getElementById('input-form')
const displayContainer = document.getElementById('display-body')

const appendResult = (message) => {
    const messageElem = document.createElement('ul');
    messageElem.innerHTML = `${message}`
    messageContainer.append(messageElem)
}

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
            const data = response.data
            for (const [key, value] of Object.entries(data)) {
                console.log(`${key}: ${value}`);
                appendResult(`${key}: ${value}`)
            }
            console.log('Resp Data', response.data)
        }).catch((error) => {
            console.log(error);
        })
})