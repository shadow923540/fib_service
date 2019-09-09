from flask_restful import Resource
import functools

@functools.lru_cache(None)
def fibb(n):
    if n < 2:
        return n
    return fibb(n-1) + fibb(n-2)

class FibNum(Resource):
    def get(self, fib):
        try:
            if fib <= 1:
                return fibb
            else:
                return fibb(fib - 1) + fibb(fib - 2)
            return {'message': 'Something wrong'}, 404
        except RecursionError:
            return 'Please put smaller value to calculate fibonacci number to avoid Recursion Error'


class FibString(Resource):
    def get(self, name):
        return 'Wrong value: '+ name + '.  Please create endpoint with correct int value for fibonacci calculation'