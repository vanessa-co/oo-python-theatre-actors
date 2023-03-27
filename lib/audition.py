
class Audition:
    all_auditions = []
    
    def __init__(self, location, role, actor, hired=True):
        self.location = location
        self.role = role
        self.actor = actor
        self.hired = hired
        self.all_auditions.append(self)

    def call_back(self):
        self.hired = True