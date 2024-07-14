import numpy as np
from itertools import product

from modules import mul_q
from modules import new_q
from modules import get_q_list
from modules import get_q_list_Qonly

from utilities import print_line
from utilities import print_q

from schemes import scheme_1
from schemes import scheme_2


np.seterr(all="raise")


# ====================================
# q_level - required output quality 0...4
def get_the_ratio_v2(x0, scheme, q_level, q_list, debug):
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

    out = get_the_ratio(x0, scheme, q_level, q_list, False)
    if out[q_level] > 0:
        x0 /= out[q_level]
        out = get_the_ratio(x0, scheme, q_level, q_list, debug)
    return {"x0": x0, "out": out}


# ====================================
def make_a_complete_search(x0, scheme, name_of_the_machines, q_list, q_level_list):
    def print_res(res, q_level):
        # max_word = max(words, key=len)
        for r in sorted(res, key=lambda elem: elem[0][0]):
            print("in:{:12.4f} out:{:>5.2f} {:}".format(r[0][0], r[1][q_level], r[2]))

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
