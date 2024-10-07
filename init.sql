-- Check if the database exists, and create it if it does not
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'employees_db') THEN
        PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE employees_db');
    END IF;
END $$;

-- Connect to the new database
\c employees_db;

-- Check if the table exists, and create it if it does not
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'employees') THEN
        CREATE TABLE employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            position VARCHAR(100) NOT NULL,
            salary INTEGER NOT NULL
        );
    END IF;
END $$;
