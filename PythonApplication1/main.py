import numpy as np
import multi
import module1
import sys
 
def func(a,b):
    result=np.sqrt(multi.multiplication(int(a),int(b)))
    return result

def func1(a,b):
    result=np.sqrt(module1.TFadd(int(a),int(b)))
    return result
 
 
if __name__ == '__main__':
    #print(func(sys.argv[1],sys.argv[2]))
    #print(func1(sys.argv[1],sys.argv[2]))
    print(func1(1,2))

