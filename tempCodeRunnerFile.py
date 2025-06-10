@app.route('/approveUser', methods=['POST'])
def approve_User():

    try:
        user_id = request.form['user_id']
        isApproved = request.form['isApproved']


        update= approve_user(userId=user_id, isApprove=isApproved)

        return jsonify({'message': 'User approval status updated successfully', 'status': 200})
    except Exception as error:
        return jsonify({'message': str(error), 'status': 400})




