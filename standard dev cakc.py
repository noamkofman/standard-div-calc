import math
num_input = input("Enter your numbers and I will give the stadard deviation (**seperate with commas**) : ")
numbers = num_input.split(',')
# below we convert every num which we split by the comma (done above ^) into an integer (done below)
converted_num = [int(num) for num in numbers]
sum1 = (sum(converted_num))
sum_sqaurediff = 0
mean = sum1/ len(numbers)
len_num = len(converted_num)
while len_num != 0:
    len_num -= 1
    # above we have a loop based on length of inputed numbers below we acess the correspooding value that goes with the len 
    index_value = converted_num[len_num] 
    num_squared = (index_value - mean) ** 2
    sum_sqaurediff += num_squared
final_sol = (math.sqrt(sum_sqaurediff / len(converted_num)))
print(final_sol)

   
    # print(converted_num)
    
  

   