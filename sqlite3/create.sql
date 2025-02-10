CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ("admin","adminpass");

SELECT * FROM users;