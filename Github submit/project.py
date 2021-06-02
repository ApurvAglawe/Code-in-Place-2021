"""
A study bot which helps to measure the problem solving speed and accuracy of the learner
by posting random problems from mathematics, aptitude etc. and plot a graph specifing the 
time taken and accuracy of the learner and showing points where the user needs to improve.
1] Welcome screen and username
2] start the test
3] give feedback: 1) no of questions solved, 2) no of correct answers, 3) accuracy, 4) Total Time taken for the test, 5) average time taken to solve one question, 6)
4] show the graph of 1) que no vs time taken (local data), 2)total time taken vs accuracy (all time)
"""
'''
start with easy mode to make user adapt with the concepts (10 questions).
Go to intermediate mode to practice speed of the user (20 questions).
can go to advanced mode to master questions and improve timing. 
'''
'''
Easy mode:
percentages, 
percentages
40 % of 280 = ?
A] 112   B] 116
C] 115   D] 120
HCF and LCM:
Find the HCF of 210, 385, and 735.
Find the least number which when divided by 12, 27 and 35 leaves 6 as a remainder.
series and progression:
Q]1,2,2,3,3,3,4,4,4,4,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,…………………………………..

Then what is the 2320 position of the number in the sequence?
Q]There are 60 pebbles and 2 persons a and b. A takes 1 pebble, b takes 2 pebbles and
again a takes 3 pebbles and b takes 4 pebbles and
this goes on alternatively. Who takes the maximum number of pebbles?
'''
import random
import time
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd

PERCENTAGE_QUE = 5
option_list = ['A','B','C','D']
ans_list = []
time_list = []
 
def percentage_easy(que_num,score):
    """
    1] print the question number
    2] print the question and the four options
    3] ask the user for the answer and wait till the user answers
    4] repeat the process for the next question
    """
    for i in range (PERCENTAGE_QUE):
        que_num += 1
        print("\nQuestion",que_num)
        percent = random.randrange(10,100,10)
        percent_of = random.randrange(200,1000,10)
        print(str(percent),'% of',str(percent_of),'= ?')
        answer = int(percent * 0.01 * percent_of)
        options = [answer]
        while len(options) < 4 :
            x = random.randrange(answer-18,answer+18)
            if (x % (percent*0.1) == 0 or x % (percent_of*0.1) == 0):
                if x not in options:
                    options.append(x)
        #generate options dictionary
        options_dict = generate_options(options)
        # get the correct option number
        correct_option = get_correct_option(options_dict,answer)
        #pass the score, options dictionary and the answer, and get the input from the user
        time_list,score = get_input(correct_option,score)
        # create a list of correct options
        ans_list.append(correct_option)
    return que_num,time_list,score
'''
def percentage_intermediate(que_num):
    for i in range (PERCENTAGE_QUE):
        print("\nQuestion",que_num)
        percent = random.randrange(10,100,10)
        percent_of = random.randrange(200,1000,10)
        print(str(percent),'% of',str(percent_of),'= ?')
        answer = int(percent * 0.01 * percent_of)
        options = [answer]
        while len(options) < 4 :
            x = random.randrange(answer-50,answer+50,10)
            #if (x % (percent*0.1) == 0 or x % (percent_of*0.1) == 0):
            if x not in options:
                options.append(x)
        generate_options(options)
        get_input(options_dict)
        print("answer = ",answer)
        que_num += 1
    return que_num
'''
def run_timer(t):
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t += 1
    pass
def generate_options(options):
    """
    input: The options to the questions in a list form.
    output: A dictionary with the option number as key and the options as its value
    """
    # list of option numbers 
     
    # shuffle the option number
    random.shuffle(options)
    #create a options dictionary
    options_dict = {}
    for key in option_list:
        for value in options:
            options_dict[key] = value
            options.remove(value)
            break
    # print the options
    for key in options_dict:
        print(key+']',options_dict[key])
    return options_dict

#function to get the correct answer
# pass in the options_dict, the answer, and the user answer
def get_correct_option(options_dict,answer):
    """
    input: The options dictionary and the correct answer.
    output: checks which option has the correct value and returns that option 
    """
    for key in options_dict:
        if options_dict[key] == answer:
            correct_option = key   
    #return correct_ans
    ans_list.append(correct_option)
    #print("answer was",correct_option,'and your score = ', score)
    return correct_option

# function to get the input and return the score
def get_input(correct_option,score):
    """
    input: Gets the correct option as input from the user.
    output: returns the score as well as a list of time taken for each question.
    """
    initial = float("{:.2f}".format(time.time()))
    user_ans = input(("Your Answer: ")).upper()
    # compare the correct answer with the user input and if answered correctly increase their score.   
    while user_ans not in option_list:
        user_ans = input(("Please input A, B, C or D: ")).upper()
    if user_ans == correct_option: 
        print("correct!")
        score+=1
    else:
        print('close! the correct answer was',correct_option)
    time_taken = float("{:.2f}".format(time.time()-initial))
    print("you took",str(time_taken),"seconds and your score is",str(score))
    time_list.append(time_taken)
    time.sleep(2)
    return time_list,score

#plots the graph with input as lists.
def plot_graph(que_list,time_list):
    mydataset = {'question number': que_list,'time taken': time_list}
#     print(mydataset)
    plt.figure(facecolor='yellow')  
    plt.title("Questions Vs Time Graph")
    plt.plot(que_list,time_list,linestyle='-', marker='o', color='b') 
    plt.xlabel('Question number')
    ax = plt.axes()
    ax.set_facecolor("orange")
    plt.ylabel('Time')
    plt.savefig("Test_analysis.png")
    plt.show()

def write_data(que_num,score,time_list):
    """
    this function writes data to the data.csv file each time the user is finished with the test 
    """
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    accuracy = float("{:.2f}".format(score/que_num))
    total_time = 0
    for i in time_list:
        total_time += i
    total_time = float("{:.2f}".format(total_time))
    average_time = float("{:.2f}".format(total_time/que_num))
    fields = [time_stamp,que_num,score,accuracy,total_time,average_time]
    analysis(que_num,score,total_time,accuracy,average_time)
    que_list = question_list(time_list)
    plot_graph(que_list,time_list)
    user_ans = input("Do you want to get the overall feedback?\nPress y for yes:").upper()
    if user_ans == "Y":
        print("\n              FEEDBACK             ")  
        give_feedback(accuracy,average_time) 
    with open("data.csv", 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    again = input("Press 'Y' to try again").upper()
    if again == 'Y':
        main()

def question_list(time_list):
    que_list = []
    for i in range(len(time_list)):
        que_list.append('Q'+ str(i+1))    
    return que_list

def analysis(que_num,score,total_time,accuracy,average_time):
    """
    The next step is to Get the analysis of the test.
    """
    print("\n              ANALYSIS             ")
    print("Number of questions solved:",str(que_num))    
    print("Your Score:",str(score)+"/"+str(que_num))    
    print("Your accuracy is:",str(accuracy * 100),'%')
    print("Time taken to solve:",str(total_time)+" seconds") 
    print("Average time taken per question:",str(average_time)+" seconds")
    print("Least time:",str(min(time_list))+" seconds")
    print("Most time:",str(max(time_list))+" seconds")
    
def give_feedback(accuracy,average_time):
    """
    Analysis:
    ideal condition: accuracy above 0.6 and average time above mean time.
    worst conditoin: accuracy below 0.4 and average time below mean time.
    intermediate: accuracy > 0.6 but average time < mean time.
    intermediate: accuracy < 0.6 but average time > mean time. 
    """
    df = pd.read_csv('data.csv')
    #print(df)
    mean_time = df['average time taken'].mean()
    # mean_time = df['accuracy'].mean()
    print("mean Time:",str(mean_time))
    if accuracy >= 0.6 and average_time <= mean_time:
        print("Good job! Your accuracy is excellent and your average time to solve a question is also less.")
    elif accuracy >= 0.6 and average_time > mean_time:
        print("Very Good, you are getting clear on your concepts and have a good accuracy, slowly you will improve with your timing.")
    elif accuracy < 0.6 and average_time < mean_time:
        print("No need to hurry, dont focus too much on the time. first get a grip on your concepts and then improve on your timing.")
    else:
        print("No one is perfect, Initially you dont need to worry about the timing, you need to improve on your accuracy first.")
    print("Your accuracy is:",str(accuracy * 100),'%')
    print("Your average time:",str(average_time)+" seconds")
    plt.title("Questions Vs Time Graph")
    plt.scatter(df['accuracy'],df['average time taken'])
    plt.scatter(accuracy,average_time)
    plt.axhline(y= mean_time, color='r', linestyle='--')
    plt.axvline(x= 0.6, color='b', linestyle='--')
    plt.legend(["Previous", "Recent"], loc ="lower right")
    plt.xlabel("Accuracy")
    plt.ylabel("average time in seconds")
    plt.savefig("Overall_analysis.png")
    plt.show()
    

def study_bot():
    que_num = 0
    score = 0
    que_num,time_list,score = percentage_easy(que_num,score)
    #que_num = percentage_intermediate(que_num)
    #plot_graph(que_list,time_list)
    #print(time_list)
    
    write_data(que_num,score,time_list)

def main():
    name = input("Enter your name:")
    print("Howdy",name+"! welcome to study bot.\nA bot which helps you improve your aptitude!")
    print("You will be asked",str(PERCENTAGE_QUE),"questions")
    print("Your goal is to get the correct answer and mark the corresponding option to the question.")
    ready = input("when ready press enter to start: ").upper()
    while (ready != ''):
        ready = input("when ready press enter to start: ").upper()
    study_bot()
    
if __name__ == '__main__':
    main()

# tasks:
# 1] after the user ends the test, compare the average time and accuracy with global data.
# 2] plot the total time taken vs accuracy scatter plot and add a backgroung image explaining the same
# 3] show what an ideal graph looks like(calculate slope of the graph)
# 4] add some more question types like HCF.
# 5]  
# 5] timer on top left(if possible)