const users = [
    {
      nombre: "admin",
      password: "admin",
      email: "admin@email.com",
      status: "active"
    },
  {
      nombre: "alberto",
      password: "maracuya",
      email: "alberto@email.com",
      status: "inactive",
      edad: "24"
    }
  ]
  
  const table = document.createElement("table")
  const thead = document.createElement("thead")
  table.appendChild(thead)
  const tr = document.createElement("tr")
  thead.appendChild(tr)
  //donde_quiero_inyectar.appendChild(que_quiero_inyectar)
  const claves = Object.keys(users[1])
  for(let i=0; i < claves.length; i++){
    console.log(claves[i])
    const td = document.createElement("td")
    td.innerText = claves[i]
    tr.appendChild(td)
  }
  
  const tbody = document.createElement("tbody")
  table.appendChild(tbody)
  
  for(let i=0; i < users.length; i++){
    console.log(users[i])
    const tr = document.createElement("tr")
    for(let j=0; j < claves.length; j++){
      const td = document.createElement("td")
      const clave = claves[j]
      td.innerText = users[i][clave]
      tr.appendChild(td)
    }
    tbody.appendChild(tr)
  }
  document.body.appendChild(table)
  // aislar el codigo que hemos creado , una funcion en javascript 
  // que dado una array de un objeto lo haga en la tabla.(es decir,ponerlo en una funcion)
  //codepen.io