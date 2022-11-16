#Somanath Dandibhotla
import os
import sys
import yaml
import json
import time
from datetime import date, datetime
import calendar
import random
from numpy.random import choice

def load_config(config):
    with open(config + '.yaml', 'r') as f:
        conf = yaml.safe_load(f)
    return conf

def load_exercise_history():
    try:
        with open('data.json', 'r') as fp:
            data = json.load(fp)
        return data
    except IOError:
        return dict()

def add_exercise_dictionary(dic, exercise, weight, reps):
    # {"bench press": {today: [{weight: 150, reps: 6}, {weight: 150, reps: 6}, {weight: 150, reps: 6}]}}
    today = str(date.today())
    if dic.get(exercise):
        if dic[exercise].get(today):
            dic[exercise][today] = dic[exercise][today] + [{ 'weight': weight, 'reps': reps}]
        else:
            dic[exercise][today] = [{ 'weight': weight, 'reps': reps}]
    else:
        dic[exercise] = { today: [{ 'weight': weight, 'reps': reps}]}
    return dic

def save_exercise_history(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def extract_int(s):
    return [int(x) for x in s.split() if x.isdigit()][0]

def convert_weight_string(s):
    """translates input to weight.
    "bar + 65" => 175 (lbs)
    not robust"""
    if "bar" in s:
        plate_weight = extract_int(s.split("bar")[1].split("+")[1]) # prettify
        return 45 + plate_weight * 2
    else:
        return extract_int(s)

def round_nearest_five(num):
    return int(num//5*5+ (5 if (num%5) >= 2.5 else 0))

def interact_with_user(exercise, num_sets, warmup=False): #dont need the warmup parameter it seems
    """Displays the current exercise and tracks number of reps performed"""
    exercise = random.choice([x.title().strip() for x in exercise.lstrip('*').lstrip('^').lstrip('=').split('OR')])
    exercise_history = load_exercise_history()

    prev_numbers = []
    if exercise_history.get(exercise):
        last_time = list(exercise_history[exercise].keys())[-1]
        #last_time_dow = calendar.day_name[datetime.strptime('2014-12-04', '%Y-%m-%d').date().weekday()]
        prev_numbers = exercise_history[exercise][last_time]

    #print(f"===== {exercise} =====")
    
    # if warmup:
    if prev_numbers:
        if exercise_history.get(exercise):
            while True:
                try:
                    checker = 0
                    checker2 = 0
                    trueOrNot1 = 0
                    trueOrNot2 = 0
                    for i in reversed(prev_numbers):
                        checker += 1
                    if checker >= 3: # if there are 3 or more entries made
                        prev_num_str = [x['reps'] + ' lbs for ' + x['weight'] for x in prev_numbers]
                        for x in prev_num_str:
                            abota = x
                        for i in reversed(prev_numbers): # get third weight used back
                            threeBack = int(i["weight"])
                            checker2 += 1
                            if checker2 == 3:
                                break
                        for i in reversed(prev_numbers): #check first one back
                            if int(i["weight"]) + 2 > threeBack:
                                trueOrNot1 = 1
                            checker2 = 0
                            checker2 += 1
                            if checker2 == 1:
                                break
                        for i in reversed(prev_numbers): #check second one back
                            if int(i["weight"]) + 2 > threeBack:
                                trueOrNot2 = 1
                            checker2 = 0
                            checker2 += 1
                            if checker2 == 2:
                                break
                        if trueOrNot1 == 1 and trueOrNot2 == 1:
                            inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nSuggestion: Looking at your workout history, per the 2/2 rule, you qualify for increasing your weights by 5-10 pounds. *User discretion is advised.*\nHow much weight(lbs) would you like to lift?: ")
                        else:
                            inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nHow much weight(lbs) would you like to lift ?: ")
                        # inp2 = input("How many reps would you like to do?: ")
                        weight = convert_weight_string(inp)
                        break
                    else: #if there are less than 2 entries made
                        prev_num_str = [x['weight'] + 'lbs for ' + x['reps'] for x in prev_numbers]
                        for x in prev_num_str:
                            abota = x
                        inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nHow much weight(lbs) would you like to lift ?: ")
                        # inp2 = input("How many reps would you like to do?: ")
                        weight = convert_weight_string(inp)
                        break
                except:
                    print("Invalid input. Please try again.")
                    break
                break
        else:
            inp = input(f"You have never logged this exercise, '{exercise}'. How much weight would you like to lift (lbs)?: ")
            weight = convert_weight_string(inp)
        # else:
        #     inp = input(f"You have never logged this exercise, '{exercise}'. How much weight would you like to lift (lbs)?: ")
        #     weight = convert_weight_string(inp)
    inp2 = input("How many reps would you like to do?: ")
    # else:
    #     weight = convert_weight_string(prev_numbers[0]["weight"])
    #print("       ( warm up ) ")
    print("")
    print("---- Workout Plan ----")
    
    def warmup_routine(reps, percent, setNumber):
        print(f"(Set {setNumber}) - {reps} reps of {round_nearest_five(weight*percent)} lbs.")
        #countdown_for_rest(rest_min)

    if num_sets == 1:
        for (percent, reps, setNumber) in [(1, int(inp2), 1)]:
            warmup_routine(reps, percent, setNumber)
    elif num_sets == 2:
        for (percent, reps, setNumber) in [(.5, int(inp2), 1), (1, int(0.5 * int(inp2)), 2)]:
            warmup_routine(reps, percent, setNumber)
    elif num_sets == 3:
        for (percent, reps, setNumber) in [(.4, int(0.5 * int(inp2)), 1), (.7, int(0.7 * int(inp2)), 2), (1, int(inp2), 3)]:
            warmup_routine(reps, percent, setNumber)
    elif num_sets == 4:
        for (percent, reps, setNumber) in [(.4, int(0.2 * int(inp2)), 1), (.6, int(0.5 * int(inp2)), 2), (.8, int(0.7 * int(inp2)), 3), (1, int(inp2), 4)]:
            warmup_routine(reps, percent, setNumber)
    elif num_sets == 5:
        for (percent, reps, setNumber) in [(.3, int(0.2 * int(inp2)), 1), (.5, int(0.4 * int(inp2)), 2), (.7,  int(0.6 * int(inp2)), 3), (1, int(0.8 * int(inp2)), 4), (.9, int(inp2), 5)]:
            warmup_routine(reps, percent, setNumber)
    else:
        print("Too many sets. Potentially harmful. Please try again.")
        exit()
            
    # if exercise_history.get(exercise): #EXERCISE HISTORY
    #     prev_num_str = [x['weight'] + 'x' + x['reps'] for x in prev_numbers]
    #     print(f" ----- {exercise} -----\r\n{last_time}: {', '.join(prev_num_str)}")
    print("---- Log Your Sets ----")
    for s in range(num_sets): # TODO: handle warmups
        while True:
            try:
                inp = input("(Set " + str(s+1) + ") - Enter info (weight, reps): ")
                weight = inp.split(',', 1)[0]
                reps = inp.split(',',1)[1].strip().replace('.','',1)
                if reps.strip().replace('.','',1).isdigit():
                    break
                else:
                    print("Invalid input. Please try again.")
            except:
                print("Invalid input. Please try again.")

        exercise_history = add_exercise_dictionary(exercise_history, exercise, weight, reps)
        save_exercise_history(exercise_history)
        #countdown_for_rest(2)
    None

# def countdown_for_rest(min):
#     def display_time(s):
#         display_min = lambda m: str(m) + " min" if m > 0 else ""
#         display_sec = lambda s: str(s) + " sec" if s > 0 else ""
#         sys.stdout.write(f"Rest for {display_min(s//60)} {display_sec(s%60)}         ")
#     for remaining in range(int(min*60), 0, -1):
#         sys.stdout.write("\r")
#         display_time(remaining)
#         sys.stdout.flush()
#         time.sleep(1)
#     sys.stdout.write("\r")

def shuffle(exercises, count):
    """Apply modifiers and then randomly shuffles list"""
    def build_weights(exercises):
        weights = list(map(lambda x: 0.0 if x.startswith('*') else (1.0 if x.startswith('^') else 0.5), exercises))
        sum_weights = sum(weights)
        weights = list(map(lambda x: x/sum_weights, weights))
        return weights

    top_priority = [x for x in exercises if x.startswith('**')]
    weights = build_weights(exercises)
    # random.choices can result in duplicates
    the_rest = []
    for _ in range(count - len(top_priority)):
        chosen = random.choices(exercises, weights=weights, k=1)[0]
        while chosen in the_rest:
            chosen = random.choices(exercises, weights=weights, k=1)[0]
        the_rest.append(chosen)

    # ensuring = is last exercise performed
    return top_priority + [x for x in the_rest if not x.startswith('=')] + [x for x in the_rest if x.startswith('=')]

def main():
    exercises = load_config("exercises")
    routine = load_config("routine")

    current_day = calendar.day_name[date.today().weekday()]
    todays_routine = routine.get(current_day, None)

    # addExercise = input("Would you like to add a new exercise? (Y/N): ")
    #     if addExercise == "Y" or addExercise == "y":
    #         whatMuscleGroup = input("What Muscle Group does it work: ")
    #         nameOfExcercise = input("What is the exercise name?: ")

    #         with open('exercises.yml', 'w') as yaml_file:
    #             yaml.dump(d, yaml_file, default_flow_style=False)

    if todays_routine:
        for muscle_group in todays_routine:
            exercise_set_count = todays_routine[muscle_group]
            muscle_group_exercises = shuffle(exercises[muscle_group], exercise_set_count)
            for i in range(exercise_set_count):
                check = input(f"Would you like to do '{muscle_group_exercises[i].title()}'? (Y/N): ")
                if check == "N" or check == " N" or check == "n" or check == " n":
                    continue
                print(f"===== {muscle_group_exercises[i].title()} =====")
                try:
                    inp = input(f"How many sets of '{muscle_group_exercises[i].title()}' would you like to do? (max:5): ")
                except:
                    print("Invalid input. Please try again.")
                interact_with_user(muscle_group_exercises[i], int(inp), i==0) 

    else:
        print("It is your Rest Day. See you tomorrow :)")

if __name__ == '__main__':
    main()