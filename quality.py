import numpy as np


def print_line(text, inp):
    print(text, "".join("{:12.4f}".format(t) for t in inp))


def print_q(a):
    print(a["text"])
    q = a["matrix"]
    print("  ", "".join("{:^12s}".format(t) for t in ("q1", "q2", "q3", "q4", "q5")))
    print_line("q1", q[0])
    print_line("q2", q[1])
    print_line("q3", q[2])
    print_line("q4", q[3])
    print_line("q5", q[4])


def mul_q(inp, q):
    if len(inp) != 5:
        raise Exception("len(inp) != 5")

    if len(q) != 5 or len(q[0]) != 5:
        raise Exception("len(q) != 5")

    res = [0, 0, 0, 0, 0]
    tq = np.transpose(q)

    for i in range(5):
        res[i] = sum(inp * tq[i])

    # print_line("res = ", res)
    return np.array(res)


quality = {
    "Normal": 1.0,
    "Uncommon": 1.30,
    "Rare": 1.60,
    "Epic": 1.90,
    "Legendary": 2.50,
}

quality_tiers = {"T1": 0.0, "T2": 0.0, "T3": 2.5}
productivity_tiers = {"T1": 4.0, "T2": 6.0, "T3": 10.0}


def new_q(
    quality_amount,
    quality_tier,
    quality_quality,
    productivity_amount,
    productivity_tier,
    productivity_quality,
):
    if quality_amount > 0:
        Qinp = (
            quality_amount
            * quality_tiers[quality_tier]
            / 100.0
            * quality[quality_quality]
        )
        text_Q = "{}xQ-{}'{}' ".format(
            quality_amount,
            quality_tier,
            quality_quality,
        )
    else:
        Qinp = 0
        text_Q = ""
    if productivity_amount > 0:
        Pinp = (
            1.0
            + productivity_amount
            * productivity_tiers[productivity_tier]
            / 100.0
            * quality[productivity_quality]
        )
        text_P = "{}xP-{}'{}' ".format(
            productivity_amount,
            productivity_tier,
            productivity_quality,
        )
    else:
        Pinp = 1.0
        text_P = ""

    text = "{}: {}{}".format(quality_amount + productivity_amount, text_Q, text_P)
    res = np.zeros((5, 5))

    res[0][1] = Qinp
    res[0][2] = Qinp * 0.1
    res[0][3] = Qinp * 0.01
    res[0][4] = Qinp * 0.001
    res[0][0] = 1 - sum(res[0])

    res[1][2] = Qinp
    res[1][3] = Qinp * 0.1
    res[1][4] = Qinp * 0.01
    res[1][1] = 1 - sum(res[1])

    res[2][3] = Qinp
    res[2][4] = Qinp * 0.1
    res[2][2] = 1 - sum(res[2])

    res[3][4] = Qinp
    res[3][3] = 1 - sum(res[3])

    res[4][4] = 1

    res *= Pinp
    # print_q(res)
    return {"text": text, "matrix": res}


q4 = new_q(4, "T3", "Normal", 0, "", "")
q4Leg = new_q(4, "T3", "Legendary", 0, "", "")
p4 = new_q(0, "", "", 4, "T3", "Normal")
q1p3 = new_q(1, "T3", "Normal", 3, "T3", "Normal")

print()
print("==================")
print_q(q4)

print()
print("==================")
print_q(q4Leg)

print()
print("==================")
print_q(p4)

print()
print("==================")
print_q(q1p3)


def get_the_ratio(x0, q_level, q1, q2, debug=False):
    mask_recycler = np.ones(5)
    mask_out = np.zeros(5)
    for i in range(5):
        if i >= q_level:
            mask_recycler[i] = 0
            mask_out[i] = 1
    # print_line("mask_recycler", mask_recycler)
    # print_line("mask_out     ", mask_out)

    tic = -1
    x1 = np.zeros(5)
    xout_0 = np.zeros(5)
    while True:
        tic += 1
        x10 = x0 + x1  # assembly machine
        x2 = mul_q(x10, q1["matrix"])  # Q1
        x3 = x2 * 0.25 * mask_recycler  # recycler + sorting
        x12 = mul_q(x3, q2["matrix"])  # Q2
        x1 = x12 * mask_recycler  # sorting
        xout = (x2 + x12) * mask_out  # sorting

        # has "xout" changed in the last tick?
        if np.array_equal(xout_0, xout):
            break
        else:
            xout_0 = xout

    if debug:
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q1["text"]))
        print("q2 (recycler) = {}".format(q2["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0)
        print_line("x1 = ", x1)
        print_line("x10= ", x10)
        print_line("x2 = ", x2)
        print_line("x3 = ", x3)
        print_line("x12= ", x12)
        print_line("x1 = ", x1)
        print_line("xout ", xout)

    return xout


def get_the_ratio_v2(x0, q_level, q1, q2):
    out = get_the_ratio(x0, q_level, q1, q2)
    x0 /= out[q_level]
    out = get_the_ratio(x0, q_level, q1, q2, True)


print()
print("==================")
print("")
print()


q_level = 1
out = get_the_ratio_v2([1.0, 0, 0, 0, 0], q_level, q4, q4)
out = get_the_ratio_v2([1.0, 0, 0, 0, 0], q_level, q4Leg, q4Leg)
out = get_the_ratio_v2([1.0, 0, 0, 0, 0], q_level, p4, q4)

