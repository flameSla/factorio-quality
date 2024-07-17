# factorio-quality

The scheme_1 class:
![alt text](img/scheme_1.png "The scheme_1 class")

The scheme_2 class:
![alt text](img/scheme_2.png "The scheme_2 class")


Q1, Q2 - blocks for calculating modules. Multiplies the quality/productivity matrix by the input data.

The calculation of x0,x1...south is in the **scheme_1** class


***********************************
Normal
q=1 in:      6.7385 out: 1.00 machine=4: 4xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=2 in:     38.5636 out: 1.00 machine=4: 4xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=3 in:    215.4172 out: 1.00 machine=4: 4xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=4 in:   1072.7888 out: 1.00 machine=4: 4xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=1 in:      3.0933 out: 1.00 machine=5: 5xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=2 in:     13.5007 out: 1.00 machine=5: 5xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=3 in:     57.7325 out: 1.00 machine=5: 5xQ3'Nor'               recycler=4: 4xQ3'Nor'
q=4 in:    221.0154 out: 1.00 machine=5: 5xQ3'Nor'               recycler=4: 4xQ3'Nor'

Uncommon
q=1 in:      5.2080 out: 1.00 machine=4: 4xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=2 in:     26.5460 out: 1.00 machine=4: 4xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=3 in:    131.8630 out: 1.00 machine=4: 4xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=4 in:    584.9986 out: 1.00 machine=4: 4xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=1 in:      2.4357 out: 1.00 machine=5: 5xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=2 in:      9.2808 out: 1.00 machine=5: 5xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=3 in:     34.6983 out: 1.00 machine=5: 5xQ3'Unc'               recycler=4: 4xQ3'Unc'
q=4 in:    116.3597 out: 1.00 machine=5: 5xQ3'Unc'               recycler=4: 4xQ3'Unc'

Rare
q=1 in:      4.2341 out: 1.00 machine=4: 3xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=2 in:     19.2350 out: 1.00 machine=4: 3xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=3 in:     85.6991 out: 1.00 machine=4: 3xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=4 in:    342.0228 out: 1.00 machine=4: 3xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=1 in:      1.9949 out: 1.00 machine=5: 4xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=2 in:      6.6987 out: 1.00 machine=5: 4xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=3 in:     22.2121 out: 1.00 machine=5: 4xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'
q=4 in:     66.1781 out: 1.00 machine=5: 4xQ3'Rar' 1xP3'Rar'     recycler=4: 4xQ3'Rar'

Epic
q=1 in:      3.4585 out: 1.00 machine=4: 3xQ3'Epi' 1xP3'Epi'     recycler=4: 4xQ3'Epi'
q=2 in:     14.1744 out: 1.00 machine=4: 3xQ3'Epi' 1xP3'Epi'     recycler=4: 4xQ3'Epi'
q=3 in:     57.1192 out: 1.00 machine=4: 3xQ3'Epi' 1xP3'Epi'     recycler=4: 4xQ3'Epi'
q=4 in:    206.5169 out: 1.00 machine=4: 3xQ3'Epi' 1xP3'Epi'     recycler=4: 4xQ3'Epi'
q=1 in:      1.6430 out: 1.00 machine=5: 3xQ3'Epi' 2xP3'Epi'     recycler=4: 4xQ3'Epi'
q=2 in:      4.8839 out: 1.00 machine=5: 3xQ3'Epi' 2xP3'Epi'     recycler=4: 4xQ3'Epi'
q=3 in:     14.4235 out: 1.00 machine=5: 3xQ3'Epi' 2xP3'Epi'     recycler=4: 4xQ3'Epi'
q=4 in:     38.3103 out: 1.00 machine=5: 3xQ3'Epi' 2xP3'Epi'     recycler=4: 4xQ3'Epi'

Legendary
q=1 in:      2.3827 out: 1.00 machine=4: 2xQ3'Leg' 2xP3'Leg'     recycler=4: 4xQ3'Leg'
q=2 in:      7.9451 out: 1.00 machine=4: 2xQ3'Leg' 2xP3'Leg'     recycler=4: 4xQ3'Leg'
q=3 in:     26.3185 out: 1.00 machine=4: 2xQ3'Leg' 2xP3'Leg'     recycler=4: 4xQ3'Leg'
q=4 in:     78.3974 out: 1.00 machine=4: 2xQ3'Leg' 2xP3'Leg'     recycler=4: 4xQ3'Leg'
q=1 in:      1.1140 out: 1.00 machine=5: 1xQ3'Leg' 4xP3'Leg'     recycler=4: 4xQ3'Leg'
q=2 in:      2.6184 out: 1.00 machine=5: 1xQ3'Leg' 4xP3'Leg'     recycler=4: 4xQ3'Leg'
q=3 in:      6.1529 out: 1.00 machine=5: 1xQ3'Leg' 4xP3'Leg'     recycler=4: 4xQ3'Leg'
q=4 in:     13.0121 out: 1.00 machine=5: 1xQ3'Leg' 4xP3'Leg'     recycler=4: 4xQ3'Leg'
