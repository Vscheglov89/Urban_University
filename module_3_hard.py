def calculate_structure_sum(*data_structure):
    sum_num = 0
    sum_len = 0

    def calc(m):
        nonlocal sum_num, sum_len
        if isinstance(m, int):
            sum_num += m
        if isinstance(m, str):
            sum_len += len(m)
        if isinstance(m, (list, tuple, set)):
            for sub_item in m:
                calc(sub_item)
        if isinstance(m, dict):
            for key, value in m.items():
                calc(key)
                calc(value)

    calc(data_structure)
    return sum_num, sum_len


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


sum_num, sum_len = calculate_structure_sum(data_structure)
print(sum_num + sum_len)