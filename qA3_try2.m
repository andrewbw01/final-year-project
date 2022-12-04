clc
clear
close
%r = 1;
%L = 1;
X = [20 0.4];
U1 = [];
U2 = [];
Z = [];
Time = [0];
choice_input = 1;
if choice_input == 1    % piecewise constant input profile
    u1 = [0.6613];
    u2 = [0.5];
    tinterval=5;
elseif choice_input==2      % sinusoidal input profile
    gen=linspace(-1*pi, 1*pi,100);
    u1 = cos(gen);
    u2 = sin(gen);
    tinterval=1;
end
hold on
for i=1:length(u1)
    tspan = tinterval*[(i-1) i];
    x0 = X(end,:)';
    if choice_input==1
        Z=[Z x0];
    end
    % notice that the inputs are given as constants u1(i), u2(i)
    % that is why ode45 is called within the loop many times
    [t,x]=ode45(@(t,x) nonlinear_system(t,x,u1(i),u2(i)),tspan,x0);
    X=[X;x];
    U1=[U1; u1(i)*ones(length(t),1)];
    U2=[U2; u2(i)*ones(length(t),1)];
    Time=[Time;t];
end
plot(Time,X(:,1), 'LineWidth',2)   %visualization
plot(Time,X(:,2), 'LineWidth',2)
%plot(Time,X(:,3), 'LineWidth',2)
legend('x_1', 'x_2')
xlabel('time(sec)')
grid on
box on
figure
plot(X(:,1),X(:,2),'-k','Linewidth', 2)
hold on
xlabel('x_1')
ylabel('x_2')
box on
if choice_input==1
    Z=[Z X(end,:)'];
    plot(Z(1,:),Z(2,:),'o', 'Linewidth',5)
    legend('Robot trajectory', 'change of inputs')
else
    legend('robot trajectory')
end
title(' ')
figure
hold on
plot(Time(2:end), U1,'Linewidth', 2)
plot(Time(2:end), U2,'Linewidth', 2)
legend('u_1','u_2')
xlabel('time(sec)')
ylabel('inout profile')
grid on
box on











