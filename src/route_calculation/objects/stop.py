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

    def add_neighbor(self, stop: "Stop", distance: float):
        if not self.is_neighbor(stop):
            self.neighbors[stop] = distance
            stop.add_neighbor(self, distance)

    def is_neighbor(self, stop: "Stop"):
        return stop in self.neighbors.keys()

    def get_distance_with(self, stop: "Stop"):
        if self.is_neighbor(stop):
            return self.neighbors[stop]
        else:
            pass  # dijkstra

    # def SommetMini(self, D):


def get_stop_with_name(name: str):
    for stop in stops:
        if stop.name.casefold() == name.casefold():
            return stop


def get_stop_with_id(id: int):
    return stops[id]


stops: list[Stop]
