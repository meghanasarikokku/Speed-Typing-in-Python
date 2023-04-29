import time

def typing_speed_test():
    print("Welcome to the typing speed test!")
    time.sleep(1)
    print("You will be given a phrase to type. Type it as quickly and accurately as possible!")
    time.sleep(1)
    phrase = "iam meghana sarikokku"
    print("Phrase to type:", phrase)
    time.sleep(1)
    start_time = time.time()
    user_input = input("Type the phrase above and press Enter to finish: ")
    end_time = time.time()
    time_elapsed = end_time - start_time
    correct_chars = 0
    for i in range(len(user_input)):
        if user_input[i] == phrase[i]:
            correct_chars += 1
    accuracy = correct_chars / len(phrase) * 100
    speed = len(phrase) / time_elapsed / 5 * 60 # assuming 5 characters per word
    print("Time taken:", round(time_elapsed, 2), "seconds")
    print("Accuracy:", round(accuracy, 2), "%")
    print("Typing speed:", round(speed, 2), "words per minute")
typing_speed_test()