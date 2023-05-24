
const input = document.getElementById('user-input')
const submitButton = document.getElementById('input-form')

console.log('We aare here')

submitButton.addEventListener('submit', e => {
    e.preventDefault()

    const userInput = input.value
    input.value = ''

    console.log(userInput)


    // fetch()
})