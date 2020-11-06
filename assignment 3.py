# solution 1

dictionary= {"name":"Utkarsh kakadey",
             "age":20,
             "city":"Bhilai"}
print(dictionary)
dictionary["Location"]=dictionary["city"]
del dictionary["city"]

print(dictionary)

# solution 2
def CountFrequency(my_list): 
      
   
   count = {} 
   for i in [11, 45, 8, 11, 23, 45, 23, 45, 89]: 
    count[i] = count.get(i, 0) + 1
   return count 
  

if _name_ == "_main_":  
    my_list =[11, 45, 8, 11, 23, 45, 23, 45, 89] 
    print(CountFrequency(my_list))
    
# solution 3
 
sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sampleList)

sampleList = list(set(sampleList))
print("unique list", sampleList)

tuple = tuple(sampleList)
print("tuple ", tuple)

print("Minimum number is: ", min(tuple))
print("Maximum number is: ", max(tuple))

#solution 4 

def showEmployee(name, salary=50000):
    print("Employee", name, "salary is:", salary)

showEmployee("Ben", 50000)
showEmployee("Ben")

# solution 5 

def outerFun(a, b):
    square = a**2
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result

# solution 6 

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
# solution 7 
def displayStudent(name, age):
    print(name, age)

displayStudent("utkarsh", 20)

# solution 8 
count=0
while (True):
    print("enter your mobile number")
    num = input()
    if len(num) == 10:  # see if number is of 10 digit or not
        count += 1
    else:
        print(f"your number is incorrect doesnot contain 10 digits . contain {len(num)} digits ")

    if num.isdigit():  # check if  number is integer or not
        count += 1
    else:

        print("your number contain characters not numbers")
    if count == 1:
        print("please check the number ")
        count=count-1
    if count== 2:
        print("mobile number is correct ")
        break
        
# solution 9 

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

# solution 10

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
    
    

        
      
