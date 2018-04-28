#wap function that accepts a group of numbers and returns the sum and avg
def sum_avg(lst):
    n=len(lst)
    s=sum(lst)
    a=s/n
    return s,a
lst=[float(x) for x in input("enter no: ").split(',')]
a,b=sum_avg(lst)
print('sum={:.2f}\nAverage={:.2f}'.format(a,b))
