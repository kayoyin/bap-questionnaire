##################################################################################################
# Broad Autism Phenotype Questionnaire                                                           #
#  * by Kayo Yin                                                                                 #
#                                                                                                #
# References:                                                                                    #
#                                                                                                #
# The broad autism phenotype questionnaire                                                       #
# Robert S E Hurley, Molly Losh, Morgan Parlier, J Steven Reznick, Joseph Piven                  #
# https://pubmed.ncbi.nlm.nih.gov/17146701                                                       #
#                                                                                                #
# The broad autism phenotype questionnaire: prevalence and diagnostic classification             #
# Noah J Sasson, Kristen S L Lam, Debra Childress, Morgan Parlier, Julie L Daniels, Joseph Piven #
# https://pubmed.ncbi.nlm.nih.gov/17146701                                                       #
#                                                                                                #
##################################################################################################

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BAP Questionnaire.')
    parser.add_argument('--gender', choices=['m', 'f', 'male', 'female'], help='Gender of the subject of the questionnaire')
    parser.add_argument('--answerer', choices=['self', 'informant'], help='Whether the questionnaire is answered by the subject themself or an external informant')
    args = parser.parse_args()

    with open("questions.txt", 'r') as file:
        questions = file.readlines()
    
    print("You are about to fill out a series of 36 statements related to personality and lifestyle. \
For each question, enter the number associated with the answer that best describes how often that statement applies to you. \
Many of these questions ask about \
your interactions with other people. Please think about \
the way you are with most people, rather than special \
relationships you may have with spouses or significant \
others, children, siblings, and parents. Everyone \
changes over time, which can make it hard to fill out \
questions about personality. Think about the way you \
have been the majority of your adult life, rather than \
the way you were as a teenager, or times you may have \
felt different than normal. You must answer each \
question, and give only one answer per question. If you \
are confused, please give it your best guess")
    print()
    print("1—Very rarely    2—Rarely    3—Occasionally   4—Somewhat often    5—Often     6—Very often")
    print()

    answers = []
    for q in questions:
        answers.append(int(input(q)))

    reverse_qs = [1, 3, 7, 9, 12, 15, 16, 19, 21, 23, 25, 28, 30, 34, 36]
    aloof = [1, 5, 9, 12, 16, 18, 23, 25, 27, 28, 31, 36]
    pl = [2, 4, 7, 10, 11, 14, 17, 20, 21, 29, 32, 34]
    rigid = [3, 6, 8, 13, 15, 19, 22, 24, 26, 30, 33, 35]
    reverse = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

    for i in reverse_qs:
        answers[i-1] = reverse[answers[i-1]]

    aloof_score = sum([answers[i-1] for i in aloof])
    pl_score = sum([answers[i-1] for i in pl])
    rigid_score = sum([answers[i-1] for i in rigid])
    total_score = aloof_score + pl_score + rigid_score

    t = {'m': {'self': {'aloof': 4.13, 'pl': 3.23, 'rigid': 3.91, 'total': 3.55}, 
          'informant': {'aloof': 4.19, 'pl': 3.29, 'rigid': 4.20, 'total': 3.63}},
         'f': {'self': {'aloof': 3.45, 'pl': 2.94, 'rigid': 3.70, 'total': 3.17}, 
          'informant': {'aloof': 3.64, 'pl': 3.19, 'rigid': 4.30, 'total': 3.46}}}
    g = args.gender[0]
    a = args.answerer

    print("RESULTS")
    print(f"Aloof (cutoff={t[g][a]['aloof']}):")
    print(round(aloof_score/12, 2))
    if aloof_score/12 > t[g][a]['aloof']:
        print("Your aloofness score is higher than the cutoff for your gender and type of answerer.")
    print()
    print(f"Pragmatic language (cutoff={t[g][a]['pl']}):")
    print(round(pl_score/12, 2))
    if pl_score/12 > t[g][a]['pl']:
        print("Your pragmatic language score is higher than the cutoff for your gender and type of answerer.")
    print()
    print(f"Rigidity (cutoff={t[g][a]['rigid']}):")
    print(round(rigid_score/12, 2))
    if rigid_score/12 > t[g][a]['rigid']:
        print("Your rigidity score is higher than the cutoff for your gender and type of answerer.")
    print()
    print(f"Total (cutoff={t[g][a]['total']}):")
    print(round(total_score/36, 2))
    if total_score/36 > t[g][a]['total']:
        print("Your average score is higher than the cutoff for your gender and type of answerer.")
    print()
