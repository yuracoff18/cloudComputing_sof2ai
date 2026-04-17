CREATE DATABASE sof2ai;

\c sof2ai;

CREATE SCHEMA sof2ai;

CREATE TABLE sof2ai.users(
    id SERIAL4 NOT NULL PRIMARY KEY,
    "name" VARCHAR(80) NOT NULL,
    email VARCHAR(100) NOT NULL,
    verified BOOLEAN NULL DEFAULT false,
    "password" VARCHAR(64) NOT NULL,
    active BOOLEAN NOT NULL,
    create_dt TIMESTAMP NOT NULL,
    update_dt TIMESTAMP NOT NULL
);


INSERT INTO sof2ai.users (
    "name",
    email,
    "password",
    verified,
    active,
    create_dt,
    update_dt
) VALUES (
    'juan',
    'juan@juan.com',
    'juan1234',
    false,
    true,
    NOW()::TIMESTAMP(0),
    NOW()::TIMESTAMP(0)
), (
    'carlos',
    'carlos@gmail.com',
    'carlos1234',
    false,
    true,
    NOW()::TIMESTAMP(0),
    NOW()::TIMESTAMP(0)
)