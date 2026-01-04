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
        
        # name = data_list[0]
        # price = data_list[1]
        # stock = data_list[2]

        # return cls(name,price,stock)

        return cls(data_list[0],data_list[1],data_list[2])

    #@classmethodをつけると、そのメソッドが受け取る最初の引数はself(個別の商品)ではなく、cls（クラスそのもの)になる。
    def sell(self,count):
        if self.stock >= count:
            self.stock -= count
            print("お買い上げありがとうございます!")
        else:
            print(f"在庫が足りません！不足{self.stock}個")


goods_data = ["猫耳カチューシャ",1500,10]
item = CatGoods.from_list(goods_data)

item.sell(3)
item.sell(10)

print(f"商品名:{item.name}")
print(f"税抜価格: {item.price}円")
print(f"税込価格: {item.price_with_tax}円")

if item.is_instock:
    print(f"在庫状況:あり(残り{item.stock}個)")
