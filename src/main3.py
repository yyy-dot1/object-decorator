def shop_manager(f):
    def _wrapper(*args, **keywards):

        print(f"店舗:{f.__name__}の在庫・名簿を更新します。")
        
        v = f(*args, **keywards)
        
        print(f"【更新完了】{v}")
        return v
    return _wrapper

@shop_manager
def cat_staff(key3,*args, **keyawrds):

    print(f"key3: {key3}") 
    print(f"args: {args}") 
    print(f"keyawrds:{keyawrds}")

    print(f"-----登録ID: {args} -------")
    
    s = ""
    for key in keyawrds:
        s += f"[{key}:{keyawrds[key]}]"
    return f"猫スタッフ名簿: {s}"

cat_staff = shop_manager(cat_staff)
    
@shop_manager
def cafe_menu():
    return "肉球ラテ, 猫耳ケーキ, またたび茶"

@shop_manager
def cat_goods():
    return "猫柄ポーチ, 爪とぎポストカード, 猫耳カチューシャ"

cat_staff(1, 2, 3)
cat_staff(key1=1, key2=2, key3=3)
cat_staff(101, 名前="たま", 種類="三毛猫", 性格="甘えん坊")
cat_staff(102, 名前="くろ", 種類="黒猫", 担当="お出迎え")

cafe_menu()
cat_goods()