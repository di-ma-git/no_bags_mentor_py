from pet import Pet


class PetApp:
    _app_name:str
    _pets: {}

    def __init__(self, name: str):
        self._app_name = name
        self._pets = {}

    def add_pet(self, pet: Pet):
        self._pets[pet.pet_id] = pet

    def remove_pet(self, pet: Pet):
        del self._pets[pet.pet_id]

    def show_all_pets(self):
        for pet in self._pets.values():
            print(f"{pet.get_type()}: {pet.get_name()}")