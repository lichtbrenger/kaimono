DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS kanji;

CREATE TABLE user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);

CREATE TABLE groveries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
);

