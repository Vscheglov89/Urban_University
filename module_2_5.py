def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n + 1):
        lst = []
        matrix.append(lst)
        for j in range(1, m + 1):
            lst.append(value)
    print(matrix)
get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)
