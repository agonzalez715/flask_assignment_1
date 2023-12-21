from flask import flask
#we need to import the flask class instance to use flask in python

app = Flask(__name__)
#creates an instance of the Flask class so we can utilize various tools, like routing, for our application

@app.route('/welcome') #a decorator that tells flask what URL should trigger the function that follows
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'

if __name__ == '__main__':
    app.run(debug=True)

    #i am unsure about the two lines above this comment and what their purpose is 
    #i am also unsure about how to use the testing portion for this assignment 
    