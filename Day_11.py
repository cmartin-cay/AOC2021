from dataclasses import dataclass, field

flash_counter: int = 0


@dataclass
class Octopus:
    value: int
    x: int
    y: int
    neighbors: list["Octopus"] = field(default_factory=list, repr=False)
    has_flashed: bool = False

    def __post_init__(self):
        pass

    def step(self):
        self.value += 1

    def increase_from_flash(self):
        if not self.has_flashed:
            self.value += 1
        else:
            pass

    def flash(self):
        if self.value > 9:
            self.has_flashed = True

    def clean_up(self):
        if self.value > 9:
            self.value = 0
        self.has_flashed = False

    def generate_neighbors(self):
        all_neighbors = [octo for octo in octo_list if octo.x in (self.x + 1, self.x, self.x - 1) and octo.y in (self.y + 1, self.y, self.y - 1)]
        original = [octo for octo in all_neighbors if octo.x == self.x and octo.y == self.y]
        self.neighbors = [x for x in all_neighbors if x not in original]


octo1 = Octopus(value=1, x=0, y=0)
octo2 = Octopus(value=1, x=-1, y=-1)
octo3 = Octopus(value=1, x=0, y=-1)
octo4 = Octopus(value=1, x=1, y=-1)
octo5 = Octopus(value=1, x=1, y=0)
octo6 = Octopus(value=1, x=1, y=1)
octo7 = Octopus(value=1, x=0, y=1)
octo8 = Octopus(value=1, x=-1, y=1)
octo9 = Octopus(value=1, x=-1, y=0)
octo10 = Octopus(value=1, x=2, y=2)

octo_list = [octo1, octo2, octo3, octo4, octo5, octo6, octo7, octo8, octo9, octo10]


for each in octo_list:
    each: Octopus
    each.generate_neighbors()

print(len(octo6.neighbors))
print(octo6.neighbors)