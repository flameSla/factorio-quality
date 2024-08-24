import pytest
from quality import get_the_ratio_v2
from modules import new_q
from schemes import scheme_1


def get_out_machine(q_level, q_list, q):
    q_list.append(new_q(4, "T3", q, 0, "T3", "", False, False))
    q_list.append(new_q(0, "", "", 4, "T3", q, False, False))
    return get_the_ratio_v2(
        [1, 0, 0, 0, 0],
        scheme_1(),
        q_level,
        q_list,
        False,
        log=False,
    )


def get_out_EMP(q_level, q_list, q):
    q_list.append(new_q(4, "T3", q, 0, "T3", "", False, False))
    q_list.append(new_q(0, "", "", 5, "T3", q, True, False))
    return get_the_ratio_v2(
        [1, 0, 0, 0, 0],
        scheme_1(),
        q_level,
        q_list,
        False,
        log=False,
    )


class TestNormal:

    def test_Normal(self):
        q = "Normal"
        out0 = get_out_machine(0, [new_q(0, "T3", q, 4, "T3", q, False, False)], q)
        out1 = get_out_machine(1, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out2 = get_out_machine(2, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out3 = get_out_machine(3, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out4 = get_out_machine(4, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.7143
        assert pytest.approx(out1["x0"][0], 0.0001) == 6.7385
        assert pytest.approx(out2["x0"][0], 0.0001) == 38.5634
        assert pytest.approx(out3["x0"][0], 0.0001) == 215.4091
        assert pytest.approx(out4["x0"][0], 0.0001) == 1072.6258

        out0 = get_out_EMP(0, [new_q(0, "T3", q, 5, "T3", q, True, False)], q)
        out1 = get_out_EMP(1, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out2 = get_out_EMP(2, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out3 = get_out_EMP(3, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out4 = get_out_EMP(4, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.5000
        assert pytest.approx(out1["x0"][0], 0.0001) == 3.0933
        assert pytest.approx(out2["x0"][0], 0.0001) == 13.5007
        assert pytest.approx(out3["x0"][0], 0.0001) == 57.7317
        assert pytest.approx(out4["x0"][0], 0.0001) == 221.0018

    def test_Uncommon(self):
        q = "Uncommon"
        out0 = get_out_machine(0, [new_q(0, "T3", q, 4, "T3", q, False, False)], q)
        out1 = get_out_machine(1, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out2 = get_out_machine(2, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out3 = get_out_machine(3, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)
        out4 = get_out_machine(4, [new_q(4, "T3", q, 0, "T3", q, False, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.6579
        assert pytest.approx(out1["x0"][0], 0.0001) == 5.2806
        assert pytest.approx(out2["x0"][0], 0.0001) == 27.0945
        assert pytest.approx(out3["x0"][0], 0.0001) == 135.5362
        assert pytest.approx(out4["x0"][0], 0.0001) == 605.4867

        out0 = get_out_EMP(0, [new_q(0, "T3", q, 5, "T3", q, True, False)], q)
        out1 = get_out_EMP(1, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out2 = get_out_EMP(2, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out3 = get_out_EMP(3, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)
        out4 = get_out_EMP(4, [new_q(5, "T3", q, 0, "T3", q, True, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.4651
        assert pytest.approx(out1["x0"][0], 0.0001) == 2.4669
        assert pytest.approx(out2["x0"][0], 0.0001) == 9.4721
        assert pytest.approx(out3["x0"][0], 0.0001) == 35.6969
        assert pytest.approx(out4["x0"][0], 0.0001) == 120.6583

    def test_Rare(self):
        q = "Rare"
        out0 = get_out_machine(0, [new_q(0, "T3", q, 4, "T3", q, False, False)], q)
        out1 = get_out_machine(1, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out2 = get_out_machine(2, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out3 = get_out_machine(3, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out4 = get_out_machine(4, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.6098
        assert pytest.approx(out1["x0"][0], 0.0001) == 4.2341
        assert pytest.approx(out2["x0"][0], 0.0001) == 19.2349
        assert pytest.approx(out3["x0"][0], 0.0001) == 85.6973
        assert pytest.approx(out4["x0"][0], 0.0001) == 341.9876

        out0 = get_out_EMP(0, [new_q(0, "T3", q, 5, "T3", q, True, False)], q)
        out1 = get_out_EMP(1, [new_q(4, "T3", q, 1, "T3", q, True, False)], q)
        out2 = get_out_EMP(2, [new_q(4, "T3", q, 1, "T3", q, True, False)], q)
        out3 = get_out_EMP(3, [new_q(4, "T3", q, 1, "T3", q, True, False)], q)
        out4 = get_out_EMP(4, [new_q(4, "T3", q, 1, "T3", q, True, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.4348
        assert pytest.approx(out1["x0"][0], 0.0001) == 1.9949
        assert pytest.approx(out2["x0"][0], 0.0001) == 6.6987
        assert pytest.approx(out3["x0"][0], 0.0001) == 22.2120
        assert pytest.approx(out4["x0"][0], 0.0001) == 66.1762

    def test_Epic(self):
        q = "Epic"
        out0 = get_out_machine(0, [new_q(0, "T3", q, 4, "T3", q, False, False)], q)
        out1 = get_out_machine(1, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out2 = get_out_machine(2, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out3 = get_out_machine(3, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)
        out4 = get_out_machine(4, [new_q(3, "T3", q, 1, "T3", q, False, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.5682
        assert pytest.approx(out1["x0"][0], 0.0001) == 3.4894
        assert pytest.approx(out2["x0"][0], 0.0001) == 14.3748
        assert pytest.approx(out3["x0"][0], 0.0001) == 58.2352
        assert pytest.approx(out4["x0"][0], 0.0001) == 211.6693

        out0 = get_out_EMP(0, [new_q(0, "T3", q, 5, "T3", q, True, False)], q)
        out1 = get_out_EMP(1, [new_q(3, "T3", q, 2, "T3", q, True, False)], q)
        out2 = get_out_EMP(2, [new_q(3, "T3", q, 2, "T3", q, True, False)], q)
        out3 = get_out_EMP(3, [new_q(3, "T3", q, 2, "T3", q, True, False)], q)
        out4 = get_out_EMP(4, [new_q(3, "T3", q, 2, "T3", q, True, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.4082
        assert pytest.approx(out1["x0"][0], 0.0001) == 1.6559
        assert pytest.approx(out2["x0"][0], 0.0001) == 4.9490
        assert pytest.approx(out3["x0"][0], 0.0001) == 14.6962
        assert pytest.approx(out4["x0"][0], 0.0001) == 39.2491

    def test_Legendary(self):
        q = "Legendary"
        out0 = get_out_machine(0, [new_q(0, "T3", q, 4, "T3", q, False, False)], q)
        out1 = get_out_machine(1, [new_q(2, "T3", q, 2, "T3", q, False, False)], q)
        out2 = get_out_machine(2, [new_q(2, "T3", q, 2, "T3", q, False, False)], q)
        out3 = get_out_machine(3, [new_q(2, "T3", q, 2, "T3", q, False, False)], q)
        out4 = get_out_machine(4, [new_q(2, "T3", q, 2, "T3", q, False, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.5000
        assert pytest.approx(out1["x0"][0], 0.0001) == 2.3977
        assert pytest.approx(out2["x0"][0], 0.0001) == 8.0281
        assert pytest.approx(out3["x0"][0], 0.0001) == 26.7043
        assert pytest.approx(out4["x0"][0], 0.0001) == 79.8786

        out0 = get_out_EMP(0, [new_q(0, "T3", q, 5, "T3", q, True, False)], q)
        out1 = get_out_EMP(1, [new_q(1, "T3", q, 4, "T3", q, True, False)], q)
        out2 = get_out_EMP(2, [new_q(1, "T3", q, 4, "T3", q, True, False)], q)
        out3 = get_out_EMP(3, [new_q(1, "T3", q, 4, "T3", q, True, False)], q)
        out4 = get_out_EMP(4, [new_q(1, "T3", q, 4, "T3", q, True, False)], q)

        assert pytest.approx(out0["x0"][0], 0.0001) == 0.3636
        assert pytest.approx(out1["x0"][0], 0.0001) == 1.1198
        assert pytest.approx(out2["x0"][0], 0.0001) == 2.6422
        assert pytest.approx(out3["x0"][0], 0.0001) == 6.2332
        assert pytest.approx(out4["x0"][0], 0.0001) == 13.2339


#
# pytest d:\GitHub\factorio-quality\test.py
#
