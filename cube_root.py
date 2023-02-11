# Write a program to find the cube root of a given number. 

# x = int (input ("Enter a number: ")) 
# y = x**(1/3) 


# print ("Cube Root of ",x , "is", y ) 

cube = int(input("Enter any number : ")) 
# won't work with x < 1 because initial upper bound is less than ans 
 
epsilon = 0.01 
num_guesses = 0 
low = 0 
high = cube 
guess = (high + low)/2.0 
while abs(guess**3 - cube) >= epsilon: 
    if guess**3 < cube:
  # look only in upper half search space 
        low = guess 
        
    else: 
       # look only in lower half search space 
        high = guess 
        # next guess is halfway in search space 
    guess = (high + low)/2.0 
    num_guesses += 1 
print('num_guesses =', num_guesses) 
print(guess, 'is close to the cube root of',cube)