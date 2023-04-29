-- Table: type

--DROP TABLE IF EXISTS type;
CREATE TABLE IF NOT EXISTS type (
    type_id SERIAL NOT NULL PRIMARY KEY,
    type VARCHAR(255) NOT NULL UNIQUE
);


--Table: news

--DROP TABLE IF EXISTS news;
CREATE TABLE IF NOT EXISTS news (
    news_id SERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    description TEXT,
    content TEXT,
    data VARCHAR(50),
    url VARCHAR(255) NOT NULL UNIQUE,
    type_id INT,
    
    CONSTRAINT fk_news_type FOREIGN KEY (type_id) REFERENCES type(type_id)
);
