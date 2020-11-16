import sympy as sym
# Linearisation

# define symbols
# define ass involved symbolic variables

# constants
M, m, g, ell = sym.symbols('M, m, g, ell', real=True, positive=True)

# system variables
x1, x2, x3, x4, F = sym.symbols('x1, x2, x3, x4, F')

# Define phi
phi = 4 * m * ell * x4**2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)
phi /= 4 * (M + m) - 3 * m * sym.cos(x3)**2

# Define psi
psi = -3 * (m * ell * x4 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3))
psi /= (4 * (M+m) - 3 * m * sym.cos(x3)**2) * ell

# Determine the partial derivatives of phi wrt to F x3 x4
phi_deriv_F = phi.diff(F)
phi_deriv_x3 = phi.diff(x3)
phi_deriv_x4 = phi.diff(x4)

# Determine the partial derivatives of psi wrt to F, x3, x4
psi_deriv_F = psi.diff(F)
psi_deriv_x3 = psi.diff(x3)
psi_deriv_x4 = psi.diff(x4)

F0 = 0
x30 = 0
x40 = 0

# At equilibrium
psi_deriv_F_at_equilibrium = psi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
psi_deriv_x3_at_equilibrium = psi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
psi_deriv_x4_at_equilibrium = psi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])

phi_deriv_F_at_equilibrium = phi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x3_at_equilibrium = phi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x4_at_equilibrium = phi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])

#sym.pprint(phi_deriv_F_at_equilibrium)
#sym.pprint(phi_deriv_x3_at_equilibrium)
#sym.pprint(phi_deriv_x4_at_equilibrium)

#sym.pprint(psi_deriv_F_at_equilibrium )
print(sym.latex(psi_deriv_x4_at_equilibrium))




