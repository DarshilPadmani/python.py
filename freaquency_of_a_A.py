# Write a program to count the frequency of letter ‘a’/’A’ in the input string. 

arr = 'Darshil'
count = 0
for i in arr:
    if i == 'a' or i == 'A':
        count+=1
print(count)