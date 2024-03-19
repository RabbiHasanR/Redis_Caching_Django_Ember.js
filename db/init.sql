-- Create a table example
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert initial data
INSERT INTO example (name) VALUES ('John'), ('Alice'), ('Bob');
