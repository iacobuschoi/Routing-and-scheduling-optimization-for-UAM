class Request:
    def __init__(self, id, source, destination, start_time, latest_time):
        self.id = id
        self.source = source
        self.destination = destination
        self.start_time = start_time
        self.latest_time = latest_time