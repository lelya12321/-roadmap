def sum_of_digits(digits):
    # your code here
    if digits == None:
        return ''

    else:

        ft = ' + '.join([str(k) for k in str(digits)])
        sum__ = sum(int(cc) for cc in str(digits))
        return ('{} = {}'.format(ft, sum__))