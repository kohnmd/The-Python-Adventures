class plateau:
    """
    The plateau class keeps track of the bounds of the plateau and can check
    whether a given coordinate is within those bounds.
    """

    def __init__(self, x_limit, y_limit):
        """
        Store the edges as a tuple. They don't need to be mutable.
        Does that make sense? Or should these be their own properties?
        """
        self.edges = (x_limit, y_limit)


    def x_edge(self):
        return self.edges[0]


    def y_edge(self):
        return self.edges[1]


    def in_bounds(self, x, y):
        """
        We're going to assume x_edge and y_edge are always positive. This could
        be built out a little more to allow for multiple plateau quadrants.
        """
        return x <= self.x_edge() and y <= self.y_edge()


    def __repr__(self):
        return '<plateau edges:(%s, %s)>' % (self.x_edge(), self.y_edge())




class cardinal:
    """
    There's enough data associated with the four cardinal directions that I
    think they deserve their own class.
    """

    def __init__(self, direction, axis, positive):
        self.direction = direction
        self.axis = axis
        self.positive = positive


    def __eq__(self, other):
        """
        Allows simple strings to be evaluated against this object's direction,
        e.g. cardinal_obj == 'N'
        """
        return self.direction == other


    def __str__(self):
        return self.direction



class rover:
    cardinals = (
        cardinal('N', 'y', True),
        cardinal('E', 'x', True),
        cardinal('S', 'y', False),
        cardinal('W', 'x', False)
    )


    def __init__(self, x, y, cardinal, steps, plateau):
        self.x = int(x)
        self.y = int(y)
        self.cardinal_index = self.get_cardinal_index_by_direction(cardinal)
        self.steps = steps
        self.step_index = 0
        self.plateau = plateau


    def move(self):
        """
        Moves the rover until the list of steps/instructions are complete.
        """
        while self.get_next_step() is not None:
            self.take_next_step()


    def get_next_step(self):
        try:
            return self.steps[self.step_index]
        except:
            return None


    def take_next_step(self):
        next_step = self.get_next_step()
        if next_step == 'L':
            status = self.turn_left()
        elif next_step == 'R':
            self.turn_right()
        elif next_step == 'M':
            self.move_forward()

        if next_step is not None:
            self.step_index += 1

        #print repr(self)


    def turn_left(self):
        if self.cardinal_index == 0:
            self.cardinal_index = len(self.cardinals) - 1
        else:
            self.cardinal_index -= 1
        #print 'left'



    def turn_right(self):
        if self.cardinal_index >= len(self.cardinals)-1:
            self.cardinal_index = 0
        else:
            self.cardinal_index += 1
        #print 'right'


    def move_forward(self):
        next_x = self.x
        next_y = self.y
        current_cardinal = self.get_current_cardinal()
        if current_cardinal.axis == 'x':
            if current_cardinal.positive:
                next_x += 1
            else:
                next_x -= 1
        elif current_cardinal.axis == 'y':
            if current_cardinal.positive:
                next_y += 1
            else:
                next_y -= 1

        if self.plateau.in_bounds(next_x, next_y):
            self.x = next_x
            self.y = next_y
            #print 'forward'
        #else:
            #print 'forward failed'


    def get_cardinal_index_by_direction(self, cardinal):
        """
        Set direction the rover is facing by storing a reference to the index of
        the cardinal object inside of the cardinals tuple.
        """
        try:
            return self.cardinals.index(cardinal)
        except:
            return None


    def get_current_cardinal(self):
        """
        Get the cardinal object that corresponds to the direction the rover is
        currently facing.
        """
        try:
            return self.cardinals[self.cardinal_index]
        except:
            return None


    def get_current_position(self):
        """
        Get a tuple of the rover's current coordinates and the cardinal
        direction it's facing.
        """
        return (self.x, self.y, str(self.get_current_cardinal()))


    def __str__(self):
        return str(self.get_current_position())


    def __repr__(self):
        return '<rover coordinates:(%i, %i) direction:%s steps:%s next_step:%s>' % (self.x, self.y, str(self.get_current_cardinal()), "".join(self.steps), self.get_next_step())




def parse_file(filename):
    """
    Extract plateau edges, and rover coordinates & steps from data file
    """

    # Get file contents
    file = open(filename, "r")
    input_list = file.read().splitlines()
    file.close()

    # Get plateau edge coordinates
    try:
        plateau_coordinates = input_list[0].split()
        plateau_data = {
            'x_edge': plateau_coordinates[0],
            'y_edge': plateau_coordinates[1]
        }
    except:
        sys.exit('Invalid input')

    # Get rover data
    # Use batch_gen() to get two lines of the input_list at a time
    rovers_data = []
    for rover_data in batch_gen(input_list[1:], 2):
        try:
            rover_start_params = rover_data[0].split()
            rovers_data.append({
                'start_x': rover_start_params[0],
                'start_y': rover_start_params[1],
                'start_cardinal': rover_start_params[2],
                'steps': list(rover_data[1])
            })
        except:
            sys.exit('Invalid input')

    return {
        'plateau_data': plateau_data,
        'rovers_data': rovers_data
    }




def batch_gen(data, batch_size):
    """
    This awesomeness courtesy of http://stackoverflow.com/a/760857
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]




def main():
    data = parse_file('input.dat')

    the_plateau = plateau(data['plateau_data']['x_edge'], data['plateau_data']['x_edge'])
    rovers = []
    for rover_data in data['rovers_data']:
        rovers.append(
            rover(rover_data['start_x'], rover_data['start_y'], rover_data['start_cardinal'], rover_data['steps'], the_plateau)
        )

    for the_rover in rovers:
        the_rover.move()
        print str(the_rover.get_current_position())




if __name__ == '__main__':
    import sys
    main()
