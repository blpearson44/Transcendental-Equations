# Written by Ben Pearson
# V0.0.1
# This function will implement the main iterations and be responsible for delivering results

# Modules
import functions as f
import constants as c
x = 4

print("Functional Iteration: x = " + str(x))
for i in range(c.N):
    x = f.func_itor(f.gx, x) 
    print("x =\t" + str(x))
    
x = 2
print("Newton's Method")
for i in range(c.N):
    x = f.newton(f.fx, f.dfx, x) 
    print("x =\t" + str(x))
