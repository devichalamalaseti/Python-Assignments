'''We are making n stone piles! The first pile has n stones. If n is
even, then all piles have an even number of stones. If n is odd, all
piles have an odd number of stones. Each pile must have more
stones than the previous pile but as few as possible. Write a
Python program to find the number of stones in each pile.
Sample Input: n = 7
Sample Output: Stones in a single pile = [2, 4, 6] '''

def stones(s):
    pile=[]
    if s%2==0:
        stn=2
    else:
        stn=1
        while s>0:
            pile.append(stn)
            s-=stn
            stn+=2
    return pile
s=7
pile=stones(s)
print("No of stones in each pile:",pile)