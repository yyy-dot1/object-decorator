class Kitchen:
    def __init__(self,name,use):
        self.name = name
        self.use = use

    def display(self):
        print(f"材料:{self.name},調理方法:{self.use}")

class Food(Kitchen):
    def __init__(self,name):
        self.food_name = name

class Cook(Kitchen):
    def __init__(self,cook):
        self.how_cook = cook

tomato = Food("トマト") 
cut = Cook("切る")
egg = Food("卵")
fry = Cook("焼く")
rice = Food("お米")
wrap = Cook("包む")


# cook = Kitchen(tomato,cut) #オブジェクトそのもの
cook1 = Kitchen(tomato.food_name,cut.how_cook) #オブジェクトが持っている中身
cook2 = Kitchen(egg.food_name,fry.how_cook)
cook3 = Kitchen(rice.food_name,fry.how_cook)
cook4 = Kitchen(egg.food_name,wrap.how_cook)

cook1.display()
cook2.display()
cook3.display()
cook4.display()