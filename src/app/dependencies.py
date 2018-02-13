
# Dependency Injection


class DI(object):
    def __init__(self):
        self.container = {}

    def get(self, dependency):
        return self.container.get(dependency)

    def set(self, dependency, value):
        self.container[dependency] = value

    def containers(self):
        return self.container.keys()
