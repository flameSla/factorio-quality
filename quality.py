import numpy as np
from itertools import product

from modules import mul_q
from modules import new_q
from modules import get_q_list
from modules import get_q_list_Qonly
from modules import get_q_list_Ponly

from utilities import print_line
from utilities import print_q

from schemes import scheme_1
from schemes import scheme_2


np.seterr(all="raise")


# ====================================
# q_level - required output quality 0...4
def get_the_ratio_v2(x0, scheme, q_level, q_list, debug, log=False):
    def get_the_ratio(x0, scheme, q_level, q_list, debug, log):
        scheme.clear(q_level)

        tic = -1
        xout_last = np.zeros(5, dtype="float64")
        while True:
            tic += 1
            if log and tic < 30:
                scheme.print0(x0, q_list, tic)
            try:
                xout = scheme.calc(x0, q_list)
            except FloatingPointError:
                raise Exception("Positive feedback! The generator!")

            if log and tic < 30:
                scheme.print1(x0, q_list, tic)

            # has "xout" changed in the last tick?
            if abs(xout_last[q_level] - xout[q_level]) <= 0.000001 and tic > 99:
                break
            else:
                xout_last = xout

        if debug:
            scheme.print0(x0, q_list, tic)
            scheme.print1(x0, q_list, tic)

        return xout

    out = get_the_ratio(x0, scheme, q_level, q_list, False, False)
    if out[q_level] > 0:
        x0 /= out[q_level]
        out = get_the_ratio(x0, scheme, q_level, q_list, debug, log)
    return {"x0": x0, "out": out}


# ====================================
def make_a_complete_search(x0, scheme, name_of_the_machines, q_list, q_level_list):
    s_level = [x > 0 for x in x0].index(True)

    def print_res(res, q_level):
        # max_word = max(words, key=len)
        for i, r in enumerate(sorted(res, key=lambda elem: elem[0][s_level])):
            print(
                "{:5d} in:{:12.4f} out:{:>5.2f} {:}".format(
                    i, r[0][s_level], r[1][q_level], r[2]
                )
            )
            if i > 10:
                print("  ...")
                break

    res = [[], [], [], [], []]
    for q_level in q_level_list:
        for q in product(*q_list):
            out = get_the_ratio_v2(list(x0), scheme, q_level, q, False)
            if abs(out["out"][q_level] - 1.0) <= 0.1:
                res[q_level].append(
                    [
                        out["x0"],
                        out["out"],
                        "".join(
                            " {} = {:<27s}".format(a, b["text"])
                            for a, b in zip(name_of_the_machines, q)
                        ),
                    ]
                )
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
    ("drill", "furn", "rec", "machine"),
    [
        get_q_list_Qonly(3, "T3", q, False),
        get_q_list(2, "T3", q, False),
        get_q_list_Qonly(4, "T3", q, False),
        get_q_list_Ponly(4, "T3", q, False),
    ],
    q_level_list=[1, 2],
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
    q_level_list=[1, 2],
)

# make_a_complete_search(
#     get_q_list(5, "T3", "Legendary", True),
#     get_q_list_Qonly(4, "T3", "Legendary", False),
# )


# print()
# print("==================")
# print(new_q(3, "T3", "Normal", 0, "", "", False))

q = "Normal"
q = "Rare"
m = new_q(4, "T3", "Normal", 0, "", "", False)
get_the_ratio_v2(
    [1, 0, 0, 0, 0],
    scheme_2(),
    4,
    (
        new_q(3, "T3", q, 0, "", "", False),
        new_q(2, "T3", q, 0, "", "", False),
        new_q(4, "T3", q, 0, "", "", False),
        new_q(0, "", "", 4, "T3", q, False),
    ),
    True,
    log=False,
)

m = new_q(4, "T3", q, 0, "", "", False)
get_the_ratio_v2(
    [1, 0, 0, 0, 0],
    scheme_2(),
    1,
    (
        new_q(3, "T3", q, 0, "", "", False),
        new_q(0, "", "", 2, "T3", q, False),
        new_q(0, "", "", 0, "", "", False),
        new_q(0, "", "", 4, "T3", q, False),
    ),
    True,
    log=False,
)

m = new_q(4, "T3", q, 0, "", "", False)
get_the_ratio_v2(
    [1, 0, 0, 0, 0],
    scheme_2(),
    1,
    (
        new_q(3, "T3", q, 0, "", "", False),
        new_q(0, "", "", 2, "T3", q, False),
        new_q(4, "T3", q, 0, "", "", False),
        new_q(0, "", "", 4, "T3", q, False),
    ),
    True,
    log=False,
)
