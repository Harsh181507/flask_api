from flask import Flask ,jsonify,request
from createTableOperation import createTables
from addOperation import createUser

app=Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello World!'

@app.route('/createUser', methods=['POST'])
def create_user():
    name=request.form['name']
    password=request.form['password']
    phone_number=request.form['phone_number']
    address=request.form['address']
    pincode=request.form['pincode']
    email=request.form['email']

    user_id=createUser(name=name,password=password,phone_number=phone_number,address=address,pincode=pincode,email=email)

    return user_id





if __name__=='__main__':
    createTables()
    app.run(debug=True) 