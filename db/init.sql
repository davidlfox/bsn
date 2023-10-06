CREATE DATABASE
IF NOT EXISTS car_db;

USE car_db;

CREATE TABLE Customers
(
    customer_id INT
    AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR
    (255),
    address VARCHAR
    (255),
    phone_number VARCHAR
    (15)
);

    CREATE TABLE Vehicles
    (
        vehicle_id INT
        AUTO_INCREMENT PRIMARY KEY,
    type ENUM
        ('small car', 'family car', 'van'),
    availability BOOLEAN DEFAULT TRUE
);

        CREATE TABLE Invoices
        (
            invoice_id INT
            AUTO_INCREMENT PRIMARY KEY,
    amount_due DECIMAL
            (10,2),
    date DATE
);

            CREATE TABLE Bookings
            (
                booking_id INT
                AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_id INT,
    date_of_hire DATE,
    return_date DATE,
    invoice_id INT,
    FOREIGN KEY
                (customer_id) REFERENCES Customers
                (customer_id),
    FOREIGN KEY
                (vehicle_id) REFERENCES Vehicles
                (vehicle_id),
    FOREIGN KEY
                (invoice_id) REFERENCES Invoices
                (invoice_id)
);
