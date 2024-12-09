import math as m
f = lambda x, y: x/y

def chi(x , coef , y , inc_y , inc_x , debug=True):
    value = m.pow((x*coef)-y , 2) / m.pow(inc_y , 2)
    if debug:
        print(value)
    return value

def sum_chi(dati_x , dati_y , inc_y ,inc_x , coef , debug = True):
    return sum([chi(dati_x[h] , coef , dati_y[h] , inc_y[h], inc_x[h] ,debug=debug) for h in range(len(dati_x))])

def media_pes(*args):
    pesi = sum([1/(dato[1]**2) for dato in args])
    medi = sum([dato[0]/(dato[1]**2) for dato in args])
    medi_m = medi/pesi
    inc = 1/(pesi**0.5)
    return (medi_m , inc)

def find(dati_x , dati_y , inc_y, inc_x):
    step = 0.0000000001
    coef = sum([f(dati_x[h] , dati_y[h]) for h in range(len(dati_x))]) / len(dati_x)
    m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef)
    while True:
        chi_2 = sum_chi(dati_x , dati_y , inc_y,inc_x , coef+step)
        chi_3 = sum_chi(dati_x , dati_y , inc_y,inc_x , coef-step)
        if m_chi < chi_2 and m_chi < chi_3:
            m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef)
            break
        elif m_chi > chi_2 and chi_3 > m_chi:
            coef += step
        else:
            coef -= step
        m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef)
    
    return (coef , m_chi)

def find_m(dati_x , dati_y , inc_y,inc_x , threshold , coef_min):
    step = 0.001
    coef1 = coef_min
    coef2 = coef_min
    m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef1)
    while True:
        chi_2 = sum_chi(dati_x , dati_y , inc_y,inc_x , coef1+step)
        if chi_2>threshold:
            m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef1)
            break
        else:
            coef1+= step
        m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef1)
    m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef2)
    while True:
        chi_2 = sum_chi(dati_x , dati_y , inc_y,inc_x , coef2-step)
        if chi_2>threshold:
            m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef2)
            break
        else:
            coef2-= step
        m_chi = sum_chi(dati_x , dati_y , inc_y,inc_x , coef1)
    return ((coef2+coef1)/2 , abs(coef2-coef1)/2)