from flask import Flask

app= Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello, World!'

@app.route('/createUser',methods =['POST'])
def create_user():



    if __name__=='__main__':
        app.run(debug=True)
