// variables - three ways to declare them
let name = "poisondaggers"     // can change
const age = 1                  // can't change
var old = "don't use this"     // old way, avoid it

// string tricks
console.log(name.toUpperCase())
console.log(`hello from ${name}`)  // template literal

// arrays
let songs = ["Flesh", "Strangers", "I Bet on Losing Dogs"]
console.log(songs[0])          // first item
console.log(songs.length)      // how many
songs.push("Super Psycho Love") // add to end

// loops
for (let song of songs) {
    console.log(`- ${song}`)
}

// functions
function greet(person) {
    return `hey ${person}!`
}
console.log(greet("levi"))

// arrow functions (modern way)
const double = (n) => n * 2
console.log(double(5))

// objects (like Python dicts)
const player = {
    name: "poisondaggers",
    health: 100,
    inventory: ["flashlight", "key"]
}
console.log(player.name)
console.log(player.inventory[0])
