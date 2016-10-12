import numpy


class Island:
    __water_volume = 0

    def __init__(self, landscape):
        self.__landscape = landscape

    @staticmethod
    def calculate_lowland_volume(landscape, x0, y0):
        volume = 0
        q = [[x0, y0]]
        lowlands_positions = []
        while q:
            (x, y), q = q[0], q[1:]
            if x == 0 or y == 0 or x == len(landscape[0]) - 1 or y == len(landscape) - 1:
                # The lake is connected with the sea
                for (x, y) in lowlands_positions:
                    landscape[y][x] = -1
                return 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx * dy != 0 or dx + dy == 0:
                        continue
                    xx, yy = x + dx, y + dy
                    if landscape[yy][xx] < 0:
                        # The lake is connected with the sea
                        for (x, y) in lowlands_positions:
                            landscape[y][x] = -1
                        return 0
                    if landscape[yy][xx] == 0:
                        landscape[yy][xx] = 1
                        volume += 1
                        q.append([xx, yy])
                        lowlands_positions.append([xx, yy])
        if volume == 0:
            volume = 1
            landscape[y0][x0] = 1
        return volume

    @staticmethod
    def calculate_lowest_lowland(landscape):
        a = landscape
        height = 1000
        for i in range(1, len(a) - 1):
            for j in range(1, len(a[0]) - 1):
                if 0 < a[i][j] < height:
                    height = a[i][j]
        return height

    def get_volume(self):
        a = self.__landscape
        volume = 0
        if len(a) < 3 or len(a[0]) < 3:
            return volume
        lowland_is_left = False
        while not lowland_is_left:
            lowland_is_left = True
            min_height = self.calculate_lowest_lowland(a)
            a = numpy.array(a) - min_height
            for i in range(1, len(a) - 1):
                for j in range(1, len(a[0]) - 1):
                    if a[i][j] == 0:
                        lowland_is_left = False
                        volume += self.calculate_lowland_volume(a, j, i)

        return volume


if __name__ == '__main__':
    a = [
        [0, 5, 6, 5, 5, 5, 5, 5, 6, 5, 5, 1, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 2, 5, 5, 5, 5, 5, 5, 5],
        [2, 5, 5, 5, 2, 1, 2, 5, 5, 5, 5, 5, 5],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    ]

    island = Island(a)
    print str(island.get_volume())

# land = raw_input('Input land: ')
# land = [int(n) for n in land.split(' ')]
