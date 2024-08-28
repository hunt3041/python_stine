
def fizz_buzz(i):
    
    if i % 3 == 0:
        if i % 5 == 0:
            return 'FizzBuzz'
        else: 
            return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    
    else: 
        return i
    
test_vector = (4, 5, 3, 15, 2, 0)
print('Test Vector: ', test_vector)
print('Output: ', list(map(fizz_buzz, test_vector)))