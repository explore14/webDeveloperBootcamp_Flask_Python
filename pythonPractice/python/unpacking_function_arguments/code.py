def mul(*args):
    total=1
    for arg in args:
        total=total*arg
    
    return total

def apply(*arg,operator):
    if operator=='+':
      return sum(arg)
    elif operator=='*':
        return mul(*arg)
    else:
        return "Invalid operator"
    
print(apply(1,2,3,4,operator='+'))

#####################################

#2
def named(**kwargs):
    print(kwargs)

details={"name":"Bob","age":25}
named(**details)

#3
def both(*args,**kwargs):
    print(args)
    print(kwargs)

both( 1,  2,3,name="Bob",age=25) 

#Use case example:
"""
def post(url,data=None,json=None,**kwargs):
    return request('post',url,data=data,json=json,**kwargs)
"""

