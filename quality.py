import numpy as np

np.seterr(all="raise")


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


# ====================================
# multiplication of the quality matrix
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
    return np.array(res, dtype="float64")


# ====================================
quality = {
    "Normal": 1.0,
    "Uncommon": 1.30,
    "Rare": 1.60,
    "Epic": 1.90,
    "Legendary": 2.50,
}

quality_tiers = {"T1": 0.0, "T2": 0.0, "T3": 2.5}  # data for T0, T1 are unknown
productivity_tiers = {"T1": 4.0, "T2": 6.0, "T3": 10.0}


# constructor for the quality/productivity matrix
def new_q(
    quality_amount,
    quality_tier,
    quality_quality,
    productivity_amount,
    productivity_tier,
    productivity_quality,
    additional50percent=False,
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
            quality_quality[:3],
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
            productivity_quality[:3],
        )
    else:
        Pinp = 1.0
        text_P = ""

    if additional50percent:
        Pinp += 0.5

    text = "{}: {}{}".format(quality_amount + productivity_amount, text_Q, text_P)
    res = np.zeros((5, 5), dtype="float64")

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
    return {"text": text, "matrix": res}


def get_q_list(number_of_modules, tier, q_quality, additional50percent):
    q_list = []
    for q in range(0, number_of_modules + 1):
        for p in range(0, number_of_modules + 1):
            if q + p <= number_of_modules and q + p > 0:
                q_list.append(
                    new_q(q, tier, q_quality, p, tier, q_quality, additional50percent)
                )
    return q_list


def get_q_list_Qonly(number_of_modules, tier, q_quality, additional50percent):
    q_list = []
    for q in range(0, number_of_modules + 1):
        q_list.append(new_q(q, tier, q_quality, 0, "", "", additional50percent))
    return q_list


# ====================================
# q_level - required output quality 0...4
def get_the_ratio(x0, q_level, q_list, debug=False, koeff=1.0):
    mask_recycler = np.ones(5, dtype="float64")
    mask_out = np.zeros(5, dtype="float64")
    for i in range(5):
        if i >= q_level:
            mask_recycler[i] = 0
            mask_out[i] = 1.0
    # print_line("mask_recycler", mask_recycler)
    # print_line("mask_out     ", mask_out)

    tic = -1
    x1 = np.zeros(5, dtype="float64")
    xout_0 = np.zeros(5, dtype="float64")
    while True:
        tic += 1
        try:
            x10 = (x0 + x1) / koeff  # assembly machine
            x2 = mul_q(x10, q_list[0]["matrix"])  # Q1
            x3 = x2 * 0.25 * koeff * mask_recycler  # recycler + sorting
            x12 = mul_q(x3, q_list[1]["matrix"])  # Q2
            x1 = x12 * mask_recycler  # sorting
            xout = (x2 + x12) * mask_out  # sorting
        except FloatingPointError:
            raise Exception("Positive feedback! The generator!")

        # has "xout" changed in the last tick?
        if abs(xout_0[q_level] - xout[q_level]) <= 0.000001 and tic > 99:
            break
        else:
            xout_0 = xout

    if debug:
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q1["text"]))
        print("q2 (recycler) = {}".format(q2["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0, "{:12.4f}".format(sum(x0)))
        print_line("x1 = ", x1)
        print_line("x10= ", x10)
        print_line("x2 = ", x2)
        print_line("x3 = ", x3)
        print_line("x12= ", x12)
        print_line("x1 = ", x1)
        print_line("xout ", xout)

    return xout


def get_the_ratio_v2(x0, q_level, q_list, debug=True, koeff=1.0):
    out = get_the_ratio(x0, q_level, q_list, False, koeff)
    if out[q_level] > 0:
        x0 /= out[q_level]
        out = get_the_ratio(x0, q_level, q_list, debug, koeff)
    return {"x0": x0, "out": out}


# ====================================
def make_a_complete_search(x0, q_list, q_level_list, koeff=1.0):
    def print_res(res, q_level):
        for r in sorted(res, key=lambda elem: elem[0][0]):
            print(
                "in:{:12.4f} out:{:>5.2f} assembly machine = {:<27s} recycler = {:<27s}".format(
                    r[0][0], r[1][q_level], r[2], r[3]
                )
            )

    res = [[], [], [], [], []]
    for q_level in q_level_list:
        for q1 in range(len(q_list[0])):
            for q2 in range(len(q_list[1])):
                out = get_the_ratio_v2(
                    list(x0), q_level, [q_list[0][q1], q_list[1][q2]], False, koeff
                )
                if abs(out["out"][q_level] - 1.0) <= 0.1:
                    res[q_level].append(
                        [
                            out["x0"],
                            out["out"],
                            q_list[0][q1]["text"],
                            q_list[1][q2]["text"],
                        ]
                    )
                else:
                    print(
                        "\t{} {} -> out = {}".format(
                            q_list[0][q1]["text"],
                            q_list[1][q2]["text"],
                            out["out"][q_level],
                        )
                    )

        print()
        print("==================")
        print("q_level = {}".format(q_level))
        print()
        print_res(res[q_level], q_level)
    return res


q = "Normal"
# q = "Uncommon"
# q = "Rare"
# q = "Epic"
# q = "Legendary"

print()
print("==================")
print("furnace")
print()
x0 = new_q(3, "T3", q, 0, "", "", False)["matrix"][0]
print_line("", x0)
make_a_complete_search(
    x0,
    [get_q_list(2, "T3", q, False), get_q_list_Qonly(4, "T3", q, False)],
    (1, 2),
)

print()
print("==================")
print("assembly machine")
print()
make_a_complete_search(
    [1.0, 0, 0, 0, 0],
    [get_q_list(4, "T3", q, False), get_q_list_Qonly(4, "T3", q, False)],
    (1, 2),
)

# make_a_complete_search(
#     get_q_list(5, "T3", "Legendary", True),
#     get_q_list_Qonly(4, "T3", "Legendary", False),
# )


# print()
# print("==================")
# print(new_q(3, "T3", "Normal", 0, "", "", False))
