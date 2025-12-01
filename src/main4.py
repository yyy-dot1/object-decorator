
def log_print(f):
    def _wrapper(*args, **keywards):
        print(f"{f.__name__}関数の開始")  
        result = f(*args, **keywards)
        print(f"{f.__name__}関数の終了") 
        return result
    return _wrapper

class Kitchen:
    def __init__(self,name,use):
        self.name = name
        self.use = use

    @log_print
    def display(self):
        print(f"材料:{self.name},調理方法:{self.use}")

    @classmethod
    def create_from_id(cls,food_id,date):
        # print(cls) # <class '__main__.Expiry'>
        if food_id == 1:
            name_data = tomato.get_name()
            # print(date) #2026-01-15
            expiry_data = date
        elif food_id == 2:
            name_data = corn.get_name()
            # print(date) #2025-01-08
            expiry_data = date
        elif food_id == 3:
            name_data = rice.get_name()
            # print(date) #2025-01-08
            expiry_data = date
        else:
            raise ValueError("無効なIDです")
        return cls(name_data,expiry_data)

class Food(Kitchen):
    def __init__(self,name):
        self.food_name = name
    @log_print
    def get_name(self,prefix=""):
        return prefix + self.food_name
    
    @log_print
    def set_stock(self,quantity):
        self.quantity = quantity
        return f"【在庫情報】 品目:{self.food_name},数量:{quantity}"
    
class Expiry(Kitchen):
    def __init__(self,name,expiry_date):
        self.name = name
        self.expiry_date = expiry_date
         
class Cook(Kitchen):
    def __init__(self,cook):
        self.how_cook = cook
    
    def get_use(self,prefix=""):
        return prefix + self.how_cook

log_without_decorater = log_print(Cook("焼く").get_use)

print(f"log_without_decorater:{log_without_decorater()}")

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

stock = egg.set_stock(4)
print(stock)

stock = tomato.set_stock(10)
print(stock)

food_1= Expiry.create_from_id(1,"2026-01-15")
food_2 = Expiry.create_from_id(2,"2025-01-08")
food_3 = Expiry.create_from_id(3,"2025-01-08")

print(f"ID 1:{food_1.name}(期限:{food_1.expiry_date})")
#print(f"ID 2:{food_2.name}(期限:{food_2.expiry_date})")
# print(f"ID 3:{food_3.name}(期限:{food_3.expiry_date})")