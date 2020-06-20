class Point():
    def __init__(self, name, latitude, longitude):
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    def get_lat_long(self):
        return (self._latitude, self._longitude)
