console.log("Hola mundo")
const nombre = "juan"
fetch('https://dummyjson.com/recipes/1')
.then(res => res.json())
.then(data => {
    console.log(data)
    // título de la receta
    const nombre = data.name
    console.log(data.name)
    const h1 = document.createElement("h1")
    h1.innerText = nombre
    document.body.appendChild(h1) // introducir en el HTML

    // dificultad 
    const difficulty = data.difficulty
    const dificultadElemento = document.createElement("p")
    dificultadElemento.innerText = `Dificultad: ${difficulty}`
    document.body.appendChild(dificultadElemento)

    // ingredientes
    const ingredients = data.ingredients
    const ingredientesElemento = document.createElement("ul") // lista desordenada
    document.body.appendChild(ingredientesElemento)
    ingredients.forEach(ingredient => {
        const item = document.createElement("li")
        item.innerText = ingredient
        ingredientesElemento.appendChild(item)
    })

    // pasos 
    const instructions = data.instructions
    const instruccionesElemento = document.createElement("ol") // lista ordenada
    document.body.appendChild(instruccionesElemento)
    instructions.forEach(step => {
        const item = document.createElement("li")
        item.innerText = step
        instruccionesElemento.appendChild(item)
    })

    // imagen
    const imagenElemento = document.createElement("img");
    imagenElemento.src = data.image; 
    imagenElemento.alt = `Imagen de la receta ${nombre}`;
    imagenElemento.style.width = "50%"; 
    document.body.appendChild(imagenElemento);

    // Tiempo de preparación
    const preparacion = data.prepTimeMinutes;
    const preparacionElemento = document.createElement("p");
    preparacionElemento.innerText = `Tiempo de preparación: ${preparacion} minutos`;
    document.body.appendChild(preparacionElemento);

    // Tiempo de cocinado
    const tiempoCocinado = data.cookTimeMinutes;
    const tiempoCocinadoElemento = document.createElement("p");
    tiempoCocinadoElemento.innerText = `Tiempo de cocción: ${tiempoCocinado} minutos`;
    document.body.appendChild(tiempoCocinadoElemento);
})


         