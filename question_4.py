import sympy as sym
# Linearisation

# define symbols
# define ass involved symbolic variables

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

#determine partial derivitives os psi
psi_deriv_F = psi.diff(F)
psi_deriv_x3 = psi.diff(x3)
psi_deriv_x4 = psi.diff(x4)

F0 = 0
x30 = 0
x40 = 0

phi_deriv_F_at_equilibrium = phi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x3_at_equilibrium = phi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x4_at_equilibrium = phi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])

psi_deriv_F_at_equilibrium = psi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
psi_deriv_x3_at_equilibrium = psi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
psi_deriv_x4_at_equilibrium = psi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])


# x2' = aF - bx3
a = phi_deriv_F_at_equilibrium
b = -phi_deriv_x3_at_equilibrium
c = -psi_deriv_F_at_equilibrium
d = psi_deriv_x3_at_equilibrium

M_value = 0.3
m_value = 0.1
ell_value = 0.35
g_value = 9.81

a_value = float(a.subs([(M, M_value), (m, m_value)]))
b_value = float(b.subs([(M, M_value), (m, m_value), (g, g_value)]))
c_value = float(c.subs([(M, M_value), (m, m_value), (g, g_value), (ell, ell_value)]))
d_value = float(d.subs([(M, M_value), (m, m_value), (g, g_value), (ell, ell_value)]))


# -------------------- only numerical values, nothing symbolic
import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

s, w = sym.symbols('s, w', real=True, positive=True)
n_points = 500
t_final = 0.2
t_span = np.linspace(0, t_final, n_points)
input_signal = np.sin(100 * (t_span)**2)                                 # input siganl
G_theta = ctrl.TransferFunction(-c_value, [1, 0, -d_value])

t_out, y_out, x_out = ctrl.forced_response(G_theta, t_span, input_signal)

plt.plot(t_out, y_out)
plt.xlabel('time (s)')
plt.ylabel('angle of trajectory (c)')
plt.grid()
plt.show()



