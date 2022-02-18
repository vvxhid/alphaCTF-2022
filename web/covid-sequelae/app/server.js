const express = require("express");
const mysql = require("mysql");
const path = require("path");

// init connection
const connection = mysql.createConnection({
  host: "db",
  user: "root",
  password: "alphaCTF2022",
  database: "sequelae",
});

const app = express(); 
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// connect handler
connection?.connect((error) => {
  if (error) throw error;
  console.log("Mysql connected!");
  // create table users
  const create_sql =
    "CREATE TABLE IF NOT EXISTS  users (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,username varchar(40) NOT NULL, password varchar(520) NOT NULL) ENGINE = InnoDB";
  connection.query(create_sql, (error, result) => {
    if (error) throw error;
    console.log("Table users created!");
    // init users
    const insert_sql = "INSERT IGNORE INTO users VALUES (1, 'admin', SHA2(RAND(), 512) )";
    connection.query(insert_sql, (error, result) => {
      if (error) throw error;
      console.log("Admin created!");
    });
  });
});

// render login page
app.get("/", (req, res) => {
  res?.sendFile(path?.join(__dirname + "/login.html"));
});

app.post("/login", (req, res) => {
  try {
    if (req?.body?.password) {
      connection?.query(
        'SELECT * FROM users WHERE username = "admin" AND password = ?',
        [req?.body?.password],
        (error, results, fields) => {
          if (error) {
            throw error;
            res.end("Something went wrong");
          }
          if (results && results?.length > 0) {
            res?.send(`Hello admin,here is your Flag: ${process?.env?.FLAG}`);
          } else {
            res?.send("Try again!");
          }
          res?.end();
        }
      );
    } else {
      res?.send("Hack this app please");
      res?.end();
    }
  } catch (error) {
    res?.end();
  }
});

app.listen(3000);
