class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.reward_points = 0

    def enroll(self):
        if self.is_rewards_member is False:
            self.is_rewards_member = True
            self.reward_points = 200
            print(f"Cogratulations {self.first_name}! You are now a member.")
        else:
            print(f"{self.first_name} is already a member")
        return self

    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.reward_points}')
        return self
    
    def spend_points(self, amount):
        if amount <= self.reward_points:
            self.reward_points = self.reward_points - amount
            print(f"{self.first_name}, you used some of your points!")
            return self
        else:
            print(f"{self.first_name}, you have {self.reward_points} points")

user_1 = User("Brendan", "Cordova", "cordovalegacy19@gmail.com", 27)
user_2 = User("Tori", "Cordova", "thetorimccullar@gmail.com", 26)
user_3 = User("Charles", "Chonk", "thenubbybubby69@gmail.com", 10)

user_1.is_rewards_member = "True"
user_1.display_info().enroll().spend_points(50)
user_2.display_info().enroll().spend_points(80)
user_3.display_info().spend_points(40)

# user_1.display_info()
# user_2.display_info()
# user_3.display_info()

# user_1.spend_points(50)
# user_2.spend_points(80)
# user_3.spend_points(240)

print(user_1.is_rewards_member)
print(user_2.is_rewards_member)
print(user_3.is_rewards_member)
print(user_1.reward_points)
print(user_2.reward_points)
print(user_3.reward_points)