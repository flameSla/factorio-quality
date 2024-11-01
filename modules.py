import numpy as np
from utilities import print_q
from utilities import print_line

quality = {
    "Normal": 1.0,
    "Uncommon": 1.30,
    "Rare": 1.60,
    "Epic": 1.90,
    "Legendary": 2.50,
}

quality_tiers = {"T1": 1.0, "T2": 2.0, "T3": 2.5}
productivity_tiers = {"T1": 4.0, "T2": 6.0, "T3": 10.0}
speed_tiers = {"T1": 20.0, "T2": 30.0, "T3": 50.0}

# iron + copper
cost_of_production = {
    "Normal": {"T1": 7.228 + 11.996, "T2": 81.983 + 114.926, "T3": 462.987 + 641.573}
}


# ====================================
# multiplication of the quality matrix
def mul_q(inp, q):
    if len(inp) != 5:
        raise Exception("len(inp) != 5")

    if len(q) != 5 or len(q[0]) != 5:
        print_q(q)
        print(len(q))
        print(len(q[0]))
        raise Exception("len(q) != 5")

    return q.transpose().dot(inp)


# constructor for the quality/productivity matrix
def new_q(
    quality_amount,
    quality_tier,
    quality_quality,
    productivity_amount,
    productivity_tier,
    productivity_quality,
    Percentage_of_productivity_bonus,
    full_name,
):
    Qinp = 0
    text_Q = ""
    Pinp = 1.0
    text_P = ""

    if quality_amount > 0:
        percentage = int(quality_tiers[quality_tier] * quality[quality_quality] * 10.0)
        Qinp = quality_amount * percentage / 1000.0
        text_Q = "{}xQ{}'{}' ".format(
            quality_amount,
            quality_tier[-1:],
            quality_quality[:3],
        )

    if productivity_amount > 0:
        percentage = int(
            productivity_tiers[productivity_tier] * quality[productivity_quality] * 10.0
        )
        Pinp = 1.0 + productivity_amount * percentage / 1000.0
        text_P = "{}xP{}'{}' ".format(
            productivity_amount,
            productivity_tier[-1:],
            productivity_quality[:3],
        )

    if isinstance(Percentage_of_productivity_bonus, float):
        Percentage_of_productivity_bonus = min(Percentage_of_productivity_bonus, 300.0)
        Percentage_of_productivity_bonus = max(Percentage_of_productivity_bonus, 0.0)
        Pinp += Percentage_of_productivity_bonus / 100.0
        Pinp = min(Pinp, 4.0)
    else:
        raise Exception(
            "Percentage_of_productivity_bonus - the type of the variable must be float"
        )

    if full_name:
        text = "{}: {:<23s}".format(
            quality_amount + productivity_amount, text_Q + text_P
        )
    else:
        text = "{}: {}".format(quality_amount + productivity_amount, text_Q + text_P)
        if quality_amount + productivity_amount == 0:
            text = "0:           "

    res = np.zeros((5, 5), dtype="float64")

    res[0][1] = Qinp * 0.9
    res[0][2] = Qinp * 0.1 * 0.9
    res[0][3] = Qinp * 0.1 * 0.1 * 0.9
    res[0][4] = Qinp * 0.1 * 0.1 * 0.1
    res[0][0] = 1 - Qinp
    if abs(sum(res[0][1:]) - Qinp) > 0.00001:
        raise Exception(sum(res[0][1:]))

    res[1][2] = Qinp * 0.9
    res[1][3] = Qinp * 0.1 * 0.9
    res[1][4] = Qinp * 0.1 * 0.1
    res[1][1] = 1 - Qinp
    if abs(sum(res[1][2:]) - Qinp) > 0.00001:
        raise Exception(sum(res[1][2:]))

    res[2][3] = Qinp * 0.9
    res[2][4] = Qinp * 0.1
    res[2][2] = 1 - Qinp
    if abs(sum(res[2][3:]) - Qinp) > 0.00001:
        raise Exception(sum(res[2][3:]))

    res[3][4] = Qinp
    res[3][3] = 1 - Qinp
    if abs(sum(res[3][4:]) - Qinp) > 0.00001:
        raise Exception(sum(res[3][4:]))

    res[4][4] = 1

    res *= Pinp
    return {"text": text, "matrix": res}


# ====================================
def get_q_list(number_of_modules, tier, q_quality, Percentage_of_productivity_bonus):
    q_list = []
    for q in range(0, number_of_modules + 1):
        for p in range(0, number_of_modules + 1):
            if q + p <= number_of_modules:
                q_list.append(
                    new_q(
                        q,
                        tier,
                        q_quality,
                        p,
                        tier,
                        q_quality,
                        Percentage_of_productivity_bonus,
                        True,
                    )
                )
    return q_list


# ====================================
def get_q_list_Qonly(
    number_of_modules, tier, q_quality, Percentage_of_productivity_bonus
):
    q_list = []
    # for q in range(0, number_of_modules + 1):
    #     q_list.append(new_q(q, tier, q_quality, 0, "", "", Percentage_of_productivity_bonus, False))

    q_list.append(new_q(0, "", "", 0, "", "", Percentage_of_productivity_bonus, False))
    q_list.append(
        new_q(
            number_of_modules,
            tier,
            q_quality,
            0,
            "",
            "",
            Percentage_of_productivity_bonus,
            False,
        )
    )
    return q_list


# ====================================
def get_q_list_Ponly(
    number_of_modules, tier, q_quality, Percentage_of_productivity_bonus
):
    q_list = []
    # for p in range(0, number_of_modules + 1):
    #     q_list.append(new_q(0, "", "", p, tier, q_quality, Percentage_of_productivity_bonus, False))
    q_list.append(
        new_q(
            0,
            "",
            "",
            number_of_modules,
            tier,
            q_quality,
            Percentage_of_productivity_bonus,
            False,
        )
    )
    return q_list


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
