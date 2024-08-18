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
from schemes import scheme_2
from schemes import scheme_3
from schemes import scheme_4

from quality import get_the_ratio_v2


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


# q = "Normal"
q = "Rare"
get_the_ratio(
    [1, 0, 0, 0, 0],
    scheme_1(),
    1,
    (
        new_q(4, "T3", q, 0, "T3", q, False, False),
        new_q(0, "T3", q, 0, "T3", q, False, False),
        new_q(4, "T3", q, 0, "T3", q, False, False),
    ),
    True,
    log=False,
)
get_the_ratio_v2(
    [1, 0, 0, 0, 0],
    scheme_1(),
    1,
    (
        new_q(4, "T3", q, 0, "T3", q, False, False),
        new_q(0, "T3", q, 0, "T3", q, False, False),
        new_q(4, "T3", q, 0, "T3", q, False, False),
    ),
    True,
    log=False,
)

q0 = new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"]
q1 = new_q(0, "T3", q, 0, "T3", q, False, False)["matrix"]
q2 = new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"]

q_level = 1
mask_recycler = np.zeros(5, dtype="float64")
mask_out = np.ones(5, dtype="float64")
mask_recycler[:q_level] = 1.0
mask_out[:q_level] = 0.0

# print(mask_recycler)
# print(mask_out)

x0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0])

mask1 = np.zeros((5, 5), dtype="float64")
mask1[0] = mask_recycler * 0.25
mask1[1] = mask_recycler * 0.25
mask1[2] = mask_recycler * 0.25
mask1[3] = mask_recycler * 0.25
mask1[4] = mask_recycler * 0.25
# mask1 = np.transpose(mask1)

k = q0 * mask1
k = k.dot(q2)
# print("k = ", type(k), k)

# numerator = mul_q(x0, k)
# print_line("numerator2 = ", numerator)


obr = np.linalg.inv(np.eye(5).transpose() - k)
# print("obr = ", obr)
feedback = mul_q(mul_q(x0, k), obr)
print_line("feedback=", feedback)
x1 = x0 + feedback
print_line("x1=", x1)
x2 = mul_q(x1 * mask_recycler, q0) + mul_q(x1 * mask_out, q1)
print_line("x2=", x2)
xout = x2 * mask_out
print_line("xout = ", xout)
print_line("x0 = ", x0 / xout[q_level])


# a = np.array([1.0000, 0.0000, 0.0000, 0.0000, 0.0000])
# b = np.array([0.2142, 0.0892, 0.0231, 0.0053, 0.0008])
# print(a + b)
# print_line(" b=", b)
# print_line("x1=", numerator + k.transpose().dot(b))
# print_line("x1 * (1-k)=", (np.eye(5) - k.transpose()).dot(b))


# print(mul_q(a + b, new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"]))


# print(mul_q(a, new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"]))
# print(mul_q(b, new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"]))
# print(
#     mul_q(a, new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"])
#     + mul_q(b, new_q(4, "T3", q, 0, "T3", q, False, False)["matrix"])
# )
