import random

while True:
    reward_list = ("Nothing", "Animated Sand", "Ebony Blade",
                   "Alley Cat Fangs", "Dwarven Bane", "Yeeterson", "500 Gold",
                   "250 Denlayins", "5 Gold", "3 Denlayins", "A fine leather backpack",
                   "A quiver that dispenses beer", "2d20 homing arrows", "A box of fireworks",
                   "A large brown sack of gems. Wait.. these look like regular rocks that were painted.",
                   "An unhatched dragon egg", "1d4 Potions of Healing", "Centurion Spear", "Caretaker's Spade",
                   "Clacker Balls of Ki Channeling", "Dead King's Blade", "Dead King's Blade", "Deku Stick",
                   "Devilsknife", "Fallen Star", "Far Shores", "Flame Arrows (20)", "Flamesnare Whip", "Flaying Dagger",
                   "Frost Arrows (20)", "30 Gold", "1d6 burning damage", "Stormsnare Whip", "Strike Bow",
                   "Super Bug-Catching Net",
                   "Thieving Blade", "Throwing Weapon", "Flintlock", "Hondo's Wonder-Rifle", "Marksman's rifle"

                   )

    print("\nPlayer reward: ", random.choice(reward_list))
    user_input = input("\nWould you like to stop?\nEnter 'end': ")

    if user_input.lower() == "end":
        break
    else:
        continue
