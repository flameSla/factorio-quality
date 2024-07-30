# ====================================
def print_line(text, inp, end=""):
    print(text, "".join("{:12.4f}".format(t) for t in inp), end)


def print_q(a):
    print(a["text"])
    q = a["matrix"]
    print("  ", "".join("{:^12s}".format(t) for t in ("q1", "q2", "q3", "q4", "q5")))
    print_line("q1", q[0])
    print_line("q2", q[1])
    print_line("q3", q[2])
    print_line("q4", q[3])
    print_line("q5", q[4])


def print_mat5x5(a):
    for i in range(len(a)):
        print_line("q{}".format(i), a[i])


######################################
#
# main
if __name__ == "__main__":
    pass
