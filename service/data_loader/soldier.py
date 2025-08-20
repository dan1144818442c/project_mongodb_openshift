

class Soldier:

    def __init__(self, id, first_name, last_name, rank, phone_number):
        self.id  = id
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.phone_number = phone_number

    def get_dict_person(self):
        return {"id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "rank": self.rank,
                "phone_number": self.phone_number}
