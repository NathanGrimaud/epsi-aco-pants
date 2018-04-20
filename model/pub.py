class Pub():
    name = None
    # (easting, northing)
    location = (None, None)

    def __init__(self, name, easting, northing):
        self.name = name
        self.location = (int(easting), int(northing))
