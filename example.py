# calculate simple interest 
def simple_interest(p:float|int,n:int,r:float|int) ->tuple:
    """ p:principle in INR
    n :no of years
    r :rate of interest in percent per annum
    output interest ,amount"""
    i=(p*n*r)/100
    a=p+i
    return i,a

# take p,n ,r as input from user
p=float(input("please enter principl in INR:"))
n=int(input("please enter no of years:"))
r=float(input("please enter rate of interest in %p.a:"))

#call the simple interest function
i,a =simple_interest (p,n,r)

# print the interest and amount
print(f"simple Interest :{i:.2f} INR")
print(f"Amount : {a:.2f} INR")
