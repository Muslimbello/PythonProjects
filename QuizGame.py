print("Welcome to my computer quiz")
playing = input("Do you want to play? yes/no\n")
answer = [
    "central processing unit",
    "read access memory",
    "graphics processing unit",
    "operating system",
    "read only memory",
]
question = ["CPU", "RAM", "GPU", "OS", "ROM"]
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)")
""" I can pass i into answer since both of them will have them same length"""
for i in range(len(question)):
    q = input(f"What is the full meaning of {question[i]}? ").lower()
    if q == answer[i]:
        print("That's correct")
    else:
        print(
            "Check your spellings and make sure each word is separated by a single space"
        )
