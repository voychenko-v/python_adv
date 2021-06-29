""""
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt DATE,
    order_type TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL
    );

CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL
    );

CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    position TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    ON UPDATE SET NULL
    ON DELETE CASCADE
    );
"""