console.log("Hola mundo")
const nombre = "juan"
fetch('https://dummyjson.com/recipes/1')
.then(res => res.json())
.then(data => {
    console.log(data)
    // titulo receta
    const nombre = data.name
    console.log(data.name)
    const h1 = document.createElement("h1")
    h1.innerText = nombre
    document.body.appendChild(h1)// introducir en el html
    // dificultad 
    const difficulty = data.difficulty
    const dificultadElemento = document.createElement("p")
    dificultadElemento.innerText = difficulty
    document.body.appendChild(dificultadElemento)
    // ingredientes
    const ingredients = data.ingredients
    const ingredientesElemento = document.createElement("p")
    document.body.appendChild(ingredientesElemento)
    ingredientesElemento.innerText = ingredients
    // pasos 
    const instructions = data.instructions
    const instruccionesElemento = document.createElement("p")
    document.body.appendChild(instruccionesElemento)
    instruccionesElemento.innerText = instructions
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



         