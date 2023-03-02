% Set up the initial positions of the red ship and obstacle
red_ship_position = [0, 20];
obstacle_position = [-10, 5];

% Set up the velocity vectors for the red ship and obstacle
red_ship_velocity = [0, -3];
obstacle_velocity = [2 , 0];

% Set up the time step and the duration of the simulation
dt = 0.1;
t_end = 20;

% Set up the path array to store the positions of the red ship during movement
path = red_ship_position;

% Loop over each time step of the simulation
for t = 0:dt:t_end
    % Update the positions of the red ship and obstacle based on their velocities
    red_ship_position = red_ship_position + red_ship_velocity .* dt;
    obstacle_position = obstacle_position + obstacle_velocity .* dt;

    % Check if the red ship has crossed the path of the obstacle
    if red_ship_position(2) < obstacle_position(2) + 5 && ...
       red_ship_position(2) > obstacle_position(2) && ...
       red_ship_position(1) < obstacle_position(1) + 5 && ...
       red_ship_position(1) > obstacle_position(1)

        % Determine the distance between the red ship and the obstacle
        distance = norm(red_ship_position - obstacle_position);

        % If the red ship is too close to the obstacle, move in a semicircle around the obstacle
        if distance < 5

            % Calculate the angle between the red ship and the obstacle
            angle = atan2(red_ship_position(2) - obstacle_position(2), red_ship_position(1) - obstacle_position(1));
            
            % Determine the position of the center of the arc
            center = obstacle_position + [0, 5];
            
            % Calculate the radius of the arc
            radius = 1.5;

            % Calculate the new velocity vector for the red ship
            if angle >= 0 && angle < pi
                % Move to the left of the obstacle
                red_ship_velocity = [(red_ship_position(1)-center(1)), (red_ship_position(2)-center(2))] .* [-1, 1] / radius .* 3;
            else
                % Move to the right of the obstacle
                red_ship_velocity = [(red_ship_position(1)-center(1)), (red_ship_position(2)-center(2))] .* [1, -1] / radius .* 3;
            end

        % If the red ship is not too close to the obstacle, move towards it
        else
            red_ship_velocity = [0, -3];
        end

    % If the red ship has not crossed the path of the obstacle, move towards it
    else
        red_ship_velocity = [0, -3];
    end

    % Store the position of the red ship in the path array
    path = [path; red_ship_position];

    % Plot the positions of the red ship and obstacle
    plot(path(:,1), path(:,2), 'r--')
    hold on
    plot(red_ship_position(1), red_ship_position(2), 'ro', 'MarkerSize', 10)
    plot(obstacle_position(1), obstacle_position(2), 'bo', 'MarkerSize', 10)
    xlim([-15, 15])
    ylim([-5, 25])
    pause(0.1)
    hold off
end

% After the obstacle has moved, continue moving the red ship towards its final position
while red_ship_position(2) > 0
    % Determine the distance between the red ship and the final position
    distance = norm(red_ship_position - [0, 0]);

    % If the red ship is too far from the final position, move towards it
    if distance > 0.5
        red_ship_velocity = [-1, -3]
    else
        red_ship_velocity = [0, -3];
    end

    % Update the position of the red ship based on its velocity
    red_ship_position = red_ship_position + red_ship_velocity .* dt;
    path = [path; red_ship_position];

    % Plot the positions of the red ship and obstacle
    plot(path(:,1), path(:,2), 'r--')
    hold on
    plot(red_ship_position(1), red_ship_position(2), 'ro', 'MarkerSize', 10)
    plot(obstacle_position(1), obstacle_position(2), 'bo', 'MarkerSize', 10)
    xlim([-15, 15])
    ylim([-5, 25])
    pause(0.1)
    hold off
end

