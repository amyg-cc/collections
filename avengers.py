# Make a dictionary called avengers. It should contain keys for Iron Man and Hulk.
# Each attack should have an int value of the attack's power. Iron man can punch (10) and kick (100) and Hulk can smash (1000) and roll (500).
# Each avenger is represented by another dictionary, and has a name (Tony Stark and Bruce Banner respectively) and another dictionary containing their attacks.
# Once you have created the dictionary, retrieve and print out the attack power of Hulks smash move.

avengers = {
    "iron_man": {
        "personal_details": {
            "name": "Tony Stark",
            "age": 49
        },
        "attacks": {
            "punch": 10,
            "kick": 1000
        }
    },

    "hulk": {
        "personal_details": {
            "name": "Bruce Banner",
            "age": 40
        },
        "attacks": {
            "smash": 1000,
            "roll": 500
        }
    }
}
print("Hulk Smash is worth " + str(avengers["hulk"]["attacks"]["smash"]) + " points.")
print("Iron Man is " + str(avengers["iron_man"]["personal_details"]["age"]) + " years old.")

