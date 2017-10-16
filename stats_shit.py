from math import sqrt

def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0

with open('nums.txt') as f:
    nums = f.read().split()
    numlst = list(float(num) for num in nums)

    n = len(numlst)
    total = sum(numlst)
    totsq = sum(num**2 for num in numlst)
    med = median(numlst)
    mean = total/n
    stdvar = (totsq - ((total**2)/n))/(n - 1)
    stddev = sqrt(sum((num-mean)**2 for num in numlst)/(n-1))

    print('n = {}'.format(n))
    print('Sorted Data: {}'.format(' '.join(sorted(numlst))))
    print('Mean: {0:.4f}'.format(mean))
    print('Median: {0:.4f}'.format(med))
    print('Standard Variance: {0:.4f}'.format(stdvar))
    print('Standard Deviation: {0:.4f}'.format(stddev))
    print('Sum(Xi): {0:.4f}'.format(total))
    print('Sum(Xi^2): {0:.4f}'.format(totsq))
