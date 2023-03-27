from .audition import Audition


class Actor:
    def __init__(self, name):
        self.name = name

    @property
    def auditions(self):
        return [audition for audition in Audition.all_auditions if audition.actor == self]

    @property
    def roles(self):
        return list({audition.role for audition in self.auditions})

    @property
    def characters(self):
        return list({role.character_name for role in self.roles})

    @property
    def paychecks(self):
        hired_characters = list({audition.role.character_name for audition in self.auditions if audition.hired})
        return hired_characters if hired_characters else "No hired characters"

