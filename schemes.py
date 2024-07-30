import numpy as np
from modules import mul_q
from modules import new_q
from utilities import print_line
from utilities import print_mat5x5
from utilities import print_q


identity_matrix = np.eye(5, dtype="float64")


# ====================================
class scheme:
    """base class"""

    def __init__(self):
        pass

    def get_masks(self, q_level):
        self.mask_recycler = np.zeros(5, dtype="float64")
        self.mask_out = np.ones(5, dtype="float64")
        self.mask_recycler[:q_level] = 1.0
        self.mask_out[:q_level] = 0.0
        self.q_mask_recycler = np.array(
            [
                self.mask_recycler,
                self.mask_recycler,
                self.mask_recycler,
                self.mask_recycler,
                self.mask_recycler,
            ],
            dtype="float64",
        )

    def sorting(self, inp):
        return inp * self.mask_recycler, inp * self.mask_out

    def machine(self, inp, q1, q2):
        result = mul_q(inp * self.mask_recycler, q1)
        result += mul_q(inp * self.mask_out, q2)
        return result


# ====================================
class scheme_1(scheme):
    """assembly machine + recycler"""

    def __init__(self):
        pass

    def calc(self, x0, q_level, q_list):
        self.get_masks(q_level)

        # k = Q0 * q_mask_recycler * Q2
        # feedback = x2 * q_mask_recycler * Q2
        # x2 = (x0 + feedback) * Q0
        # feedback = (x0 + feedback) * Q0 * q_mask_recycler * Q2
        # feedback = (x0 + feedback) * k
        # feedback = x0 * k + feedback * k
        # feedback * (1 - k)= x0 * k
        q = np.concatenate(
            (q_list[0]["matrix"][:][:q_level], q_list[1]["matrix"][:][q_level:])
        )

        k = (q * self.q_mask_recycler * 0.25).dot(q_list[2]["matrix"])
        obr = np.linalg.inv(identity_matrix - k)
        self.feedback = mul_q(mul_q(x0, k), obr)
        self.x1 = x0 + self.feedback  # feedback
        self.x2 = self.machine(
            self.x1, q_list[0]["matrix"], q_list[1]["matrix"]
        )  # Q1, Q2, assembly machine
        self.xout = self.x2 * self.mask_out

        return self.xout

    def print(self, x0, q_list):
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q_list[0]["text"]))
        print("q1 (assembly machine) = {}".format(q_list[1]["text"]))
        print("q2 (recycler) = {}".format(q_list[2]["text"]))
        print_line("      x0 = ", x0, "{:12.4f}".format(sum(x0)))
        print_line("feedback = ", self.feedback)
        print_line("      x1 = ", self.x1)
        print_line("      x2 = ", self.x2)
        print_line("feedback = ", self.feedback)
        print_line("    xout = ", self.xout)


# ====================================
class scheme_11(scheme):
    """assembly machine + recycler"""

    """ a separate set of modules for machines """

    def __init__(self):
        pass

    def calc(self, x0, q_level, q_list):
        self.get_masks(q_level)

        # k = Q0 * q_mask_recycler * Q2
        # feedback = x2 * q_mask_recycler * Q2
        # x2 = (x0 + feedback) * Q0
        # feedback = (x0 + feedback) * Q0 * q_mask_recycler * Q2
        # feedback = (x0 + feedback) * k
        # feedback = x0 * k + feedback * k
        # feedback * (1 - k)= x0 * k

        q = np.array(
            [
                q_list[0]["matrix"][:][0],
                q_list[1]["matrix"][:][1],
                q_list[2]["matrix"][:][2],
                q_list[3]["matrix"][:][3],
                q_list[4]["matrix"][:][4],
            ],
            dtype="float64",
        )

        k = (q * self.q_mask_recycler * 0.25).dot(q_list[5]["matrix"])
        obr = np.linalg.inv(identity_matrix - k)
        self.feedback = mul_q(mul_q(x0, k), obr)

        self.x1 = x0 + self.feedback  # feedback
        self.x20 = mul_q(self.x1 * [1.0, 0.0, 0.0, 0.0, 0.0], q_list[0]["matrix"])
        self.x21 = mul_q(self.x1 * [0.0, 1.0, 0.0, 0.0, 0.0], q_list[1]["matrix"])
        self.x22 = mul_q(self.x1 * [0.0, 0.0, 1.0, 0.0, 0.0], q_list[2]["matrix"])
        self.x23 = mul_q(self.x1 * [0.0, 0.0, 0.0, 1.0, 0.0], q_list[3]["matrix"])
        self.x24 = mul_q(self.x1 * [0.0, 0.0, 0.0, 0.0, 1.0], q_list[4]["matrix"])
        self.x2 = self.x20 + self.x21 + self.x22 + self.x23 + self.x24
        self.xout = self.x2 * self.mask_out

        return self.xout

    def print(self, x0, q_list):
        print()
        print("==================")
        print("q0 (assembly machine) = {}".format(q_list[0]["text"]))
        print("q1 (assembly machine) = {}".format(q_list[1]["text"]))
        print("q3 (assembly machine) = {}".format(q_list[2]["text"]))
        print("q4 (assembly machine) = {}".format(q_list[3]["text"]))
        print("q5 (assembly machine) = {}".format(q_list[4]["text"]))
        print("q6 (recycler) = {}".format(q_list[5]["text"]))
        print_line("      x0 = ", x0, "{:12.4f}".format(sum(x0)))
        print_line("feedback = ", self.feedback)
        print_line("      x1 = ", self.x1)
        print_line("      x2 = ", self.x2)
        print_line("feedback = ", self.feedback)
        print_line("    xout = ", self.xout)


# ====================================
class scheme_2:
    """mining drill + furnace + recycler + assembly machine"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.x2 = np.zeros(5, dtype="float64")
        self.mask_recycler, self.mask_out = get_masks(q_level)

    def calc(self, x0, q_list):
        self.x1 = mul_q(x0, q_list[0]["matrix"])  # Q0 - mining drill
        self.x3 = self.x1 + self.x2  # furnace
        self.x4 = mul_q(self.x3, q_list[1]["matrix"])  # Q1
        self.x5 = self.x4 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x6 = mul_q(self.x5, q_list[2]["matrix"])  # Q2
        self.x7 = mul_q(self.x6 * self.mask_out, q_list[3]["matrix"])
        self.x2 = self.x6 * self.mask_recycler  # sorting
        self.x10 = self.x4 * self.mask_out + self.x7  # sorting
        self.x11 = self.x10  # assembly machine
        self.xout = mul_q(self.x11, q_list[4]["matrix"])  # Q4
        return self.xout

    def print0(self, x0, q_list, tic):
        print()
        print("==================")
        print("q0 (mining drill) = {}".format(q_list[0]["text"]))
        print("q1 (furnace) = {}".format(q_list[1]["text"]))
        print("q2 (recycler) = {}".format(q_list[2]["text"]))
        print("q3 (assembly machine) = {}".format(q_list[3]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0)
        print_line("x1 = ", self.x1)
        print_line("x2 = ", self.x2)

    def print1(self, x0, q_list, tic):
        print_line("x3 = ", self.x3)
        print_line("x4 = ", self.x4)
        print_line("x5 = ", self.x5)
        print_line("x6 = ", self.x6)
        print_line("x7 = ", self.x7)
        print_line("x2 = ", self.x2)
        print_line("x10= ", self.x10)
        print_line("xout ", self.xout)


# ====================================
class scheme_3:
    """iron for GC"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x6 = np.zeros(5, dtype="float64")
        self.mask_recycler, self.mask_out = get_masks(q_level)

    def calc(self, x0, q_list):
        self.x1 = mul_q(x0, q_list[0]["matrix"])  # Q0 - mining drill
        # sorting ore
        self.x3 = mul_q(self.x1 * self.mask_recycler, q_list[1]["matrix"])  # Q1
        self.x4 = mul_q(self.x1 * self.mask_out, q_list[2]["matrix"])  # Q2
        self.x5 = self.x3 + self.x4
        self.x7 = self.x5 + self.x6  # assembly machine GC
        self.x8 = mul_q(self.x7, q_list[3]["matrix"])  # Q3
        self.x9 = self.x8 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x10 = mul_q(self.x9, q_list[4]["matrix"])  # Q4
        self.x6 = self.x10 * self.mask_recycler
        self.x11 = mul_q(
            self.x10 * self.mask_out, q_list[5]["matrix"]
        )  # assembly machine GC2
        self.xout = self.x8 * self.mask_out + self.x11
        return self.xout

    def print0(self, x0, q_list, tic):
        print()
        print("==================")
        print("q0 (mining drill) = {}".format(q_list[0]["text"]))
        print("q1 (furnace) = {}".format(q_list[1]["text"]))
        print("q2 (recycler) = {}".format(q_list[2]["text"]))
        print("q3 (assembly machine) = {}".format(q_list[3]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0)

    def print1(self, x0, q_list, tic):
        print_line("x1 = ", self.x1)
        print_line("x3 = ", self.x3)
        print_line("x4 = ", self.x4)
        print_line("x5 = ", self.x5)
        print_line("x6 = ", self.x6)
        print_line("x7 = ", self.x7)
        print_line("x8 = ", self.x8)
        print_line("x9 = ", self.x9)
        print_line("x10= ", self.x10)
        print_line("x11= ", self.x11)
        print_line("xout ", self.xout)


# ====================================
class scheme_4:
    """iron for T1"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x6 = np.zeros(5, dtype="float64")
        self.mask_recycler, self.mask_out = get_masks(q_level)

    def calc(self, x0, q_list):
        self.x1 = mul_q(x0, q_list[0]["matrix"])  # Q0 - mining drill
        # sorting ore
        self.x3 = mul_q(self.x1 * self.mask_recycler, q_list[1]["matrix"])  # Q1 furn
        self.x4 = mul_q(self.x1 * self.mask_out, q_list[2]["matrix"])  # Q2 furn
        self.x41 = self.x3 + self.x4
        self.x42 = mul_q(self.x41 * self.mask_recycler, q_list[3]["matrix"])  # Q3 GC
        self.x43 = mul_q(self.x41 * self.mask_out, q_list[4]["matrix"])  # Q4 GC
        self.x5 = self.x42 + self.x43
        self.x7 = (self.x5 + self.x6) / 5.0  # assembly machine T1
        self.x8 = mul_q(self.x7, q_list[5]["matrix"])  # Q5 T1
        self.x9 = self.x8 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x10 = mul_q(self.x9, q_list[6]["matrix"])  # Q6 rec
        self.x6 = self.x10 * self.mask_recycler
        self.x11 = mul_q(
            self.x10 * self.mask_out / 5.0, q_list[7]["matrix"]  # Q7 T1
        )  # assembly machine GC2
        self.xout = self.x8 * self.mask_out + self.x11
        return self.xout

    def print0(self, x0, q_list, tic):
        print()
        print("==================")
        print("q0 (mining drill) = {}".format(q_list[0]["text"]))
        print("q1 (furnace) = {}".format(q_list[1]["text"]))
        print("q2 (recycler) = {}".format(q_list[2]["text"]))
        print("q3 (assembly machine) = {}".format(q_list[3]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0)

    def print1(self, x0, q_list, tic):
        print_line("x1 = ", self.x1)
        print_line("x3 = ", self.x3)
        print_line("x4 = ", self.x4)
        print_line("x5 = ", self.x5)
        print_line("x6 = ", self.x6)
        print_line("x7 = ", self.x7)
        print_line("x8 = ", self.x8)
        print_line("x9 = ", self.x9)
        print_line("x10= ", self.x10)
        print_line("x11= ", self.x11)
        print_line("xout ", self.xout)


######################################
#
# main
if __name__ == "__main__":
    func_list = [
        name
        for (name, obj) in vars().items()
        if hasattr(obj, "__class__") and obj.__class__.__name__ == "function"
    ]
    print(func_list)

    def get_method_names(class_name):
        print("****************************")
        print(f"{class_name}")
        for name in dir(class_name):
            if name[-1] != "_":
                print(name)

    print("****************************")
    print("****************************")
    get_method_names(scheme_1)
    get_method_names(scheme_2)
