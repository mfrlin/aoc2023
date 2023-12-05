class MapPart:
    def __init__(self, destination, source, range_length):
        self.destination = destination
        self.source = source
        self.range_length = range_length
        self.range_ = range(source, source + range_length)

    def __repr__(self):
        return f'MapPart(destination={self.destination}, source={self.source}, range_length={self.range_length})'

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

with open('input.txt') as f:
    current_map = None
    for l in f:
        l = l.strip()
        if l.startswith('seeds'):
            seeds = list(map(int, l[7:].split(' ')))
            continue
        if l.startswith('seed-to-soil'):
            current_map = seed_to_soil
            continue
        if l.startswith('soil-to-fertilizer'):
            current_map = soil_to_fertilizer
            continue
        if l.startswith('fertilizer-to-water'):
            current_map = fertilizer_to_water
            continue
        if l.startswith('water-to-light'):
            current_map = water_to_light
            continue
        if l.startswith('light-to-temperature'):
            current_map = light_to_temperature
            continue
        if l.startswith('temperature-to-humidity'):
            current_map = temperature_to_humidity
            continue
        if l.startswith('humidity-to-location'):
            current_map = humidity_to_location
            continue
        if not l:
            continue
        destination, source, range_length = map(int, l.split(' '))
        current_map.append(MapPart(destination, source, range_length))



# PART 1
# locations = []
# for seed in seeds:
#     location = seed
#     for m in maps:
#         for part in m:
#             if location in part.range_:
#                 location = part.destination + (location - part.source)
#                 break
#     locations.append(location)
#
# print('min location', min(locations))

# PART 2
min_location = None
for seed_start, seed_range in zip(seeds[::2], seeds[1::2]):
    seed = seed_start
    while seed < (seed_start + seed_range):
        can_skip = None
        location = seed
        for m in maps:
            for part in m:
                if location in part.range_:
                    could_skip = part.range_.stop - location
                    if can_skip is None or could_skip < can_skip:
                        can_skip = could_skip
                    location = part.destination + (location - part.source) 
                    break
        if min_location is None or location < min_location:
            min_location = location
        seed += can_skip

print(min_location)

