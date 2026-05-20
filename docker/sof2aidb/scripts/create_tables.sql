\c sof2ai;

CREATE SCHEMA sof2ai;

CREATE TABLE sof2ai.users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    PASSWORD_ VARCHAR(255) NOT NULL
);

CREATE TABLE sof2ai.posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150),
    content TEXT,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sof2ai.comments (
    id SERIAL PRIMARY KEY,
    post_id INT,
    user_id INT,
    content TEXT,
    parent_comment_id INT NULL,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);