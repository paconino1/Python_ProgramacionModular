from fractions import Fraction

def sumar_fraccion_dosis(f1_n, f1_d, f2_n, f2_d):
  return Fraction(f1_n, f1_d) + Fraction(f2_n, f2_d)