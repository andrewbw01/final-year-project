function [xCoord,yCoord,xMCoord,yMCoord] = newCoords(Vx,Vy,psi,X,Y,VxM,VyM,mpsi,Xm,Ym)%newCoords(Vx,Vy,psi,X,Y,VxM,VyM,mpsi,Xm,Ym)
%Own ship
X(1)=X;
Y(1)=Y;
xCoord(1) = Vx.*sin(psi) + cos(psi) + X(1);
yCoord(1) = Vy.*sin(psi) + cos(psi) + Y(1);
%Other Ship
Xm(1)=Xm;
Ym(1)=Ym;
xMCoord(1) = VxM.*sin(mpsi) + cos(mpsi) + Xm(1);
yMCoord(1) = VyM.*sin(mpsi) + cos(mpsi) + Ym(1);

for i=2:50
X(i)=xCoord(i-1);
Y(i)=yCoord(i-1);
xCoord(i) = Vx.*sin(psi) + cos(psi) + X(i);
yCoord(i) = Vy.*sin(psi) + cos(psi) + Y(i);

Xm(i)=xMCoord(i-1);
Ym(i)=yMCoord(i-1);
xMCoord(i) = VxM.*sin(mpsi) + cos(mpsi) + Xm(i);
yMCoord(i) = VyM.*sin(mpsi) + cos(mpsi) + Ym(i);
end

if xMCoord(i) == xCoord(i) && yMCoord(i)== yCoord(i)
    disp("HIT")
    disp(xMCoord(i))
    disp(xCoord(i))
end

%allCoords = [xCoord,yCoord,xMCoord,yMCoord];

end