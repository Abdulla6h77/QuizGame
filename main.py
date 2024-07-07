import emoji

print('Hello, welcome to the quiz game')
print('There are 3 levels to this game:')
print('Level 1 - Beginners')
print('Level 2 - Intermediate')
print('Level 3 - Advanced')

choose_level = input('Enter the level you want to play: ')

def evaluate_level(questions, answers):
    marks = 0
    for i in range(len(questions)):
        if questions[i].strip().lower() == answers[i].strip().lower():
            marks += 1
    percentage = (marks / len(questions)) * 100

    if marks == 5:
        print(emoji.emojize(":nerd_face:"), f"You're a nerd! {percentage}%")
    elif marks == 4:
        print(emoji.emojize(":smiley:"), f"You're good at studying. {percentage}%")
    elif marks == 3:
        print(emoji.emojize(":face_with_rolling_eyes:"), f"You're average. {percentage}%")
    elif marks == 2:
        print(emoji.emojize(":sob:"), f"You're not so smart. {percentage}%")
    elif marks == 1:
        print(emoji.emojize(":cry:"), f"Even how? {percentage}%")
    else:
        print(f"Oops, you didn't answer any questions correctly. {percentage}%")

    print("Thanks for playing the game! :)")

if choose_level.lower() == 'level 1' or choose_level == '1':
    questions = [
        input('WHAT DOES CPU STAND FOR? '),
        input('WHAT DOES GPU STAND FOR? '),
        input('WHAT DOES RAM STAND FOR? '),
        input('WHAT DOES ROM STAND FOR? '),
        input('WHAT ARE OUTPUT DEVICES? ')
    ]
    answers = [
        "central processing unit",
        "graphics processing unit",
        "random access memory",
        "read-only memory",
        "monitor, speaker, printer" or "printer" or "speaker" or "monitor"
    ]
    evaluate_level(questions, answers)

elif choose_level.lower() == 'level 2' or choose_level == '2':
    questions = [
        input('WHAT IS A MOTHERBOARD? '),
        input('WHAT DOES PSU STAND FOR? '),
        input('WHAT IS A HARD DRIVE? '),
        input('WHAT DOES SSD STAND FOR? '),
        input('WHAT IS AN INPUT DEVICE? ')
    ]
    answers = [
        "the main circuit board of a computer",
        "power supply unit",
        "a device for storing data",
        "solid state drive",
        "keyboard, mouse"
    ]
    evaluate_level(questions, answers)

elif choose_level.lower() == 'level 3' or choose_level == '3':
    questions = [
        input('WHAT DOES HTTP STAND FOR? '),
        input('WHAT IS THE PURPOSE OF DNS? '),
        input('WHAT DOES IP STAND FOR? '),
        input('WHAT IS A FIREWALL? '),
        input('WHAT DOES LAN STAND FOR? ')
    ]
    answers = [
        "hypertext transfer protocol",
        "translate domain names to IP addresses",
        "internet protocol",
        "a network security system",
        "local area network"
    ]
    evaluate_level(questions, answers)

quit()

#cd path/to/your/project
