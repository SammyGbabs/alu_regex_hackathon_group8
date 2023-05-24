
const input = document.getElementById('user-input')
const submitButton = document.getElementById('input-form')
const displayContainer = document.getElementById('display-body')

const appendResult = (message) => {
    const messageElem = document.createElement('ul');
    messageElem.innerHTML = `${message}`
    displayContainer.append(messageElem)
}

submitButton.addEventListener('submit', e => {
    
    const userInput = input.value
    input.value = ''

    const url = 'https://regex-server.onrender.com/regex/match/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: userInput,
    }).then((response) => {
        return response.json()
    })
        .then((response) => {
            const data = response.data
            for (const [key, value] of Object.entries(data)) {
                appendResult(`${key}: ${value}`)
            }
        }).catch((error) => {
            console.log(error);
        })
})