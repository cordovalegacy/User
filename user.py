class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.reward_points = 0

    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.reward_points}')
    
    def enroll(self):
        if self.is_rewards_member is False:
            self.is_rewards_member = True
            self.reward_points = 200
        else:
            print("User already a member")
    
    def spend_points(self, amount):
        if amount <= self.reward_points:
            self.reward_points = self.reward_points - amount
        else:
            print("Insufficient funds")

user_1 = User("Brendan", "Cordova", "cordovalegacy19@gmail.com", 27)
user_2 = User("Tori", "Cordova", "thetorimccullar@gmail.com", 26)
user_3 = User("Charles", "Chonk", "thenubbybubby69@gmail.com", 10)

user_1.display_info()
user_2.display_info()
user_3.display_info()

user_1.is_rewards_member = "True"
user_1.enroll()
user_2.enroll()
user_3.enroll()

user_1.spend_points(50)
user_2.spend_points(80)
user_3.spend_points(240)

print(user_1.is_rewards_member)
print(user_2.is_rewards_member)
print(user_3.is_rewards_member)
print(user_1.reward_points)
print(user_2.reward_points)
print(user_3.reward_points)