from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# db
conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="car_db"
)


@app.route("/customer", methods=["POST"])
def add_customer():
    name = request.json.get("name")
    address = request.json.get("address")
    phone_number = request.json.get("phone_number")

    cursor = conn.cursor()
    query = "INSERT INTO Customers (name, address, phone_number) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, address, phone_number))
    conn.commit()

    return jsonify({"message": "Customer added successfully"}), 201


@app.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    name = request.json.get("name")
    address = request.json.get("address")
    phone_number = request.json.get("phone_number")

    cursor = conn.cursor()
    query = (
        "UPDATE Customers SET name=%s, address=%s, phone_number=%s WHERE customer_id=%s"
    )
    cursor.execute(query, (name, address, phone_number, customer_id))
    conn.commit()

    return jsonify({"message": "Customer updated successfully"}), 200


@app.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    cursor = conn.cursor()
    query = "DELETE FROM Customers WHERE customer_id=%s"
    cursor.execute(query, (customer_id,))
    conn.commit()

    return jsonify({"message": "Customer deleted successfully"}), 200


@app.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Customers WHERE customer_id=%s"
    cursor.execute(query, (customer_id,))
    customer = cursor.fetchone()

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200


if __name__ == "__main__":
    app.run(debug=True)
