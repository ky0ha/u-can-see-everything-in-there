from torch import rand, zeros


D = 10
NP = 300
Xs = 20
Xx = -20
G = 200
nf = zeros(D, NP)
Pc = 0.8
Pm = 0.1
f = rand(D, NP) * (Xs - Xx) + Xx

