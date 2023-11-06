class Stop:
    def __init__(self, name: str, neighbors: dict):
        global stops
        try:
            self.id = len(stops)
        except NameError:
            self.id = 0
            stops = []
        self.name = name
        self.neighbors = neighbors

    def add_neighbor(self, neighbor: "Stop", distance: float):
        """
        Add a neighbor mutually to a stop.

        :param neighbor: Stop
        :param distance: Distance between the neighbor and itself.
        """
        if not self.is_neighbor(neighbor):
            self.neighbors[neighbor] = distance
            neighbor.add_neighbor(self, distance)

    def is_neighbor(self, stop: "Stop") -> bool:
        """
        Check if a stop is a neighbor of this.

        :param stop: The stop to check
        :return: Boolean
        """
        return stop in self.neighbors.keys()

    def get_distance_with_neighbor(self, neighbor: "Stop") -> float:
        """
        Get the distance between 2 neighbors.

        :param neighbor: Stop
        :return: Distance between
        """
        if self.is_neighbor(neighbor):
            return self.neighbors[neighbor]


def get_stop_with_name(name: str) -> Stop:
    for stop in stops:
        if stop.name.casefold() == name.casefold():
            return stop


def get_stop_with_id(id: int) -> Stop:
    return stops[id]


stops: list[Stop]
