
def my_home(f):
    def _wrapper(*args, **keywards): #*args,**keywordsはなくてもOK

        print(f"wood2:{f.__name__}の実行") #(例) woodの実行
        
        v = f(*args, **keywards)
        
        print(f"wood2:{v}") #(例) 机,ベッド,椅子

    return _wrapper

def wood(*args, **keyawrds):
# def wood(key3, *args, **keyawrds):
    # print(f"key3: {key3}")
    print(f"args: {args}")
    print(keyawrds)
    s = ""
    for key in keyawrds:
        s += str(keyawrds[key])
    return f"str: {s}"
    #return f" 机,ベッド,椅子"
wood2 = my_home(wood)

@my_home
def electricity():
    return "電子レンジ,TV,冷蔵庫"
@my_home
def cloth():
    return "カーテン,布団,ソファ"

print(f"wood2:{wood2()}")
# wood2(1, 2, 3)
# wood2(key1=1, key2=2, key3=3)
electricity()
cloth()