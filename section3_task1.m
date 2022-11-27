
m = 1;
M=10;
l = 1;
J = 1;
g = 9.81;
c = 0;
gamma = 0;
Mt = M + m;
Jt = J + m*l^2;
mu = Mt*Jt - (m^2)*(l^2)

%input the matrices for the state space description
A = [0, 0, 1, 0;...
    0, 0, 0, 1; ...
    0, ((m^2)*(l^2)*g)/mu, -c*Jt/mu, -gamma*l*m/mu;...
    0, (Mt*m*g*l)/mu, -(c*l*m)/mu, -gamma*Mt/mu];
B = [0; 0; Jt/mu; l*m/mu];
C = [1, 0, 0, 0; 0, 1, 0, 0];
D = 0;

%create the state space object
sys = ss(A, B, C, D)