import math

def birthday_paradox_find_n(probability):
    print (math.ceil(math.sqrt(2*365*(math.log(1/(1-probability))))))


print ("Example-1: birthday_paradox_find_n(0.50)")
birthday_paradox_find_n(0.50)

print ("Example-2: birthday_paradox_find_n(0.70)")
birthday_paradox_find_n(0.70)

print ("Example-1: birthday_paradox_find_n(0.99)")
birthday_paradox_find_n(0.99)

print ("Example-1: birthday_paradox_find_n(0.999)")
birthday_paradox_find_n(0.999)
