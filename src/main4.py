cat_data_list = [
    {
        "name": "ちゃとら",
        "personality": 5,
        "status": "1:指名マッチ",
        "waiting_days": 5,
        "medical_history": [
            {"date": "2025-10-01", "reason": "ワクチン"},
            {"date": "2025-12-25", "reason": "健康診断"}
        ]
    },
    {
        "name": "くろ",
        "personality": 3,
        "status": "2:エリアマッチ",
        "waiting_days": 60,
        "medical_history": [
            {"date": "2025-05-10", "reason": "去勢手術"},
            {"date": "2025-11-01", "reason": "定期検診"}
        ]
    },
    {
        "name": "しろ",
        "personality": 4,
        "status": "1:指名マッチ",
        "waiting_days": 15,
        "medical_history": []
    }
]

user_setting = {"target_personality": 5}

def log_print(f):
    def _wrapper(*args, **keywards):
        print(f"{f.__name__}関数の開始")  
        result = f(*args, **keywards)
        print(f"{f.__name__}関数の終了") 
        return result
    return _wrapper

class MatchBase:
    def __init__(self,cat_name,status):
        self.cat_name = cat_name
        self.status = status

    @log_print
    def display(self,score):
        prefix = "⭐︎" if "指名" in self.status else ""
        print(f"{prefix}猫:{self.cat_name},スコア:{score}")

    @classmethod
    def create_from_data(cls,cat_obj,user_pref):
        score = 0
        if cat_obj.personality == user_pref["target_personality"]:
            score += 500
        return cls(cat_obj.name,cat_obj.status),score

class Cat(MatchBase):
    def __init__(self,name,personality,status):
        self.name = name
        self.personality = personality
        self.status = status

tama = Cat("たま", 5, "1:指名マッチ")
user_setting = {"target_personality": 5}

result_instance,final_score = MatchBase.create_from_data(tama,user_setting)

result_instance.display(final_score)