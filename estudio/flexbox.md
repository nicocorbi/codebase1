# que es flexbox
Flexbox (o Flexible Box Layout) es un modelo de diseño de CSS que proporciona una manera más eficiente de distribuir espacio y alinear elementos dentro de un contenedor

flex-direction: Define la dirección de los elementos dentro del contenedor (puede ser row, column, row-reverse, column-reverse).
justify-content: Alinea los elementos en el eje principal (ej., center, space-between, space-around).
align-items: Alinea los elementos en el eje transversal (ej., flex-start, flex-end, center).
align-self: Permite que un elemento dentro del contenedor tenga una alineación diferente a la de los otros.
flex-wrap: Permite que los elementos se envuelvan si no caben en una sola línea (ej., wrap o nowrap).
Propiedades de los elementos flexibles:

flex-grow: Define cuánto crecerá un elemento para ocupar el espacio disponible en el contenedor.
flex-shrink: Define cuánto se puede reducir un elemento si el contenedor es más pequeño que el espacio necesario para todos los elementos.
flex-basis: Especifica el tamaño inicial de un elemento antes de que crezca o se reduzca.
flex: Es una propiedad abreviada que establece las tres anteriores (flex-grow, flex-shrink, flex-basis).
align-self: Permite modificar la alineación de un solo elemento, sobreescribiendo la propiedad align-items del contenedor.
ejemplo: .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item {
  flex: 1;
}
