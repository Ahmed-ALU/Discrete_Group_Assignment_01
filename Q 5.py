x = [ 20, 40, 60, 80, 80]
y = [ 3, 4]
print("X = ", x)
print("Y = ", y)
Value = bool(True)

for numy in y: # There is exists Y that ....
    if Value == False:
            break
    for numx in x: # for all of X ...
        if numx%numy == 0: #The condition
            Value = True
        else:
            Value = False # IF there is only one value of x that is false, the condition is false
            break
        
                    

if Value == True:
    print("The condition Y|X is True")
else: 
    print("The condition is False")