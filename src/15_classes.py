# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return 'latitude: {self.lat} \n longitude: {self.lon}'.format(self=self) 
         
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def _init_(self, name, lat, lon):
        self.name = name
        super(LatLon, self)._init_(self, lat, lon)
    def __str__(self):
        return 'latitude: {self.lat} \n longitude: {self.lon} \n name: {self.name}'.format(self=self) 
        



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def _init_(self, name, lat, lon, difficulty, size):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.difficulty = difficulty
        self.size = size
        super(Waypoint, self)._init_(self, name, lat, lon)
    def __str__(self):
        return 'latitude: {self.lat} \n longitude: {self.lon} \n name: {self.name} \n difficulty: {self.difficulty} \n size: {self.size}'.format(self=self) 
        

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(41.70505, -121.51521)
waypoint.name = "Catacombs"


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(44.052137, -121.41556)
geocache.name = "Newberry Views"
geocache.difficulty = 1.5
geocache.size = 2

# Print it--also make this print more nicely
print(geocache)
