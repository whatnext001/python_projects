light_1 = "green"
light_2 = "red"
light_3 = "yellow"

traffic_light = {
    "Go":"green",
    "Stop":"red",
    "Wait":"yellow"
}

for i in traffic_light:
    if light_1 == traffic_light["Stop"]:
        print("fuck off")
    elif light_2 == traffic_light["Stop"]:
        print("Stay put")
    else:
        print("wait a moment")




alphabet = "the little living one in a dream"

vowel = ['a','e','i','o','u']

count_vowel = alphabet.count("a")

for vowel in alphabet:
    print(vowel.count(vowel))



list_details = ["5","gh","tyyy","y677"]

for items in list_details:

    print(f"{items*2}")