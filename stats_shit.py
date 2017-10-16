#!/usr/bin/env python3
import sys
import statistics as stats

def main(num_txt_file):
    with open(num_txt_file) as f:
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
        print('Sorted Data: {}'.format(' '.join(map(str, sorted(numlst)))))
        print('Mean: {0:.4f}'.format(mean))
        print('Median: {0:.4f}'.format(median))
        print('Standard Variance: {0:.4f}'.format(stdvar))
        print('Standard Deviation: {0:.4f}'.format(stddev))
        print('Sum(Xi): {0:.4f}'.format(total))
        print('Sum(Xi^2): {0:.4f}'.format(totsq))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} /path/to/num_set.txt'.format(sys.argv[0]), file=sys.stderr)
        exit(1)
    else:
        main(sys.argv[1])
        exit(0)
