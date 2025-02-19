CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT NOT NULL UNIQUE,
   password TEXT NOT NULL,
   age INTEGER,
   gender TEXT,
   points INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS messages (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   id_user INTEGER NOT NULL,
   message TEXT NOT NULL,
   FOREIGN KEY (id_user) REFERENCES users(id)
);

INSERT INTO users (username,password,age,points,gender) VALUES ("admin","adminpass",20 ,100,"H");
INSERT INTO users (username,password,age,gender) VALUES ("user0","user0pass",30,"H");
INSERT INTO users (username,password,age) VALUES ("user1","user1pass", 35);
INSERT INTO users (username,password) VALUES ("user2","user2pass");

SELECT * FROM users;

INSERT INTO messages (id_user,message) VALUES (1,"El madrid roba");
INSERT INTO messages (id_user,message) VALUES (2,"FACTOS");
INSERT INTO messages (id_user,message) VALUES (3,"REAL HERMANO");

SELECT * FROM messages;

