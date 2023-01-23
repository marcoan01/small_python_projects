
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
      )

def highest(dc):
    biggest = 0
    for i in dc:
        if dc[i] > biggest:
            biggest = dc[i]
    print(biggest)



contestants = {}
decision = 'yes'
while decision.lower() == 'yes':
    name = input("What is your name? \n")
    bid = int(input("what is your bid? \n"))
    contestants[name] = bid
    decision = input("Is there another person who would like to bid? ")
highest(contestants)
