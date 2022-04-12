import library
import numpy as np
import matplotlib.pyplot as plt


#Q1
def Q1():
    #importing
    x,y=np.loadtxt('/home/ws3/Desktop/rahul/P452/Q1.txt',unpack=True)

    #fitting
    X ,inv = library.polynomial_fit(x,y,4)
    fit = []

    #generating fitted points
    for i in range(len(x)):
        fit.append(X[3]*(x[i]**3) + X[2]*(x[i]**2) + X[1]*(x[i]**1) +X[0])

    sum = 0
    for i in range(len(y)):
        sum+= (y[i] - fit[i])**2
    sum = sum**0.5

    print(f'cubic coefficients are {X}')
    print(f'least square error is  = {sum}')

    plt.plot(x,y,'.')
    plt.plot(x,fit)
    plt.savefig('normal_fit.png')

Q1()

#cubic coefficients are [0.5770238673498951, 4.6976757145595, -11.060931165172533, 7.625785656722557]
#least square error is  = 0.19279438310417016

#Q2
def Q2(a,m):
    # defining parameters
    x0x =39
    x0y =19
    circle=0
    total =0
    a = a
    m=m
    #loop to calculate random points
    for i in range(10000):
        rand_no_x = library.random_no_gen(x0x,a,m)
        rand_no_y = library.random_no_gen(x0y,a,m)
        x0x = rand_no_x*m
        x0y = rand_no_y*m
        r =(rand_no_x**2+rand_no_y**2)**0.5
        # check if point lies in unit circle
        if(r <= 1):
            circle+=1
            total+=1
        else:
            total+=1    
    result = circle*4/total

    print(f'result using throwing points is {result} for a = {a} and m ={m}')

    #function for monte carlo
    def xfunction(x):
        return (1-x**2)**0.5

    integration = library.montecarlo(xfunction,0,1,100000,21,a,m)
    result = integration*4
    print(f'result using monte carlo is {result} for a = {a} and m ={m}')

Q2(65,1021)
Q2(572,16381)

#result using throwing points is 3.14 for a = 65 and m =1021
#result using monte carlo is 3.9999976520175857 for a = 65 and m =1021
#result using throwing points is 3.116 for a = 572 and m =16381
#result using monte carlo is 3.9999871835636314 for a = 572 and m =16381



#Q3

def Q3():

    #Volume function for Steinmetz solid,

    def  SS_volume(x):
        r=1
        return 4*(r**2-x**2)

    integration = library.montecarlo(SS_volume,-1,1,100000,19,65,1021)
    #Actual volume for comarision
    actual_volume =16/3 
    print(f'Volume with monte carlo is {integration} and actual result is {actual_volume}' )

Q3()
#Volume with monte carlo is 5.751650908866749e-05 and actual result is 5.333333333333333

