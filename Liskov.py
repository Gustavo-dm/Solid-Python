class Bird:
    def fly(self):
        print("Flying")

    def get_color(self):
        return "Unknown"


class Duck(Bird):
    def fly(self):
        print("Flying like a duck")

    def get_color(self):
        return "Brown"


class Penguin(Bird):
    # Applying Liskov Substitution principle

    def fly(self):
        raise NotImplementedError("Penguins cannot fly")

    def get_color(self):
        return "Black and white"


def process_bird(bird):
    bird.fly()
    color = bird.get_color()
    print("Color:", color)
