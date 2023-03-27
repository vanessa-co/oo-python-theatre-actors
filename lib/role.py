from .audition import Audition

class Role:
  
    def __init__(self, character_name):
        self.character_name = character_name

    @property
    def auditions(self):
        return [audition for audition in Audition.all_auditions if audition.role == self]

    @property
    def actors(self):
        return list({audition.actor.name for audition in self.auditions})

    @property
    def locations(self):
        return list({audition.location for audition in self.auditions})

    @classmethod
    def get_silver_screen(cls):
        hired_characters = []
        for audition in Audition.all_auditions:
            if audition.hired and audition.role.character_name not in hired_characters:
                hired_characters.append(audition.role.character_name)
        return hired_characters

    @property
    def silver_screen(self):
        return self.get_silver_screen()