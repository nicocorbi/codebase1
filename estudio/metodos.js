//los datos primitivos son objetos en JavaScript

/*
*/

console.log("hola") //"hola"

console.log("hola".length) //4
/*
console.log("hola".toUpperCase()) //HOLA
console.log("hola".toLowerCase()) //hola
console.log("hola".split('')) //["h", "o", "l", "a"]
console.log("hola".split('')[0]) //hola

console.log("hola".split('o')) //["h", "la"]
console.log("hola".replace('o', '0')) //h0la
console.log("hola".replace(/o/g, '0')) //h0la
console.log("hola".indexOf('o')) //1
console.log("hola".lastIndexOf('o')) //2
console.log("hola".includes('o')) //true
console.log("hola".startsWith('h')) //true
console.log("hola".endsWith('a')) //true
console.log("hola".slice(1, 3)) //ol
console.log("hola".substring(1, 3)) //ol
console.log("hola".charAt(1)) //o
console.log("hola".charCodeAt(1)) //111

console.log("hola".repeat(3)) //holaholahola
console.log("hola".split('').reverse().join('')) //aloh
console.log("hola".split('').map(char => char.repeat(3)).join('')) //hhhooolllaaa
console.log("hola".split('').map(char => char.repeat(3)).join('').split('').reverse().join('')) //aaallllooohhh

console.log("hola".split('').map(char => {
    switch (char) {
        case 'a': return '4';
        case 'e': return '3';
        case 'i': return '1';
        case 'o': return '0';
        case 'u': return 'v';
        default: return char;
    }
}).join('')) //h0l4
*/
