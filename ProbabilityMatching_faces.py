#Katie Marlowe
#last updated: March 10, 2015

from graphics import *
from os import rename
import random

#GUI dimensions
#height = 1025
#width = 1900
height =830
width = 1430

current_money_exp = 0   #initialize money counters
current_money_con = 0
num_iterations = [200, 50]   #amount of times to ask for each probability

#experiment designs
#payout format: (guess, result)
###Design 1###
AJ_probabilities1 = [.7, .7]
payouts1a = [{('b', 'b'): 2, ('b', 'a'): 0, ('a', 'b'): 0, ('a', 'a'): 2}, {('b', 'b'): 0, ('b', 'a'): 0, ('a', 'b'): 2, ('a', 'a'): 2}]
payouts1b = [{('b', 'b'): 2, ('b', 'a'): 0, ('a', 'b'): 0, ('a', 'a'): 2}, {('b', 'b'): 2, ('b', 'a'): 2, ('a', 'b'): 0, ('a', 'a'): 0}]
###Design 2###
AJ_probabilities2 = [.7, .7]
payouts2a = [{('b', 'b'): 2, ('b', 'a'): 1, ('a', 'b'): 1, ('a', 'a'): 2}, {('b', 'b'): 0, ('b', 'a'): 0, ('a', 'b'): 2, ('a', 'a'): 2}]
payouts2b = [{('b', 'b'): 2, ('b', 'a'): 1, ('a', 'b'): 1, ('a', 'a'): 2}, {('b', 'b'): 2, ('b', 'a'): 2, ('a', 'b'): 0, ('a', 'a'): 0}]
###Design 3###
AJ_probabilities3 = [.3, .7]
payouts3a = [{('b', 'b'): 2, ('b', 'a'): 1, ('a', 'b'): 1, ('a', 'a'): 2}, {('b', 'b'): 0, ('b', 'a'): 0, ('a', 'b'): 2, ('a', 'a'): 2}]
payouts3b = [{('b', 'b'): 2, ('b', 'a'): 1, ('a', 'b'): 1, ('a', 'a'): 2}, {('b', 'b'): 2, ('b', 'a'): 2, ('a', 'b'): 0, ('a', 'a'): 0}]
###Design 4###
AJ_probabilities4 = [.3, .7]
payouts4a = [{('b', 'b'): 2, ('b', 'a'): 0, ('a', 'b'): 0, ('a', 'a'): 2}, {('b', 'b'): 0, ('b', 'a'): 0, ('a', 'b'): 2, ('a', 'a'): 2}]
payouts4b = [{('b', 'b'): 2, ('b', 'a'): 0, ('a', 'b'): 0, ('a', 'a'): 2}, {('b', 'b'): 2, ('b', 'a'): 2, ('a', 'b'): 0, ('a', 'a'): 0}]

answers = {'experiment': [], 'control': []}
results = {'experiment': [], 'control': []}

#design randomization
possible_payouts = [payouts1a, payouts1b, payouts2a, payouts2b, payouts3a, payouts3b, payouts4a, payouts4b]
payout_num = random.choice([0, 1, 2, 3, 4, 5, 6, 7])  #randomly choose design 1-4
payouts = possible_payouts[payout_num]
control_after = random.choice([True, False])   #determine if control is done before or after experiment
if not control_after:
    payouts.reverse()
    num_iterations.reverse()
AJ_prob_possibilities = [AJ_probabilities1, AJ_probabilities2, AJ_probabilities3, AJ_probabilities4]
AJ_probabilities = AJ_prob_possibilities[payout_num / 2]

global k
global response
response = False
#understand user's response ("a" or "b")
def keypress(event):
    global k
    k = event.char
    if response:
        enteredt.setText('You entered ' +k + '\n Please click to continue.')
        enteredt.setTextColor('gray35')
        enteredt.setSize(24)
        enteredt.draw(window)

#display how payouts will be give
def show_payoffs(typ):
    if typ == 'experiment':
        if payout_num in [0, 1, 6, 7]:
            lose = 0
        else:
            lose = 1
        payout_text = Text(Point(width/2, 350), 'In this portion of the experiment, your pay will be determined by if you guess the image correctly. \n \n\
            If you guess the image correctly, you will recieve v$2.    \n If you guess incorrectly, you will recieve v$' + str(lose) + '.')
        payout_text.setSize(28)
        payout_text.draw(window)
        continue_text = Text(Point(width/2, 600), 'Click to continue.')
        continue_text.setSize(24)
        continue_text.setTextColor('PeachPuff4')
        continue_text.draw(window)
        window.getMouse()
        payout_text.undraw()
        continue_text.undraw()
    else:
        payout_txt = Text(Point(width/2, 200), 'In this portion of the experiment your pay will be determined according to the following matrix:')
        payout_txt.setSize(28)
        payout_txt.draw(window)
        if payout_num in [0, 2, 4, 6]:
            payout_img = Image(Point((width/2), 400), 'angelina_control.gif')
            img_name = 'Angelina Jolie'
            other_img = 'Brad Pitt'
        else:
            payout_img = Image(Point((width/2), 400), 'brad_control.gif')
            img_name = 'Brad Pitt'
            other_img = 'Angelina Jolie'
        payout_img.draw(window)
        clarify_text = Text(Point(width/2, 575), 'In other words, if you guess ' + img_name + ', you will always get v$2 \n\
            and if you guess ' + other_img + ', you will always get v$0.            ')
        clarify_text.setSize(28)
        clarify_text.draw(window)
        continue_txt = Text(Point(width/2, 700), 'Click to continue.')
        continue_txt.setSize(24)
        continue_txt.setTextColor('PeachPuff4')
        continue_txt.draw(window)
        window.getMouse()
        payout_txt.undraw()
        payout_img.undraw()
        continue_txt.undraw()
        clarify_text.undraw()

#initialize window
window = GraphWin("Angelina Jolie or Brad Pitt?", width, height)
window.setBackground('sky blue')

#welcome page
sona_label = Text(Point((width/2)-190, 100), 'SONA ID:')
sona_label.setSize(16)
sona_label.draw(window)
sona_box = Entry(Point(width/2, 100), 50)
sona_box.draw(window)
displayed_text = Text(Point(width/2, 250), 'Welcome to the study! \n \n During this simulation an image of Angelina Jolie or Brad Pitt will appear multiple times. \n\
    For each iteration you will enter your guess of which person will appear by typing "a" for Angelina Jolie or "b" for Brad Pitt. \n\
    At the bottom of your screen you will see how much money you have earned in virtual dollars (v$). \n\
    Please enter your SONA ID in the box above.')
displayed_text.setSize(24)
displayed_text.draw(window)
continue_text = Text(Point(width/2, 375), 'Click to continue.')
continue_text.setSize(24)
continue_text.setTextColor('PeachPuff4')
continue_text.draw(window)
BPintro = Image(Point((width/2)+200, 550), 'brad_pitt_small.gif')
AJintro = Image(Point((width/2)-200, 550), 'angelina_jolie_small.gif')
bradpitt = Text(Point((width/2)+200, 700), 'Brad Pitt')
bradpitt.setSize(16)
angelinajolie = Text(Point((width/2)-200, 700), 'Angelina Jolie')
angelinajolie.setSize(16)
bradpitt.draw(window)
angelinajolie.draw(window)
BPintro.draw(window)
AJintro.draw(window)
window.getMouse()
sonaID = sona_box.getText()
while len(sonaID) != 5:   #make sure doesn't move on until SONA ID entered
    warning_text = Text(Point((width/2), 50), 'Please enter your SONA ID')
    warning_text.setSize(20)
    warning_text.setTextColor('red')
    warning_text.draw(window)
    window.getMouse()
    sonaID = sona_box.getText()
    warning_text.undraw()
    time.sleep(.2)
displayed_text.undraw()
continue_text.undraw()
sona_box.undraw()
BPintro.undraw()
AJintro.undraw()
bradpitt.undraw()
angelinajolie.undraw()
sona_label.undraw()

#images
BP = Image(Point(width/2, 500), 'brad_pitt_big.gif')
AJ = Image(Point(width/2, 500), 'angelina_jolie_big.gif')

#experiment
j = 0
for p_X in AJ_probabilities:
    if j == 0:
        if control_after:
            typ = 'experiment'
        else:
            typ = 'control'
    else:
        if control_after:
            typ = 'control'
        else:
            typ = 'experiment'
    show_payoffs(typ)
    money_text = Text(Point(100, 850), 'v$0')
    money_text.setSize(44)
    money_text.setStyle('bold')
    money_text.setTextColor('navy')
    money_text.draw(window)
    for i in xrange(num_iterations[j]):
        q_text = Text(Point(width/2, 50), 'Do you think Angelina Jolie or Brad Pitt will appear?')
        q_text.setSize(32)
        q_text.setFace('helvetica')
        q_text.draw(window)
        BPintro.draw(window)
        AJintro.draw(window)
        bottom_textA = Text(Point((width/2)-200, 400), 'Type "a" for Angelina Jolie')
        bottom_textA.setSize(20)
        bottom_textA.draw(window)
        bottom_textB = Text(Point((width/2)+200, 400), 'Type "b" for Brad Pitt')
        bottom_textB.setSize(20)
        bottom_textB.draw(window)
        enteredt = Text(Point(width/2, 250), '')
        k = ''
        response = True
        window.bind_all('<Key>', keypress)
        window.getMouse()
        while k == '':
            empty_text = Text(Point((width/2), 150), 'Please enter either "a" or "b"')
            empty_text.setSize(14)
            empty_text.setTextColor('red')
            empty_text.draw(window)
            window.bind_all('<Key>', keypress)
            window.getMouse()
            empty_text.undraw()
        while k != 'a' and k != 'b':
            enteredt.undraw()
            error_text = Text(Point(width/2, 150), 'Invalid. \n Please enter "a" or "b".')
            error_text.setSize(14)
            error_text.setTextColor('red')
            error_text.draw(window)
            window.bind_all('<Key>', keypress)
            window.getMouse()
            error_text.undraw()
        response = False
        enteredt.undraw()
        BPintro.undraw()
        AJintro.undraw()
        bottom_textA.undraw()
        bottom_textB.undraw()
        answers[typ].append(k)
        val = random.random()
        if val < p_X:
            result_pic = AJ
            result = 'a'
            results[typ].append('a')
        else:
            result_pic = BP
            result = 'b'
            results[typ].append('b')
        result_pic.draw(window)
        pay = payouts[j][(k, result)]
        if answers[typ][-1] == results[typ][-1]:
            if typ == 'experiment':
                r_text = 'Correct! \n +v$' + str(pay) + ' '
            else:
                r_text = '+v$' + str(pay)
        else:
            if typ == 'experiment':
                r_text = 'Incorrect! \n +v$' + str(pay) + ' '
            else:
                r_text = '+v$' + str(pay)
        result_text2 = Text(Point(width/2, 150), r_text)
        if typ == 'experiment':
            if answers[typ][-1] == results[typ][-1]:
                result_text2.setTextColor('forest green')
            else:
                result_text2.setTextColor('red2')
        else:
            if pay == 2:
                result_text2.setTextColor('forest green')
            else:
                result_text2.setTextColor('red2')
        result_text2.setSize(60)
        result_text2.draw(window)
        bottom_text2 = Text(Point(width/2, 800), 'Click to continue.')
        bottom_text2.setTextColor('PeachPuff4')
        bottom_text2.setSize(24)
        bottom_text2.draw(window)
        money_text.undraw()
        if typ == 'experiment':
            current_money_exp += pay
            money_text = Text(Point(100, 850), 'v$' + str(current_money_exp))
        else:
            current_money_con += pay
            money_text = Text(Point(100, 850), 'v$' + str(current_money_con))
        money_text.setSize(44)
        money_text.setStyle('bold')
        money_text.setTextColor('navy')
        money_text.draw(window)
        window.getMouse()
        q_text.undraw()
        result_pic.undraw()
        result_text2.undraw()
        bottom_text2.undraw()
    if typ == 'experiment':
        d = current_money_exp
    else:
        d = current_money_con
    money_text.undraw()
    earned_text = Text(Point((width/2), 350), 'You have earned v$' + str(d) + '\n in this portion of the experiment.')
    earned_text.setSize(36)
    earned_text.draw(window)
    continue_txt = Text(Point(width/2, 600), 'Click to continue.')
    continue_txt.setSize(24)
    continue_txt.setTextColor('PeachPuff4')
    continue_txt.draw(window)
    window.getMouse()
    earned_text.undraw()
    continue_txt.undraw()
    j += 1

#End page
close_text = Text(Point(width/2, 250), 'Thank you for participating!')
close_text.setSize(32)
close_text.draw(window)
if control_after:
    money1 = current_money_exp
    money2 = current_money_con
else:
    money1 = current_money_con
    money2 = current_money_exp
earned_text = Text(Point(width/2, 500), 'You earned v$' + str(money1) + ' in the first part of the experiment.\n\
    You earned v$' + str(money2) + ' in the second part of the experiment. \n \n In total, you earned v$' + str(money1+money2) + '. \n \n\
    Please raise your hand to indicate you are finished.')
earned_text.setSize(24)
earned_text.draw(window)

#Output results
f = open('data.txt', 'w')
f.write('SONA ID: ' + str(sonaID) + '\n \n')
f.write('DESIGN: Payout 1 = design 1 & design 5, Payout 2 = design 1 & design 6, Payout 3 = design 2 & design 5,\
Payout 4 = design 2 & design 6, Payout 5 = design 3 & design 5, Payout 6 = design 3 & design 6, \
Payout 7 = design 4 & design 5, Payout 8 = design 4 & design 6 \n \n')
f.write('Payout that was used: Payout ' + str(payout_num + 1) + '\n \n')
if control_after:
    f.write('Control was completed AFTER experiment. \n \n')
else:
    f.write('Control was completed BEFORE experiment. \n \n')
f.write('User guesses for experiment: ' + str(answers['experiment']) + '\n')
f.write('Program results for experiment: '+ str(results['experiment']) + '\n \n')
f.write('User guesses for control: ' + str(answers['control']) + '\n')
f.write('Program results for control: ' + str(results['control']) + '\n \n')
f.write('User earned: v$' + str(current_money_exp) + ' during the experiment \n')
f.write('User earned: v$' + str(current_money_con) + ' during the control.')

os.rename('data.txt', 'data' + sonaID + '.txt')
f.close()

print 'SONA ID: ', sonaID
print 'Payout: ', str(payout_num + 1)
print 'answers =', answers
print 'results = ', results
print 'Money earned during experiment: v$', current_money_exp
print 'Money earned during control: v$', current_money_con

window.mainloop()
window.close()
