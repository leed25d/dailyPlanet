#!/bin/bash
psql <<EOF

drop table if exists users;
CREATE TABLE users
(
    id    serial primary key,
    first_name        VARCHAR(40) not null,
    last_name         VARCHAR(40) not null,
    userid            VARCHAR(40) not null
);

drop table if exists groups;
CREATE TABLE groups
(
    id    serial primary key,
    name            VARCHAR(40) not null
);

drop table if exists users_groups;
CREATE TABLE users_groups (
    users_id    int REFERENCES users (id) ON UPDATE CASCADE ON DELETE CASCADE,
    groups_id   int REFERENCES groups (id) ON UPDATE CASCADE
);

EOF
