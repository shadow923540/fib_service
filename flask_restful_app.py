from flask import Flask
from flask_restful import Api
from fib import FibNum, FibString

app = Flask(__name__)
api= Api(app)

api.add_resource(FibNum, '/fib/<int:fib>')
api.add_resource(FibString, '/fib/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)