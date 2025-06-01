from flask import Flask, jsonify, request
from createTableOpration import createTables
from addOperation import create_User
from readOperation import authenticate_user

app= Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello, World!'

@app.route('/createUser',methods =['POST'])
def create_user():
    try:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phoneNumber']
        pincode = request.form['pinCode']

        userId =create_User(name = name, password = password, email = email,address = address, phone_number = phone_number, pincode = pincode)
    
        return jsonify({'message':str(userId), 'status':200})

    except Exception as error:
        return jsonify({'message':str(error), 'status':400})
    

@app.route('/login', methods=['POST'])
def login():
    try:
        email= request.form['email']
        password = request.form['password']

        user = authenticate_user(email=email, password=password)
        if user:
            return jsonify({'meaage':user[1], 'status': 200})
        else:
            return jsonify({'message': 'Invalid email or password', 'status': 401})
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})

    
if __name__=='__main__':
    createTables()
    app.run(debug=True)
