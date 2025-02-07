'''Finding nth fibonacci number'''
'''Using loop'''
def fib_loop(n):
    prev2 = 0
    prev1 = 1
    for c in range(2,n):
        nu = prev2+prev1
        prev2=prev1
        prev1=nu
    print(prev1)
'''0 1 1 2 3 5 8'''

'''using recursion'''
def fib_recur(n, prev1=1, prev2=0):
    global count
    if n>=0:
       tem = prev1+prev2
       prev2=prev1
       prev1 = tem
       return fib_recur(n-2, prev1, prev2)
    else :
        print(prev1)
'''using formula f(n)=f(n-1)+f(n-2)'''
mem=[]
def fib_formu(n):
    if n-1==0:
        return 0
    elif n-1==1:
        return 1
    else :
        return fib_formu(n-1)+fib_formu(n-2)
    
'''optimized solution for fibanocci series'''
mem=[0,1]
def rec_opt_fib(n):
    print(n)
    global mem
    if n<=len(mem):
        return mem[n-1];
    mem.append(rec_opt_fib(n-2)+rec_opt_fib(n-1))
    print(n)
    print(mem)
    return mem[n-1]



if __name__=='__main__':
    n=rec_opt_fib(int(input('Enter the term:\n')))
    if n :
        print(n)
