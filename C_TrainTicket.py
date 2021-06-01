n = input()
op_cnt = len(n) - 1  # Number of op

for i in range(2**op_cnt):  # The total number may or may not include the op.
    op = ["-"] * op_cnt
    for j in range(op_cnt):
        if ((i >> j) & 1):
            # Overwrite the flagged location with "+".
            op[op_cnt - 1 - j] = "+"
    formula = ""
    for p_n, p_o in zip(n, op + [""]):
        formula += (p_n + p_o)
    if eval(formula) == 7:
        print(formula + "=7")
        break
