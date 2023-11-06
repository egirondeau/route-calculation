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

    def get_neighbor(self, stop: Stop):
        for i in range(len(G[0])):
            neighbor=[0]
            return neighbor

    def get_distance_with(self, stop: Stop):
        if stop==neighbor:
            return distance
        else:
            pass #dijkstra

    def 

bus_lines: list[BusLine]


def get_bus_line_with_id(id: int):
    return bus_lines[id]
