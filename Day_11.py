from dataclasses import dataclass, field
from math import floor

flash_counter: int = 0
sync: bool = False


@dataclass
class Octopus:
    value: int
    x: int
    y: int
    neighbors: list["Octopus"] = field(default_factory=list, repr=False)
    has_flashed: bool = False

    def step(self):
        self.value += 1
        self.flash()

    def increase_neighbors(self):
        for octo in self.neighbors:
            if not octo.has_flashed:
                octo.value += 1
            else:
                pass

    def flash(self):
        if self.value > 9 and not self.has_flashed:
            self.has_flashed = True
            global flash_counter
            flash_counter += 1

    def clean_up(self):
        if self.value > 9:
            self.value = 0
        self.has_flashed = False

    def generate_neighbors(self):
        all_neighbors = [
            octo
            for octo in octo_list
            if octo.x in (self.x + 1, self.x, self.x - 1)
               and octo.y in (self.y + 1, self.y, self.y - 1)
        ]
        original = [
            octo for octo in all_neighbors if octo.x == self.x and octo.y == self.y
        ]
        self.neighbors = [x for x in all_neighbors if x not in original]


with open("Day_11.txt") as in_file:
    starting = in_file.read()
octo_list = []
square = 10
for idx, num, in enumerate(starting):
    octo_list.append(Octopus(value=int(num), x=floor(idx / square), y=idx % square))

# octo1 = Octopus(value=1, x=0, y=0)
# octo2 = Octopus(value=9, x=-1, y=-1)
# octo3 = Octopus(value=9, x=0, y=-1)
# octo4 = Octopus(value=9, x=1, y=-1)
# octo5 = Octopus(value=9, x=1, y=0)
# octo6 = Octopus(value=9, x=1, y=1)
# octo7 = Octopus(value=9, x=0, y=1)
# octo8 = Octopus(value=9, x=-1, y=1)
# octo9 = Octopus(value=9, x=-1, y=0)
#
# octo_list = [octo1, octo2, octo3, octo4, octo5, octo6, octo7, octo8, octo9]

for each in octo_list:
    each: Octopus
    each.generate_neighbors()


def cave_step():
    # Step 1: Increase everyone
    [octo.step() for octo in octo_list]
    # Step 2: Make a list of everyone that gone over 9
    flashed_list = [octo for octo in octo_list if octo.has_flashed]
    while flashed_list:
        # Step 3: Flash everyone that went over 9
        current_octo = flashed_list.pop()
        current_octo.increase_neighbors()
        # Step 3a: Deal with neighbors that have flashed
        for octo in current_octo.neighbors:
            if octo.value > 9 and not octo.has_flashed:
                octo.flash()
                flashed_list.append(octo)
    # Step 4: Reset everyone for the next round
    [octo.clean_up() for octo in octo_list]


steps = 1
while True:
    cave_step()
    if (sum(octo.value for octo in octo_list)) == 0:
        break
    steps += 1
print(steps)
