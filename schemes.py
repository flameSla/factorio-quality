import numpy as np
from modules import mul_q
from utilities import print_line


# ====================================
class scheme_1:
    """assembly machine + recycler"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.mask_recycler = np.zeros(5, dtype="float64")
        self.mask_out = np.ones(5, dtype="float64")
        self.mask_recycler[:q_level] = 1.0
        self.mask_out[:q_level] = 0.0

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


# ====================================
class scheme_2:
    """mining drill + assembly machine + recycler"""

    def __init__(self):
        pass

    def clear(self, q_level):
        self.x1 = np.zeros(5, dtype="float64")
        self.mask_recycler = np.zeros(5, dtype="float64")
        self.mask_out = np.ones(5, dtype="float64")
        self.mask_recycler[:q_level] = 1.0
        self.mask_out[:q_level] = 0.0

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
