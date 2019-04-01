import numpy as np
import multi
import sys
 
def func(a,b):
    result=np.sqrt(multi.multiplication(int(a),int(b)))
    return result
 
 
if __name__ == '__main__':
    print(func(sys.argv[1],sys.argv[2]))
    #print(func(1,2))

