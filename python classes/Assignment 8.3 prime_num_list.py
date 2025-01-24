# import math

# def prime_num_list(max_range):
#     prime_list = [2]
#     is_prime = True
#     increase = 1
#     last_key = prime_list[len(prime_list)-1]
    
#     while last_key + increase <= max_range:
#         last_key = prime_list[len(prime_list)-1]
#         is_prime = True
        
#         # print(prime_list)
#         # print("increase", increase)
#         # print("last_key", last_key)
        
#         square_root = 3
#         # if not last_key == 2:
#         square_root = int(math.sqrt(last_key + increase))
#         if not square_root > 2:
#             square_root = 3
#         # print("root", square_root)
        
#         for divisor in range(2, square_root+1):
#             if (last_key + increase) % divisor == 0 and not divisor == last_key + increase:
#                 is_prime = False
#                 # print("is_prime", is_prime)
#                 break
            
#         # print("After increase", increase)
#         # print("After last_key", last_key)
            
#         if is_prime:
#             # print("is_prime", is_prime)
#             prime_list.append(last_key + increase)
#             is_prime = True
#             increase = 1
#         else:
#             increase += 1
        
#     print(prime_list)
      
# user_range = 40
# prime_num_list(user_range) import math

# def prime_num_list(max_range):
#     prime_list = [2]
#     is_prime = True
#     increase = 1
#     last_key = prime_list[len(prime_list)-1]
    
#     while last_key + increase <= max_range:
#         last_key = prime_list[len(prime_list)-1]
#         is_prime = True
        
#         square_root = 3
#         square_root = int(math.sqrt(last_key + increase))
#         if not square_root > 2:
#             square_root = 3
#         for divisor in range(2, square_root+1):
#             if (last_key + increase) % divisor == 0 and not divisor == last_key + increase:
#                 is_prime = False
#                 # print("is_prime", is_prime)
#                 break
#             prime_list.append(last_key + increase)
#             is_prime = True
#             increase = 1
#         else:
#             increase += 1
        
#     print(prime_list)

# user_range = 40
# prime_num_list(user_range) 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(2, 101) if is_prime(num)]
print(primes)
