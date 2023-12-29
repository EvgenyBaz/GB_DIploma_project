class BasicCommander:
    """ Basic class for all Commanders, contains common methods for all commanders"""

    presence: int = 0

    def __init__(self):
        self.name: str = "empty"
        self.cost: int = 0
        self.special: set[str] = {
            "property"
        }

    def get_cost_of_commander(self) -> int:
        """

        :return: current commander cost
        """

        return self.cost

    def get_name_of_commander(self) -> str:
        """

        :return: current commander name
        """

        return self.name

    def get_skills_of_commander(self) -> str:
        """

        :return: string with commander skills"
        """

        skills = "  "
        for k in self.special:
            skills = skills + str(k) + ", "
        return skills[0:-2]
