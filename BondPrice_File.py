import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    t = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    discount = (1 + y / ppy) ** t

    pv_coupon = np.sum(coupon / discount)

    pv_face = face / ((1 + y / ppy) ** (m * ppy))

    return pv_coupon + pv_face
