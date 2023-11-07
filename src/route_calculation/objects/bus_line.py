from route_calculation.objects.stop import Stop


class BusLine:
    def __init__(self, name: str, stops: list[Stop], speed: float):
        global bus_lines
        try:
            self.id = len(bus_lines)
        except NameError:
            self.id = 0
            bus_lines = []
        bus_lines.append(self)
        self.name = name
        self.stops = stops
        self.speed = speed

    def insert_stop(self, index: int, stop: Stop):
        self.stops.insert(index, stop)

    def get_distance_between(self, stop1: Stop, stop2: Stop) -> float:
        distance=0
        if stop1==stop2:
            return 0
        elif stop1==neighbor:
            return self.get_distance_between()
        else:
            distance.append(self.neighbor(stop1))
            return self.get_distance_between()
        """
        Retrieve the distance between 2 stops belonging to the bus line.

        :param stop1:
        :param stop2:
        :return: Distance
        """


bus_lines: list[BusLine]


def get_bus_line_with_id(id: int):
    return bus_lines[id]
