from island import Island


def main(arg):
    for island in arg:
        print str(island.get_volume())


if __name__ == '__main__':

    islands = []
    number_of_island = input("Please enter a number of islands: ")
    for i in range(number_of_island):
        dimensions = raw_input('Enter the dimensions of the island:')
        dimensions = dimensions.split(' ')
        N = int(dimensions[0])
        M = int(dimensions[1])
        landscape = []
        for i in range(N):
            landscape.append([])
            raw = raw_input().split(' ')
            for j in range(M):
                altitude = int(raw[j])
                landscape[i].append(altitude)
        island = Island(landscape)
        islands.append(island)
    main(islands)
