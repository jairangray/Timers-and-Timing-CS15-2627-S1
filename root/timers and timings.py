import time
import random
fastest_time = 100
print("Welcome to the Reaction Time Game!")
for attempt in range(5):
    print()
    print("Attempt", attempt + 1)
    print("Wait for GO!")

    wait_time = random.randint(2, 5)
    time.sleep(wait_time)

    print("GO!")

    start_time = time.monotonic()
    input("Press Enter as fast as you can!")

    end_time = time.monotonic()
    reaction_time = end_time - start_time

    print("Your reaction time was", round(reaction_time, 3), "seconds")

    if reaction_time < fastest_time:
        fastest_time = reaction_time

print()
print("Game over!")
print("Your fastest reaction time was", round(fastest_time, 3), "seconds")