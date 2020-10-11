z = 2
choices = []
test = []
add = []
x = int(input('The number of prime numbers up to this input: '))
while z <= x:
    choices.append(z)
    z +=1
#---------------------------------------------------------------------    
    
i = 0
while i < len(choices):
    for num in choices:
        choices[i] % num
        test.append(choices[i] % num)
    i += 1
    
#---------------------------------------------------------------------------------

n= x - 1
for i in range(0, len(test), n):
    add.append(test[i:i+n])
    
#---------------------------------------------------------------------

r = 0
while r < len(add):
    g = 0
    for t in add[r]:
        if t == 0:
            g = g + 1
        if g == 1:
            add[r] = 1 
        else:
            add[r] = 0
    r += 1
    
p= 0
while p <= x*2:
    for zeros in add:
        if zeros == 0:
            add.remove(zeros)
    p += 1

len(add)