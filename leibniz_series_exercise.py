def approximate_pi():
    n_terms = int(input("how many numbers?"))
    list_of_numbers = []
    for i in range(n_terms):
        list_of_numbers.append((-1)**i/(2*i+1))
    pi = sum(list_of_numbers) * 4
    return pi
approximate_pi()
