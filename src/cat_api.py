import requests
from cat_logic import CatGoods

class CatGoods:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    @property
    def price_with_tax(self):
        return int(self.price * 1.1)

    @property
    def is_instock(self):
        return self.stock > 0

    @classmethod
    def from_list(cls,data_list):
        return cls(data_list[0],data_list[1],data_list[2])

    def get_cat_fact(self):
        try:
            response = requests.get("https://catfact.ninja/fact")
            return response.json()["fact"]
        except:
            return "猫は可愛い"

    def sell(self,count):
        if self.stock >= count:
            self.stock -= count
            print("お買い上げありがとうございます!")
            fact = self.get_cat_fact()
            print(f"猫の豆知識:{fact}")
        else:
            print(f"在庫が足りません！不足{self.stock}個")

goods_data = ["猫耳カチューシャ",1500,10]
item = CatGoods.from_list(goods_data)

item.sell(3)
item.sell(10)