import numpy as np
from itertools import product

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


class scheme_1:
    """assembly machine + recycler"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.mask_recycler = np.ones(5, dtype="float64")
        self.mask_out = np.zeros(5, dtype="float64")
        for i in range(5):
            if i >= q_level:
                self.mask_recycler[i] = 0
                self.mask_out[i] = 1.0

    def calc(self, x0, q_list):
        self.x10 = x0 + self.x1  # assembly machine
        self.x2 = mul_q(self.x10, q_list[0]["matrix"])  # Q1
        self.x3 = self.x2 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x12 = mul_q(self.x3, q_list[1]["matrix"])  # Q2
        self.x1 = self.x12 * self.mask_recycler  # sorting
        self.xout = (self.x2 + self.x12) * self.mask_out  # sorting
        return self.xout

    def print(self, x0, q_list, tic):
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q_list[0]["text"]))
        print("q2 (recycler) = {}".format(q_list[1]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0, "{:12.4f}".format(sum(x0)))
        print_line("x1 = ", self.x1)
        print_line("x10= ", self.x10)
        print_line("x2 = ", self.x2)
        print_line("x3 = ", self.x3)
        print_line("x12= ", self.x12)
        print_line("x1 = ", self.x1)
        print_line("xout ", self.xout)


class scheme_2:
    """mining drill + assembly machine + recycler"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.mask_recycler = np.ones(5, dtype="float64")
        self.mask_out = np.zeros(5, dtype="float64")
        for i in range(5):
            if i >= q_level:
                self.mask_recycler[i] = 0
                self.mask_out[i] = 1.0

    def calc(self, x0, q_list):
        self.x01 = mul_q(x0, q_list[0]["matrix"])  # Q0 - mining drill
        self.x10 = self.x01 + self.x1  # assembly machine
        self.x2 = mul_q(self.x10, q_list[1]["matrix"])  # Q1
        self.x3 = self.x2 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x12 = mul_q(self.x3, q_list[2]["matrix"])  # Q2
        self.x1 = self.x12 * self.mask_recycler  # sorting
        self.xout = (self.x2 + self.x12) * self.mask_out  # sorting
        return self.xout

    def print(self, x0, q_list, tic):
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q_list[0]["text"]))
        print("q2 (recycler) = {}".format(q_list[1]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0)
        print_line("x01 = ", self.x01)
        print_line("x1 = ", self.x1)
        print_line("x10= ", self.x10)
        print_line("x2 = ", self.x2)
        print_line("x3 = ", self.x3)
        print_line("x12= ", self.x12)
        print_line("x1 = ", self.x1)
        print_line("xout ", self.xout)


# ====================================
# q_level - required output quality 0...4
def get_the_ratio(x0, scheme, q_level, q_list, debug):
    scheme.clear(q_level)

    tic = -1
    xout_last = np.zeros(5, dtype="float64")
    while True:
        tic += 1
        try:
            xout = scheme.calc(x0, q_list)
        except FloatingPointError:
            raise Exception("Positive feedback! The generator!")

        # has "xout" changed in the last tick?
        if abs(xout_last[q_level] - xout[q_level]) <= 0.000001 and tic > 99:
            break
        else:
            xout_last = xout

    if debug:
        scheme.print(x0, q_list, tic)

    return xout


def get_the_ratio_v2(x0, scheme, q_level, q_list, debug):
    out = get_the_ratio(x0, scheme, q_level, q_list, False)
    if out[q_level] > 0:
        x0 /= out[q_level]
        out = get_the_ratio(x0, scheme, q_level, q_list, debug)
    return {"x0": x0, "out": out}


# ====================================
def make_a_complete_search(x0, scheme, name_of_the_machines, q_list, q_level_list):
    def print_res(res, q_level):
        for r in sorted(res, key=lambda elem: elem[0][0]):
            print("in:{:12.4f} out:{:>5.2f} {:}".format(r[0][0], r[1][q_level], r[2]))

    res = [[], [], [], [], []]
    for q_level in q_level_list:
        for q in product(*q_list):
            out = get_the_ratio_v2(list(x0), scheme, q_level, q, False)
            if abs(out["out"][q_level] - 1.0) <= 0.1:
                list_of_machines = ""
                for i in range(len(q)):
                    list_of_machines += " {} = {:<27s}".format(
                        name_of_the_machines[i], q[i]["text"]
                    )
                res[q_level].append([out["x0"], out["out"], list_of_machines])
            else:
                print(
                    "\t{} -> out = {}".format(
                        "".join("{:<27s}".format(t["text"]) for t in q),
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
print("mining drill + furnace")
print()
make_a_complete_search(
    [1.0, 0, 0, 0, 0],
    scheme_2(),
    ("mining drill", "furnace", "recycler"),
    [
        get_q_list_Qonly(3, "T3", q, False),
        get_q_list(2, "T3", q, False),
        get_q_list_Qonly(4, "T3", q, False),
    ],
    q_level_list=(1, 2),
)

print()
print("==================")
print("assembly machine")
print()
make_a_complete_search(
    [1.0, 0, 0, 0, 0],
    scheme_1(),
    ("assembly machine", "recycler"),
    [get_q_list(4, "T3", q, False), get_q_list_Qonly(4, "T3", q, False)],
    q_level_list=(1, 2),
)

# make_a_complete_search(
#     get_q_list(5, "T3", "Legendary", True),
#     get_q_list_Qonly(4, "T3", "Legendary", False),
# )


# print()
# print("==================")
# print(new_q(3, "T3", "Normal", 0, "", "", False))

# get_the_ratio(
#     [30.2777, 0, 0, 0, 0],
#     scheme_2(),
#     1,
#     (
#         new_q(0, "", "", 0, "", "", False),
#         new_q(1, "T3", "Normal", 0, "", "", False),
#         new_q(0, "", "", 0, "", "", False),
#     ),
#     True,
# )
