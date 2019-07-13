from db import get_user
from users import User


if __name__ == "__main__":

    while True:
        name = input("ユーザー名を入力してください。: ")
        
        user_ = get_user(name)
        if user_:
            user = User(user_["id"], user_["name"], user_["age"])
            break
    
    print(user.name + "でログインしました。")

    tweet = input("ツイートしてください。: ")
    
    print("===ツイート内容===")
    print(user.name + "さん:" + tweet)
            
