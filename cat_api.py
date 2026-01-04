import requests
from cat_logic import CatGoods

def get_cat_fact():
    # 猫の豆知識をくれる無料API
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        return response.json()["fact"]
    return "豆知識が取得できませんでした。"

def sell(self,count):
    if self.stock >= count:
        self.stock -= count
        print("お買い上げありがとうございます!")
        print(get_cat_fact())
    else:
        print(f"在庫が足りません！不足{self.stock}個")

goods_data = ["猫耳カチューシャ",1500,10]
item = CatGoods.from_list(goods_data)

item.sell(3)
item.sell(10)