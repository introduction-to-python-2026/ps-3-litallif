def approximate_pi(n_terms):
    sum=0
    for i in range(n_terms):
        sum=sum+(-1)**i/(2*i+1)
        return 4*sum
