# -*- coding: utf-8 -*-
from . import random


def mean(L):
    return sum(L)/len(L)


def meboot(L, J=1):
    """
    Returns list of J maximum entropy bootstrap samples of time-series L
    """
    N = len(L)
    L_sort = sorted((e,i) for i,e in enumerate(L))
    L_vals = [l[0] for l in L_sort]
    L_inds = [l[1] for l in L_sort]
    L_out = [0]*J
    for j in range(J):
        Z = [(L_vals[i] + L_vals[i+1])/2 for i in range(N-1)]
        m_trm = mean([abs(L[i] - L[i-1]) for i in range(1, N)])
        Z = [L_vals[0] - m_trm] + Z + [L_vals[-1] + m_trm]
        m = [0]*N
        m[0] = 0.75*L_vals[0] + 0.25*L_vals[1]
        for k in range(1, N-1):
            m[k] = 0.25*L_vals[k-1] + 0.5*L_vals[k] + 0.25*L_vals[k+1]
        m[-1] = 0.25*L_vals[-2] + 0.75*L_vals[-1]
        U = sorted([random.random() for _ in range(N)])
        quantiles = [0]*N
        x = [float(y)/N for y in range(N+1)]
        for k in range(N):
            ind = min(range(len(x)), key=lambda i: abs(x[i] - U[k]))
            if x[ind] > U[k]:
                ind -= 1
            c = (2*m[ind] - Z[ind] - Z[ind + 1]) / 2
            y0 = Z[ind] + c
            y1 = Z[ind + 1] + c
            quantiles[k] = y0 + (U[k] - x[ind]) * \
                            (y1 - y0) / (x[ind + 1] - x[ind])
        L_out[j] = [x for y, x in sorted(zip(L_inds, quantiles))]
    return L_out