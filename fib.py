from flask_restful import Resource
import functools

@functools.lru_cache(None)
def calculate_fibonacci(n):
    if n < 2:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

class FibNum(Resource):
    def get(self, fib):
        try:
            if fib <= 1:
                return fib
            else:
                return calculate_fibonacci(fib - 1) + calculate_fibonacci(fib - 2)
            return {'message': 'Something wrong'}, 404
        except RecursionError:
            return 'Please put smaller value to calculate fibonacci number to avoid Recursion Error', 400


class FibString(Resource):
    def get(self, name):
        return 'Wrong value: '+ name + '.  Please create endpoint with correct int value for fibonacci calculation', 404