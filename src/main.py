
class Kitchen:
    def __init__(self,name,use):
        self.name = name
        self.use = use

    def display(self):
        print(f"材料:{self.name},調理方法:{self.use}")

class Food(Kitchen):
    def __init__(self,name):
        self.food_name = name

    def get_name(self,prefix=""):
        return prefix + self.food_name

class Cook(Kitchen):
    def __init__(self,cook):
        self.how_cook = cook

    def get_use(self,prefix=""):
        return prefix + self.how_cook


tomato = Food("トマト") 
cut = Cook("切る")
corn = Food("とうもろこし")
egg = Food("卵")
fry = Cook("焼く")
rice = Food("お米")
wrap = Cook("包む")

cook1 = Kitchen(
    name=tomato.get_name(),
    use=cut.get_use()
)

cook2 = Kitchen(
    name=corn.get_name(),
    use=fry.get_use()
)

cook3 = Kitchen(
    name=rice.get_name(),
    use=fry.get_use()
)

cook4 = Kitchen(
    name=egg.get_name("半熟の"),
    use=wrap.get_use("優しく")
)

cook1.display()
cook2.display()
cook3.display()
cook4.display()