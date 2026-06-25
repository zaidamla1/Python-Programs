# function without params without return

#1. declaration
def greet():
    print("Welcome to Python batch")

#2. calling

#function with param without return

def addTwoNums(n1,n2):
    total = n1 + n2
    print("total is",total,sep=" $ ")


def printNums(start,end):
    while start <= end:
        print(start,end=" ")
        start+=1

#function without params with return

def getEmpId():
    empId = "Emp001"
    return empId;



#function with params with return

def fibonacciSeries(n):
    a = 0
    b = 1
    fibSeries = []
    for i in range(1,n+1):
        c = a + b
        fibSeries.append(a)
        a = b
        b = c        
    return fibSeries

print(__name__)

if __name__ == "__main__":
    greet()
    addTwoNums(10,20)
    printNums(10,20)
    print()
    empid = getEmpId()
    print(empid)
    fibonacci = fibonacciSeries(5)
    print(fibonacci)
