from flask import Flask, request
from operations import add, sub, mult, div #we are importing the functions from the operations python file in this folder

app = Flask(__name__)

 #this is associated with the URL path /add and when navigating to that URL, this function should run 
@app.route('/add') #function will be called when we access the /add route
def addition():
    #
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def subtration():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    result = div(a,b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)

    #at this time, the app does not seem to be connecting to the local server 