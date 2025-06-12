from flask import Flask, jsonify, request
from createTableOpration import createTables
from addOperation import create_User
from readOperation import authenticate_user ,getAllUsers , getSpecificUser, get_all_products, get_specific_product, get_all_orders_detail
from updateOperation import approve_user , update_user_details
from delete import delete_specificUser
from addOperation import add_product, order_details  # Make sure this is the correct module name and order_details is defined in addOperation


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
    
        return jsonify({'message': "User Created Successfully", 'status':200})

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

@app.route('/getAllUsers', methods=['GET'])
def get_All_Users():
    try:
        return jsonify(getAllUsers())
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})
    

@app.route('/getSpecificUser',methods=['POST'])
def get_Specific_User():
    try:
        userId= request.form['user_id']

        user = getSpecificUser(userId=userId)

        return jsonify(user)
    

    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})

    

@app.route('/approveUser', methods=['POST'])
def approve_User():

    try:
        user_id = request.form['user_id']
        isApprove = request.form['isApprove']


        update= approve_user(userID=user_id, isApproved=isApprove)

        return jsonify({'message': 'User approval status updated successfully', 'status': 200})
    
    
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})
    

@app.route('/updateUserAllDetails', methods=['PATCH'])
def updateUserAllDetails():
    try:
        user_id = request.form['user_id']
        

        updateUser={}

        for key, value in request.form.items():
            if key != 'user_id':
                updateUser[key] = value
        update_user_details(userId=user_id, **updateUser)

        return jsonify({'message': 'User details updated successfully', 'status': 200})
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})




@app.route('/addProduct', methods=['POST'])
def addProduct():
    try:
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        stock = request.form['stock']

        add_product(name=name, price=price, category=category, stock=stock)
        return jsonify({'message': 'Product added successfully', 'status': 200})
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})

@app.route('/getAllProduct', methods=['GET'])
def getAllProduct():
    try:
        return get_all_products()
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})
    
@app.route('/getSpecificProduct', methods=['POST'])
def getSpecificProduct():
    try:
        product_id = request.form['products_id']
        return jsonify(get_specific_product(product_id=str(product_id)))
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})


@app.route('/addOrderDetails', methods=['POST'])
def addOrderDetails():
    try:
        product_id = request.form['product_id']
        user_id = request.form['user_id']
        product_name = request.form['product_name']
        user_name = request.form['user_name']
        quantity = request.form['quantity']
        message = request.form['message']
        price = request.form['price']
        category = request.form['category']

        order_details(user_id=user_id,message=message, product_id=product_id, product_name=product_name, user_name=user_name, quantity=quantity, price=price, category=category)
        return jsonify({'message': 'Order details added successfully', 'status': 200})
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})


@app.route('/getAllOrdersDetail', methods=['GET'])
def getAllOrdersDetail():
    try:
        return jsonify(get_all_orders_detail())
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})




@app.route('/deleteSpecificUser', methods=['DELETE'])
def deleteSpecificUser():
    try:
        userId = request.form['userID']

        delete_specificUser(userId=userId)
        return jsonify({'message': 'User deleted successfully', 'status': 200})
       
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})
    
if __name__=='__main__':
    createTables()
    app.run(debug=True)
