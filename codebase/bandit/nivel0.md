# bandit 0

El objertivo es entrar por ssh y leer un archivo `readme`.


host: bandit.labs.overthewire.org
puerto: 2220
usuario: bandit0
contraseña: bandit0

para entrar por ssh debemos mandar :

```bash
ssh usuario@direccion
```

si queremos entrar con otro puerto:

```bash
ssh usario@direccion -p 1234
```

para resolver el nivel:
```bash 
ssh bandit0@bandit.labs.overthewire.org -p 2220
#introducimos contraseña bandit0 para entrar
#la contraseña esta en home/bandit0/readme
#ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
