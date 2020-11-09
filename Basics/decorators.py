
def div(a,b):   #Main function not to be changed
    print(a/b)

def smart_div(func): #decorator or extending the Div function outside the function
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1=smart_div(div)
div1(2,4)