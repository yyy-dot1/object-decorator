# main_program.py

# 💡 インポート！
# "cooking_module.py" から Kitchen クラスと run() 関数をインポートします。
# 拡張子 (.py) は付けません。
import cooking_module

def utilize_classes():
    print(">>> main_program.py が独自の処理を実行します <<<")
    
    # 1. run() 関数を呼び出す
    # cooking_module で定義された run() が実行される
    print("\n--- run() 関数を呼び出し ---")
    cooking_module.run()
    
    # 2. Kitchen クラスを直接利用する
    # モジュール名.クラス名 でアクセスする
    print("\n--- Kitchen クラスを直接利用 ---")
    
    # Food クラスと Cook クラスも同様に利用できる
    new_material = cooking_module.Food("鶏肉").get_name("新鮮な")
    new_method = cooking_module.Cook("煮込む").get_use("じっくり")
    
    new_dish = cooking_module.Kitchen(
        name=new_material,
        use=new_method
    )
    new_dish.display()
    
    print("\n>>> main_program.py の処理完了 <<<")


if __name__ == "__main__":
    utilize_classes()