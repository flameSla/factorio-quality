import numpy as np
from modules import mul_q
from utilities import print_line


def get_masks(q_level):
    mask_recycler = np.zeros(5, dtype="float64")
    mask_out = np.ones(5, dtype="float64")
    mask_recycler[:q_level] = 1.0
    mask_out[:q_level] = 0.0
    # if q_level == 0:
    #     mask_out[0] = 1.0

    return mask_recycler, mask_out


# ====================================
class scheme_1:
    """assembly machine + recycler"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.mask_recycler, self.mask_out = get_masks(q_level)

    def calc(self, x0, q_list):
        self.x10 = x0 + self.x1  # assembly machine
        self.x2 = mul_q(self.x10, q_list[0]["matrix"])  # Q1
        self.x3 = self.x2 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x12 = mul_q(self.x3, q_list[1]["matrix"])  # Q2
        self.x1 = self.x12 * self.mask_recycler  # sorting
        self.x13 = mul_q(self.x12 * self.mask_out, q_list[2]["matrix"])
        self.xout = self.x2 * self.mask_out + self.x13  # sorting
        return self.xout

    def print0(self, x0, q_list, tic):
        print()
        print("==================")
        print("q1 (assembly machine) = {}".format(q_list[0]["text"]))
        print("q2 (recycler) = {}".format(q_list[1]["text"]))
        print("tic = {}".format(tic))
        print_line("x0 = ", x0, "{:12.4f}".format(sum(x0)))
        print_line("x1 = ", self.x1)

    def print1(self, x0, q_list, tic):
        print_line("x10= ", self.x10)
        print_line("x2 = ", self.x2)
        print_line("x3 = ", self.x3)
        print_line("x12= ", self.x12)
        print_line("x1 = ", self.x1)
        print_line("x13= ", self.x13)
        print_line("xout ", self.xout)


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
        self.x3 = mul_q(self.x1 * self.mask_recycler, q_list[1]["matrix"])  # Q1
        self.x4 = mul_q(self.x1 * self.mask_out, q_list[2]["matrix"])  # Q2
        self.x41 = self.x3 + self.x4
        self.x42 = mul_q(self.x41 * self.mask_recycler, q_list[3]["matrix"])  # Q1 GC
        self.x43 = mul_q(self.x41 * self.mask_out, q_list[4]["matrix"])  # Q2 GC
        self.x5 = self.x42 + self.x43
        self.x7 = (self.x5 + self.x6) / 5.0  # assembly machine GC
        self.x8 = mul_q(self.x7, q_list[5]["matrix"])  # Q3
        self.x9 = self.x8 * 0.25 * self.mask_recycler  # recycler + sorting
        self.x10 = mul_q(self.x9, q_list[6]["matrix"])  # Q4
        self.x6 = self.x10 * self.mask_recycler
        self.x11 = mul_q(
            self.x10 * self.mask_out / 5.0, q_list[7]["matrix"]
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
