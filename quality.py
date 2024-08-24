import numpy as np
import locale
from itertools import product

from modules import mul_q
from modules import new_q
from modules import get_q_list
from modules import get_q_list_Qonly
from modules import get_q_list_Ponly

from utilities import print_line
from utilities import print_q

from schemes import scheme_1

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
            if abs(xout_last[q_level] - xout[q_level]) <= 0.00000000001:
                if not all([x == 0.0 for x in xout]) or tic > 99:
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
def make_a_complete_search(
    x0,
    scheme,
    name_of_the_machines,
    q_list,
    q_level_list,
    filename,
    show_the_counter=False,
):
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

    i = 0
    locale.setlocale(locale.LC_ALL, "")

    max_i = 1
    for q in q_list:
        max_i *= len(q)
    print("number of combinations = {}".format(max_i))

    min_res = {}
    for q in range(5):
        min_res[q] = {
            "x0": 999999999999999.0,
            "q_level": q,
            "text": "",
            "text_csv": "",
        }
    with open(filename, mode="w", encoding="utf8") as f:
        line = "q_level;x0;out;" + ";".join(
            "{}".format(a) for a in name_of_the_machines
        )
        print(line, file=f)
        for q_level in q_level_list:
            temp_res = {
                "x0": 999999999999999.0,
                "q_level": q_level,
                "text": "",
                "text_csv": "",
            }
            for q in product(*q_list):
                if show_the_counter and i % 1000 == 0:
                    print(i)
                i += 1
                out = get_the_ratio_v2(list(x0), scheme, q_level, q, False)
                if abs(out["out"][q_level] - 1.0) <= 0.1:
                    text_csv = "{};{};{};{}".format(
                        q_level,
                        locale.format_string("%f", out["x0"][s_level]),
                        locale.format_string("%f", out["out"][q_level]),
                        ";".join("{}".format(a["text"]) for a in q),
                    )
                    print(
                        text_csv,
                        file=f,
                    )
                    text = "q={:d} in:{:>12.4f} out:{:>5.2f}".format(
                        q_level, out["x0"][s_level], out["out"][q_level]
                    )
                    text += "".join(
                        " {} = {}".format(a, b["text"])
                        for a, b in zip(name_of_the_machines, q)
                    )
                    temp_res["x0"] = out["x0"][s_level]
                    temp_res["q_level"] = q_level
                    temp_res["text"] = text
                    temp_res["text_csv"] = text_csv

                    if temp_res["x0"] < min_res[q_level]["x0"]:
                        min_res[q_level] = dict(temp_res)

    for q in range(5):
        print(min_res[q]["text"])

    return min_res


######################################
#
# main
if __name__ == "__main__":

    print()
    print("==================")
    print("assembly machine")
    print()
    for q in ("Normal", "Uncommon", "Rare", "Epic", "Legendary"):
        print("==================")
        print(q)
        make_a_complete_search(
            [1.0, 0, 0, 0, 0],
            scheme_1(),
            ("machine", "recycler", "machine"),
            [
                get_q_list(4, "T3", q, False),
                get_q_list_Qonly(4, "T3", q, False),
                get_q_list_Ponly(4, "T3", q, False),
            ],
            q_level_list=[0, 1, 2, 3, 4],
            filename="out_machine_{}.csv".format(q),
        )
        make_a_complete_search(
            [1.0, 0, 0, 0, 0],
            scheme_1(),
            ("    EMP", "recycler", "EMP"),
            [
                get_q_list(5, "T3", q, True),
                get_q_list_Qonly(4, "T3", q, False),
                get_q_list_Ponly(5, "T3", q, True),
            ],
            q_level_list=[0, 1, 2, 3, 4],
            filename="out_EMP_{}.csv".format(q),
        )

    # print()
    # print("==================")
    # print(new_q(3, "T3", "Normal", 0, "", "", False))

    # q = "Normal"
    # q = "Rare"
    # get_the_ratio_v2(
    #     [1, 0, 0, 0, 0],
    #     scheme_2(),
    #     4,
    #     (
    #         new_q(3, "T3", q, 0, "", "", False, False),
    #         new_q(2, "T3", q, 0, "", "", False, False),
    #         new_q(4, "T3", q, 0, "", "", False, False),
    #         new_q(0, "", "", 2, "T3", q, False, False),
    #         new_q(0, "", "", 4, "T3", q, False, False),
    #     ),
    #     True,
    #     log=False,
    # )

    print()
    print("==================")
    print("The calculation is finished")
    print()
