DROP TABLE IF EXISTS Language CASCADE;
CREATE TABLE Language
(
    language_id   INTEGER     NOT NULL PRIMARY KEY AUTO_INCREMENT,
    language_name VARCHAR(64) NOT NULL
);

DROP TABLE IF EXISTS Usr CASCADE;
CREATE TABLE Usr
(
    user_id   INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(64) NOT NULL UNIQUE
);


DROP TABLE IF EXISTS Tag CASCADE;
CREATE TABLE Tag
(
    tag_id   INTEGER PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(64) NOT NULL
);

DROP TABLE IF EXISTS Repository CASCADE;
CREATE TABLE Repository
(
    repository_id   INTEGER PRIMARY KEY,
    repository_name VARCHAR(64) NOT NULL,
    description     VARCHAR(120),
    last_update     DATE,
    stars DOUBLE,
    url             VARCHAR(255),
    user_name       VARCHAR(64),
    FOREIGN KEY (user_name) REFERENCES Usr (user_name)
);

DROP TABLE IF EXISTS repository_tag CASCADE;
CREATE TABLE repository_tag
(
    repository_id INTEGER,
    tag_id        INTEGER,
    PRIMARY KEY (repository_id, tag_id),
    FOREIGN KEY (repository_id) REFERENCES Repository (repository_id),
    FOREIGN KEY (tag_id) REFERENCES Tag (tag_id)
);

DROP TABLE IF EXISTS repository_language CASCADE;
CREATE TABLE repository_language
(
    repository_id INTEGER,
    language_id   INTEGER,
    PRIMARY KEY (repository_id, language_id),
    FOREIGN KEY (repository_id) REFERENCES Repository (repository_id),
    FOREIGN KEY (language_id) REFERENCES Language (language_id)
);