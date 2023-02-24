#Count Odd Numbers in an Interval Range
#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

low=3
high=7
if low % 2==1:
    low -=1
if high % 2==1:
    high +=1

print((high-low)//2)

# if low % 2 == 0:

#     print((high-low+1)//2)
#     print((high-low)//2+1)

    # return (high-low+1)//2
    #  return (high-low)//2 + 1
