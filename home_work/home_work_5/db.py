""""
create table if not exists orders (
	order_id SERIAL primary key,
	created_dt date not null,
	updated_dt date,
	order_type text not null,
	description text not null,
	status text not null,
	serial_no integer not null,
	creator_id integer not null
	);

create table if not exists employees (
	employee_id SERIAL primary key,
	fio text not null,
	position text not null,
	department_id integer not null
	);

create table if not exists departments (
	department_id SERIAL primary key,
	director_id integer not null,
	department_name text not null
	);
"""