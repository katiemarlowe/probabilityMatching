import csv
import matplotlib.pyplot as plt
import matplotlib
import pylab as plb

ages = []
incomes = {'less than $25,000': 0, '$25,000 - $50,000': 0, '$50,001-$75,000': 0, '$75,001-$100,000': 0, '$100,001 - $200,000': 0,'More than $200,000': 0}
occupations = {'Unemployed': 0, 'Working now': 0, 'Student': 0, 'Other': 0}
pattern = {}

#read data from csv
with open('post_study_data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ages.append(row[2])
        income = row[9]
        if income in incomes:
            incomes[income] += 1
        occupation = row[6].split(', ')
        for o in occupation:
            if o in occupations:
                occupations[o] += 1
            else:
                occupations['Other'] += 1
        pattern[row[1]] = row[20]
    ages.remove('Age:')
    ages = [int(age) for age in ages]
del pattern['SONA ID:']

#create age histogram
##plt.hist(ages, 8, color='cyan')
##plt.title('Ages of Subjects')
##plt.xlabel('Age')
##plt.ylabel('Frequency')
##plt.savefig('ageHist.pdf', bbox_inches='tight')
##plt.clf()
##
###create income pie chart
##plb.pie(incomes.values(), labels = incomes.keys(), autopct='%1.1f%%')
##plb.title('Incomes of Subjects')
##plb.savefig('incomeChart.pdf', bbox_inches='tight')
##plb.clf()
##
###create occupations pie chart
##plb.pie(occupations.values(), labels = occupations.keys(), autopct='%1.1f%%')
##plb.title('Working Status of Subjects')
##plb.savefig('occupationsChart.pdf', bbox_inches='tight')
##plb.clf()

#make all charts
##plt.subplot(221)
##plt.hist(ages, 8, color='cyan') #ages
##plt.xlabel('Age')
##plt.ylabel('Number of Participants')
##plt.subplot(212)
##plt.bar(range(len(incomes)), incomes.values(), align='center', color='cyan') #incomes
##plt.xticks(range(len(incomes)), incomes.keys())
##plt.xlabel("Income")
##plt.ylabel("Number of Participants")
##plt.subplot(222)
##plt.bar(range(len(occupations)), occupations.values(), align='center', color='cyan') #occupations
##plt.xticks(range(len(occupations)), occupations.keys())
##plt.xlabel("Occupation")
##plt.ylabel("Number of Participants")
##plt.show()



#create income bar chart
##plt.bar(range(len(incomes)), incomes.values(), align='center', color='cyan')
##plt.xticks(range(len(incomes)), incomes.keys())
##plt.title("Incomes of Subjects")
##plt.xlabel("Income")
##plt.ylabel("Number of Participants")
##plt.show()
#create occupations bar chart
##plt.bar(range(len(occupations)), occupations.values(), align='center', color='cyan')
##plt.xticks(range(len(occupations)), occupations.keys())
##plt.title("Occupations of Subjects")
##plt.xlabel("Occupation")
##plt.ylabel("Number of Participants")
##plt.show()

p_hat_dic = {'79507': 0.6611111111111111, '57447': 0.9888888888888889, '31828': 0.6666666666666667, '67378': 0.6888888888888889, '45178': 0.8666666666666667, '47674': 0.5944444444444444, '35167': 1.0, '80641': 1.0, '62917': 0.7388888888888889, '67234': 0.9, '32605': 0.7166666666666667, '67903': 0.85, '80659': 0.9277777777777778, '79822': 0.9333333333333333, '72760': 0.7611111111111111, '52633': 0.9666666666666667, '80596': 0.975, '78727': 0.825, '62446': 0.9888888888888889, '80593': 0.9277777777777778, '70912': 0.8461538461538461, '62386': 0.85, '76591': 0.8055555555555556, '60709': 0.8, '63334': 0.4833333333333333, '80584': 0.8666666666666667, '62161': 0.6787878787878787, '76756': 0.7277777777777777, '63595': 0.967741935483871, '68350': 0.9444444444444444, '79489': 0.5666666666666667, '78853': 0.9666666666666667, '33667': 0.8611111111111112, '57394': 0.9722222222222222, '36773': 0.7611111111111111, '71617': 0.96875, '78613': 0.9055555555555556, '61885': 0.8222222222222222, '78637': 0.8333333333333334, '73264': 0.8, '80188': 0.5944444444444444, '76108': 0.6944444444444444, '74476': 0.9222222222222223, '79996': 0.80625, '80614': 0.7277777777777779, '79156': 0.7555555555555555, '61372': 0.8111111111111111, '76666': 0.9586206896551724, '73396': 0.9888888888888889, '75754': 0.9055555555555556, '80608': 0.8258064516129032, '32008': 0.6125, '56296': 0.8347826086956522, '68287': 0.9666666666666667, '68464': 0.95, '68641': 0.9944444444444445, '74011': 0.8944444444444445, '63574': 0.6222222222222222, '80587': 0.8785714285714286, '79975': 0.9888888888888889, '67159': 0.8777777777777778, '66898': 0.9944444444444445, '69928': 0.98, '80695': 0.9705882352941176, '38008': 0.7611111111111111, '74599': 0.9, '78064': 0.7388888888888889, '72298': 0.9944444444444445, '62050': 0.9277777777777778, '74134': 0.5888888888888889, '31855': 0.8, '79801': 0.8, '64894': 0.75, '54742': 0.9828571428571429, '76768': 0.967741935483871, '80569': 0.65, '62593': 0.9666666666666667, '70045': 0.7517241379310344, '80320': 0.9636363636363636, '72049': 0.6166666666666667, '68368': 0.9944444444444445, '67492': 0.9}

##with open('pattern.csv', 'wb') as csvfile:
##    writer = csv.writer(csvfile)
##    writer.writerow(['SONA ID', 'p^', 'Pattern Answer'])
##    for sona in pattern.keys():
##        writer.writerow([sona, str(round(p_hat_dic[sona], 4)), pattern[sona]])

p_hat_dic1 = {'78727': 0.825, '47674': 0.5944444444444444, '35167': 1.0, '62917': 0.7388888888888889, '73396': 0.9888888888888889, '67903': 0.85, '74476': 0.9222222222222223, '52633': 0.9666666666666667, '80596': 0.975, '70912': 0.8461538461538461, '62386': 0.85, '79801': 0.8, '80584': 0.8666666666666667, '31828': 0.6666666666666667, '76756': 0.7277777777777777, '80695': 0.9705882352941176, '36773': 0.7611111111111111, '61885': 0.8222222222222222, '80188': 0.5944444444444444, '76108': 0.6944444444444444, '79996': 0.80625, '61372': 0.8111111111111111, '75754': 0.9055555555555556, '32008': 0.6125, '56296': 0.8347826086956522, '74011': 0.8944444444444445, '63574': 0.6222222222222222, '80587': 0.8785714285714286, '79975': 0.9888888888888889, '66898': 0.9944444444444445, '69928': 0.98, '38008': 0.7611111111111111, '62050': 0.9277777777777778, '74134': 0.5888888888888889, '74599': 0.9, '64894': 0.75, '62593': 0.9666666666666667, '80320': 0.9636363636363636, '72049': 0.6166666666666667, '68368': 0.9944444444444445, '80569': 0.65}
p_hat_dic2 = {'57447': 0.9888888888888889, '67378': 0.6888888888888889, '45178': 0.8666666666666667, '67234': 0.9, '32605': 0.7166666666666667, '80614': 0.7277777777777779, '80659': 0.9277777777777778, '79822': 0.9333333333333333, '72760': 0.7611111111111111, '62446': 0.9888888888888889, '80593': 0.9277777777777778, '78853': 0.9666666666666667, '68641': 0.9944444444444445, '76591': 0.8055555555555556, '60709': 0.8, '63334': 0.4833333333333333, '62161': 0.6787878787878787, '63595': 0.967741935483871, '68350': 0.9444444444444444, '79489': 0.5666666666666667, '33667': 0.8611111111111112, '68464': 0.95, '71617': 0.96875, '78613': 0.9055555555555556, '78637': 0.8333333333333334, '73264': 0.8, '79507': 0.6611111111111111, '78064': 0.7388888888888889, '68287': 0.9666666666666667, '57394': 0.9722222222222222, '80641': 1.0, '67159': 0.8777777777777778, '76666': 0.9586206896551724, '80608': 0.8258064516129032, '72298': 0.9944444444444445, '31855': 0.8, '54742': 0.9828571428571429, '76768': 0.967741935483871, '70045': 0.7517241379310344, '79156': 0.7555555555555555, '67492': 0.9}

#create p^ histogram
yes_pattern = []
no_pattern = []
for sona in pattern.keys():
    if pattern[sona] == 'Yes':
        if sona in p_hat_dic1:
            yes_pattern.append(p_hat_dic1[sona])
        else:
            yes_pattern.append(p_hat_dic2[sona])         
    elif pattern[sona] == 'No':
        if sona in p_hat_dic1:
            no_pattern.append(p_hat_dic1[sona])
        else:
            no_pattern.append(p_hat_dic2[sona])
plt.hist([yes_pattern, no_pattern], color=['cyan', 'yellow'], label=['Pattern Finders', 'Non Pattern Finders'])
plt.xlabel('Frequency to choose dominant image')
plt.ylabel('Number of Participants')
plt.title('Pattern Finders vs. Non Pattern Finders')
plt.legend(loc=2)
plt.show()
