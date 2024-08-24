CREATE TABLE servers(
    server_id INTEGER UNIQUE NOT NULL,
    channel_id INTEGER NOT NULL,
    PRIMARY KEY(server_id)
);
CREATE TABLE posted(
    server_id INTEGER,
    post_code TEXT,
    FOREIGN KEY(server_id) REFERENCES server(server_id) ON DELETE CASCADE
);
CREATE TABLE pages(
    server_id INTEGER,
    page TEXT,
    FOREIGN KEY(server_id) REFERENCES server(server_id) ON DELETE CASCADE
);