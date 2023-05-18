import math


def area(side, alpha, beta):
    alpha = math.radians(alpha)
    beta = math.radians(beta)
    return math.pow(side, 2) / 2 * ((math.sin(alpha) * math.sin(beta)) / math.sin(math.pi - (alpha + beta)))