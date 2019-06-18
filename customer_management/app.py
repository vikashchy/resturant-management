from flask import Flask, request, jsonify, g
from dbhelper import create_conn
import sqlite3

app = Flask(__name__)


@app.route('/cust/<int:cust_id>', methods=['GET'])
def get_customer_details(cust_id):
    sql = f'select rowid,cust_name, cust_email, cust_address, cost_phone from customerDetails ' \
        f'where rowid={cust_id}'
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute(sql)
        cust_details = cur.fetchall()
        print(cust_details)
        cur.close()
        conn.close()
        return jsonify({'cust_id': cust_details[0], 'cust_name': cust_details[1], 'cust_email': cust_details[2],
                        'cust_add': cust_details[3],
                        'cust_phone': cust_details[4]})
    except sqlite3.Error as e:
        return f'Error occured {e}', 404


@app.route('/cust/create', methods=['POST'])
def create_customer():
    cust_email = request.json['email']
    cust_name = request.json['name']
    cust_address = request.json['address']
    cust_phone = request.json['phone']
    try:
        print('going to create conn')
        conn = create_conn()
        cur = conn.cursor()
        cur.execute('insert into customerDetails values(?,?,?,?)', (cust_name, cust_email, cust_address, cust_phone))
        cust_id = cur.lastrowid
        conn.commit()
    except sqlite3.Error as e:
        return e, 404
    return jsonify({'message': 'Customer created successfully', 'cust_id': str(cust_id)})


@app.route('/cust/update/<int:cust_id>', methods=['PUT'])
def update_customer(cust_id):
    cust_email = request.json['email']
    cust_name = request.json['name']
    cust_address = request.json['address']
    cust_phone = request.json['phone']
    sql = 'update customerDetails set cust_name = ?, cust_email=?, cust_address=?, cost_phone=? where rowid=?'
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute(sql, (cust_name, cust_email, cust_address, cust_phone, cust_id))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({'Message': 'Error Occured' + str(e)}), 404
    return jsonify({'cust_email': cust_email, 'cust_name': cust_name, 'cust_address': cust_address,
                    'cust_phpone': cust_phone, 'message': 'Detailsupdated successfully'})


@app.route('/cust/delete/<int:cust_id>', methods=['DELETE'])
def delete_customer(cust_id):
    sql = 'delete from customerDetails where rowid=?'
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute(sql, (cust_id,))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({'Message': 'Error Occured' + str(e)}), 404
    return jsonify({'Message': 'Record deleted for customer id' + cust_id})


if __name__ == '__main__':
    app.run(debug=True)
