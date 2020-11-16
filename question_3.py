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

# Determine the partial derivatives of phi wrt to F x3 x4
phi_deriv_F = phi.diff(F)
phi_deriv_x3 = phi.diff(x3)
phi_deriv_x4 = phi.diff(x4)

F0 = 0
x30 = 0
x40 = 0

phi_deriv_F_at_equilibrium = phi_deriv_F.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x3_at_equilibrium = phi_deriv_x3.subs([(F, F0), (x3, x30), (x4, x40)])
phi_deriv_x4_at_equilibrium = phi_deriv_x4.subs([(F, F0), (x3, x30), (x4, x40)])



# x2' = aF - bx3
a = phi_deriv_F_at_equilibrium
b = -phi_deriv_x3_at_equilibrium   # here I will have to do C and D
c = 3 / ell / (4*M+m)
d = 3 * (M+m) * g / ell / (4*M+m)

M_value = 0.3
m_value = 0.1
ell_value = 0.35
g_value = 9.81

a_value = a.subs([(M, M_value), (m, m_value)])
b_value = b.subs([(M, M_value), (m, m_value), (g, g_value)])
c_value = c.subs([(M, M_value), (m, m_value), (g, g_value)]), (ell, ell_value)
d_value = d.subs([(M, M_value), (m, m_value), (g, g_value)]), (ell, ell_value)

w = sym.symbols('w-/', real=True)
s, t = sym.symbols('s, t', real=True, positive=True)
a, b, c, d,  = sym.symbols('a, b, c, d', real=True, positive=True)
G_theta = -c / (s**2 - d)                                                      # G_theta uses X3 as output variable and F(s) as input variable
G_x = (-c * b + d * a - s**2) / (-s**4 + d * s**2)                             # G_x uses X1 as output variable and F(s) as input variable

F_s_impulse = 1                                                                #use laplace transform to go from f(t) to f(s) and inverse to go f(s) to f(t)
F_s_step = 1 / s                                                               # but must manually go from f(t) to f(s)
F_s_frequency = w / (s**2 + w**2)
                                                                               # push: F_s = 1 / s
X3_s_frequency = G_theta * F_s_frequency
X3_s_step = G_theta * F_s_step
X3_s_impulse = G_theta * F_s_impulse                                                   # shake: F_s = 1 / (s**2 + 1)   this is the inverse laplace of sin(t)
x3_t_impulse = sym.inverse_laplace_transform(X3_s_impulse, s, t, w)           # kick: f_s = 1
x3_t_step = sym.inverse_laplace_transform(X3_s_step, s, t, w)
x3_t_frequency = sym.inverse_laplace_transform(X3_s_frequency, s, t, w)

X1_s_impulse = G_x * F_s_impulse
X1_s_step = G_x * F_s_step
X1_s_frequency = G_x * F_s_frequency
x1_t_impulse = sym.inverse_laplace_transform(X1_s_impulse, s, t, w)
x1_t_step = sym.inverse_laplace_transform(X1_s_step, s, t, w)
x1_t_frequency = sym.inverse_laplace_transform(X1_s_frequency, s, t, w)


#sym.pprint(x3_t.simplify())
#sym.pprint(x1_t_impulse.simplify())
sym.pprint(X1_s_frequency)

