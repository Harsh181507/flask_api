from flask import Flask ,jsonify
from createTableOperation import createTables

app=Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello World!'

@app.route('/createUser', methods=['POST'])
def create_user():
    return hs




if __name__=='__main__':
    createTables()
    app.run(debug=True)