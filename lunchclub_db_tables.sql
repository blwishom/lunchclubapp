DROP TABLE votes;
DROP TABLE poll_options;
DROP TABLE lunches;
DROP TABLE restaurants;
DROP TABLE members;
DROP TABLE clubs;

CREATE TYPE member_type AS ENUM ('banned', 'regular', 'admin');

CREATE TABLE clubs (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
location VARCHAR(255) NOT NULL,
join_code VARCHAR(6) NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL
);

CREATE TABLE members (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
member_info member_type NOT NULL,
username VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
club_id INTEGER,
password_digest VARCHAR(255) NOT NULL,
last_login DATE NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL,

FOREIGN KEY (club_id) REFERENCES clubs
);

CREATE TABLE restaurants (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
address VARCHAR(255) NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL
);

CREATE TABLE lunches (
id SERIAL PRIMARY KEY,
club_id INTEGER,
restaurant_id INTEGER,
name VARCHAR(50) NOT NULL,
lunch_date DATE NOT NULL,
poll_open_date DATE NOT NULL,
poll_close_date DATE NOT NULL,

FOREIGN KEY (club_id) REFERENCES clubs,
FOREIGN KEY (restaurant_id) REFERENCES restaurants
);

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
