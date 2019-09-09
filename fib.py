from flask_restful import Resource

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

class FibNum(Resource):

    def get(self, fib):
        if fib <= 1:
            return fib
        else:
            return recur_fibo(fib - 1) + recur_fibo(fib - 2)
        return {'message': 'Something wrong'}, 404

