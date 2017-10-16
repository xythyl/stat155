import statistics as stats

with open('nums.txt') as f:
    nums = f.read().split()
    numlst = list(float(num) for num in nums)

    n = len(numlst)
    total = sum(numlst)
    totsq = sum(num**2 for num in numlst)
    median = stats.median(numlst)
    mean = stats.mean(numlst)
    stdvar = stats.variance(numlst)
    stddev = stats.stdev(numlst)

    print('n = {}'.format(n))
    print('Sorted Data: {}'.format(' '.join(sorted(nums, key=float))))
    print('Mean: {0:.4f}'.format(mean))
    print('Median: {0:.4f}'.format(median))
    print('Standard Variance: {0:.4f}'.format(stdvar))
    print('Standard Deviation: {0:.4f}'.format(stddev))
    print('Sum(Xi): {0:.4f}'.format(total))
    print('Sum(Xi^2): {0:.4f}'.format(totsq))
