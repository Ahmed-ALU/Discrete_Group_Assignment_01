x = [ 20, 40, 60, 80, 80]
y = [ 2, 4]


for numy in y: # There is exists Y that ....
    for numx in x: # for all of X ...
        if numx%numy == 0: #The condition
            Value = True
        else:
            Value = False # IF there is only one value of x that is false, the condition is false
            break

if Value == True:
    print("The condition is True")
else: 
    print("The condition is False")