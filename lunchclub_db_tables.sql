DROP TABLE votes;
DROP TABLE poll_options;
DROP TABLE lunches;
DROP TABLE restaurants;
DROP TABLE members;
DROP TABLE clubs;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_digest VARCHAR(255) NOT NULL,
    last_login DATE NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL
);

CREATE TYPE member_type AS ENUM ('banned', 'regular', 'admin');

CREATE TABLE clubs (
id SERIAL PRIMARY KEY,
name VARCHAR(255) UNIQUE NOT NULL,
location VARCHAR(255) NOT NULL,
join_code VARCHAR(6) NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL
);

CREATE TABLE members (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
member_info member_type NOT NULL,
email VARCHAR(255) NOT NULL,
club_id INTEGER,
user_id INTEGER UNIQUE,
created_at DATE NOT NULL,
updated_at DATE NOT NULL,

FOREIGN KEY (club_id) REFERENCES clubs,
FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
);

CREATE INDEX members_name_idx ON members (name);

CREATE TABLE restaurants (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
address VARCHAR(255) NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL,
UNIQUE (name, address)
);

CREATE INDEX restaurants_name_idx ON restaurants (name);
CREATE UNIQUE INDEX restaurants_address ON restaurants (address);

CREATE TABLE lunches (
id SERIAL PRIMARY KEY,
club_id INTEGER,
restaurant_id INTEGER,
name VARCHAR(255) NOT NULL,
lunch_date DATE NOT NULL,
poll_open_date DATE NOT NULL,
poll_close_date DATE NOT NULL,

FOREIGN KEY (club_id) REFERENCES clubs,
FOREIGN KEY (restaurant_id) REFERENCES restaurants
);

CREATE INDEX lunches_name_idx ON lunches (name);
CREATE INDEX lunches_date_idx ON lunches (lunch_date);

CREATE TABLE poll_options (
id INTEGER PRIMARY KEY,
lunch_id INTEGER,
restaurant_id INTEGER,

FOREIGN KEY (lunch_id) REFERENCES lunches,
FOREIGN KEY (restaurant_id) REFERENCES restaurants
);

CREATE TABLE votes (
id INTEGER PRIMARY KEY,
member_id INTEGER,
lunch_id INTEGER,
poll_option_id INTEGER,

FOREIGN KEY (member_id) REFERENCES members,
FOREIGN KEY (lunch_id) REFERENCES lunches,
FOREIGN KEY (poll_option_id) REFERENCES poll_options
);

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO lunchclub_app;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO lunchclub_app;
