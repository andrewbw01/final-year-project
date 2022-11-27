
m = 1;
M=10;
l = 1;
J = 1;
g = 9.81;
c = 0;
gamma = 0;
Mt = M + m;
Jt = J + m*l^2;
mu = Mt*Jt - (m^2)*(l^2);

syms q qdot theta thetadot u

%x = [q; theta; qdot; thetadot];

non_linear_sys = [qdot ;...
        thetadot;...
       (-m*l*sin(theta)*(thetadot^2) + m*g*((m*(l^2))/Jt)*sin(theta)*cos(theta) - c*qdot - (gamma/Jt)*m*l*cos(theta)*thetadot + u)/(Mt - m*(m*(l^2)/Jt)*(cos(theta))^2);...
       (-m*(l^2)*sin(theta)*cos(theta)*(thetadot^2) + Mt*g*l*sin(theta) - c*l*cos(theta)*qdot - gamma*(Mt/m)*thetadot +l*cos(theta)*u)/(Jt*(Mt/m) - m*(l*cos(theta))^2)];

   
t = 0:0.04:10; %time to simulate over
X0 = [0;1;0;0]; %initial conditions

%using ODE45 we set the input u = -kx
[t x] = ode45(@(t,x) ode_non_linear_sys(t, x, non_linear_sys, -K*x), t, X0)

plot(t, x(:,2))
grid on