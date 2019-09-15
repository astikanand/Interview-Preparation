# Q1. We have an interface named Logger which contains two functions:

# startReq( req Id, start time )

# finishReq( req Id, end time )

# Logger gets a large number of requests with the start time. These requests are sent to startReq function.
# After the request finishes, we invoke the function finishReq. 
# We should be able to print the output containing the finished requests sorted by start time.

# Request ID  Start Time     End Time
# A             0              25
# B             4              18
# C             2              20
# D             7              10

# We need output as:
# A 0 25
# C 2 20
# B 4 18
# D 7 10

def sort_request(requests):
    requests.sort(key=lambda k: (k[1], k[2]))
    
    for request in requests:
        print("{} {} {}".format(request[0], request[1], request[2]))

sort_request([("A", 0, 25), ("B", 4, 18), ("C", 2, 20), ("D", 7, 10)])
