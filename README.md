# factorio-quality

The scheme_1 class:
![alt text](img/scheme_1.png "The scheme_1 class")

The scheme_2 class:
![alt text](img/scheme_2.png "The scheme_2 class")


Q1, Q2 - blocks for calculating modules. Multiplies the quality/productivity matrix by the input data.

The calculation of x0,x1...south is in the **scheme_1** class


```
==================

Normal
number of combinations = 30
q=0 in:      0.7143 out: 1.00 machine = 4: 4xP3'Nor'               recycler = 0:            machine = 4: 4xP3'Nor' 
q=1 in:      6.7385 out: 1.00 machine = 4: 4xQ3'Nor'               recycler = 4: 4xQ3'Nor'  machine = 4: 4xP3'Nor'
q=2 in:     38.5634 out: 1.00 machine = 4: 4xQ3'Nor'               recycler = 4: 4xQ3'Nor'  machine = 4: 4xP3'Nor'
q=3 in:    215.4091 out: 1.00 machine = 4: 4xQ3'Nor'               recycler = 4: 4xQ3'Nor'  machine = 4: 4xP3'Nor'
q=4 in:   1072.6258 out: 1.00 machine = 4: 4xQ3'Nor'               recycler = 4: 4xQ3'Nor'  machine = 4: 4xP3'Nor'
number of combinations = 42
q=0 in:      0.5000 out: 1.00     EMP = 5: 5xP3'Nor'               recycler = 0:            EMP = 5: 5xP3'Nor' 
q=1 in:      3.0933 out: 1.00     EMP = 5: 5xQ3'Nor'               recycler = 4: 4xQ3'Nor'  EMP = 5: 5xP3'Nor'
q=2 in:     13.5007 out: 1.00     EMP = 5: 5xQ3'Nor'               recycler = 4: 4xQ3'Nor'  EMP = 5: 5xP3'Nor'
q=3 in:     57.7317 out: 1.00     EMP = 5: 5xQ3'Nor'               recycler = 4: 4xQ3'Nor'  EMP = 5: 5xP3'Nor'
q=4 in:    221.0018 out: 1.00     EMP = 5: 5xQ3'Nor'               recycler = 4: 4xQ3'Nor'  EMP = 5: 5xP3'Nor'
==================

Uncommon
number of combinations = 30
q=0 in:      0.6579 out: 1.00 machine = 4: 4xP3'Unc'               recycler = 0:            machine = 4: 4xP3'Unc' 
q=1 in:      5.2806 out: 1.00 machine = 4: 4xQ3'Unc'               recycler = 4: 4xQ3'Unc'  machine = 4: 4xP3'Unc'
q=2 in:     27.0945 out: 1.00 machine = 4: 4xQ3'Unc'               recycler = 4: 4xQ3'Unc'  machine = 4: 4xP3'Unc'
q=3 in:    135.5362 out: 1.00 machine = 4: 4xQ3'Unc'               recycler = 4: 4xQ3'Unc'  machine = 4: 4xP3'Unc'
q=4 in:    605.4867 out: 1.00 machine = 4: 4xQ3'Unc'               recycler = 4: 4xQ3'Unc'  machine = 4: 4xP3'Unc'
number of combinations = 42
q=0 in:      0.4651 out: 1.00     EMP = 5: 5xP3'Unc'               recycler = 0:            EMP = 5: 5xP3'Unc' 
q=1 in:      2.4669 out: 1.00     EMP = 5: 5xQ3'Unc'               recycler = 4: 4xQ3'Unc'  EMP = 5: 5xP3'Unc'
q=2 in:      9.4721 out: 1.00     EMP = 5: 5xQ3'Unc'               recycler = 4: 4xQ3'Unc'  EMP = 5: 5xP3'Unc'
q=3 in:     35.6969 out: 1.00     EMP = 5: 5xQ3'Unc'               recycler = 4: 4xQ3'Unc'  EMP = 5: 5xP3'Unc'
q=4 in:    120.6583 out: 1.00     EMP = 5: 5xQ3'Unc'               recycler = 4: 4xQ3'Unc'  EMP = 5: 5xP3'Unc'
==================

Rare
number of combinations = 30
q=0 in:      0.6098 out: 1.00 machine = 4: 4xP3'Rar'               recycler = 0:            machine = 4: 4xP3'Rar' 
q=1 in:      4.2341 out: 1.00 machine = 4: 3xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  machine = 4: 4xP3'Rar'
q=2 in:     19.2349 out: 1.00 machine = 4: 3xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  machine = 4: 4xP3'Rar'
q=3 in:     85.6973 out: 1.00 machine = 4: 3xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  machine = 4: 4xP3'Rar'
q=4 in:    341.9876 out: 1.00 machine = 4: 3xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  machine = 4: 4xP3'Rar'
number of combinations = 42
q=0 in:      0.4348 out: 1.00     EMP = 5: 5xP3'Rar'               recycler = 0:            EMP = 5: 5xP3'Rar' 
q=1 in:      1.9949 out: 1.00     EMP = 5: 4xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  EMP = 5: 5xP3'Rar'
q=2 in:      6.6987 out: 1.00     EMP = 5: 4xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  EMP = 5: 5xP3'Rar'
q=3 in:     22.2120 out: 1.00     EMP = 5: 4xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  EMP = 5: 5xP3'Rar'
q=4 in:     66.1762 out: 1.00     EMP = 5: 4xQ3'Rar' 1xP3'Rar'     recycler = 4: 4xQ3'Rar'  EMP = 5: 5xP3'Rar'
==================

Epic
number of combinations = 30
q=0 in:      0.5682 out: 1.00 machine = 4: 4xP3'Epi'               recycler = 0:            machine = 4: 4xP3'Epi' 
q=1 in:      3.4894 out: 1.00 machine = 4: 3xQ3'Epi' 1xP3'Epi'     recycler = 4: 4xQ3'Epi'  machine = 4: 4xP3'Epi'
q=2 in:     14.3748 out: 1.00 machine = 4: 3xQ3'Epi' 1xP3'Epi'     recycler = 4: 4xQ3'Epi'  machine = 4: 4xP3'Epi'
q=3 in:     58.2352 out: 1.00 machine = 4: 3xQ3'Epi' 1xP3'Epi'     recycler = 4: 4xQ3'Epi'  machine = 4: 4xP3'Epi'
q=4 in:    211.6693 out: 1.00 machine = 4: 3xQ3'Epi' 1xP3'Epi'     recycler = 4: 4xQ3'Epi'  machine = 4: 4xP3'Epi'
number of combinations = 42
q=0 in:      0.4082 out: 1.00     EMP = 5: 5xP3'Epi'               recycler = 0:            EMP = 5: 5xP3'Epi' 
q=1 in:      1.6559 out: 1.00     EMP = 5: 3xQ3'Epi' 2xP3'Epi'     recycler = 4: 4xQ3'Epi'  EMP = 5: 5xP3'Epi'
q=2 in:      4.9490 out: 1.00     EMP = 5: 3xQ3'Epi' 2xP3'Epi'     recycler = 4: 4xQ3'Epi'  EMP = 5: 5xP3'Epi'
q=3 in:     14.6962 out: 1.00     EMP = 5: 3xQ3'Epi' 2xP3'Epi'     recycler = 4: 4xQ3'Epi'  EMP = 5: 5xP3'Epi'
q=4 in:     39.2491 out: 1.00     EMP = 5: 3xQ3'Epi' 2xP3'Epi'     recycler = 4: 4xQ3'Epi'  EMP = 5: 5xP3'Epi'
==================

Legendary
number of combinations = 30
q=0 in:      0.5000 out: 1.00 machine = 4: 4xP3'Leg'               recycler = 0:            machine = 4: 4xP3'Leg' 
q=1 in:      2.3977 out: 1.00 machine = 4: 2xQ3'Leg' 2xP3'Leg'     recycler = 4: 4xQ3'Leg'  machine = 4: 4xP3'Leg'
q=2 in:      8.0281 out: 1.00 machine = 4: 2xQ3'Leg' 2xP3'Leg'     recycler = 4: 4xQ3'Leg'  machine = 4: 4xP3'Leg'
q=3 in:     26.7043 out: 1.00 machine = 4: 2xQ3'Leg' 2xP3'Leg'     recycler = 4: 4xQ3'Leg'  machine = 4: 4xP3'Leg'
q=4 in:     79.8786 out: 1.00 machine = 4: 2xQ3'Leg' 2xP3'Leg'     recycler = 4: 4xQ3'Leg'  machine = 4: 4xP3'Leg'
number of combinations = 42
q=0 in:      0.3636 out: 1.00     EMP = 5: 5xP3'Leg'               recycler = 0:            EMP = 5: 5xP3'Leg' 
q=1 in:      1.1198 out: 1.00     EMP = 5: 1xQ3'Leg' 4xP3'Leg'     recycler = 4: 4xQ3'Leg'  EMP = 5: 5xP3'Leg'
q=2 in:      2.6422 out: 1.00     EMP = 5: 1xQ3'Leg' 4xP3'Leg'     recycler = 4: 4xQ3'Leg'  EMP = 5: 5xP3'Leg'
q=3 in:      6.2332 out: 1.00     EMP = 5: 1xQ3'Leg' 4xP3'Leg'     recycler = 4: 4xQ3'Leg'  EMP = 5: 5xP3'Leg'
q=4 in:     13.2339 out: 1.00     EMP = 5: 1xQ3'Leg' 4xP3'Leg'     recycler = 4: 4xQ3'Leg'  EMP = 5: 5xP3'Leg'
```