class BasicCommander:
    """ Basic class for all Commanders, contains common methods for all commanders"""

    presence = 0

    def __init__(self):
        self.name: str = "empty"
        self.cost: int = 0
        self.special = {}

    def get_cost_of_commander(self):
        """ Returns current commander cost"""

        return self.cost

    def get_name_of_commander(self):
        """ Returns current commander name"""

        return self.name

    def get_skills_of_commander(self):
        skills = "  "
        for k in self.special:
            skills = skills + str(k) + ", "
        return skills[0:-2]
