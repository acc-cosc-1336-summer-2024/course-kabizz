import decisions
#Get test score from user 
score = float(input('Enter your test score: ')) 
#Get total points possible points in test from end user
total = int(input('Enter total possible points that can be made on test: '))  
#This calculates the score to be displayed for end user     
average = decisions.get_options_ratio(score, total)
#This calculates the rating to be displayed for end user
rating = decisions.get_faculty_rating (average)
#This displays the score and the rating to the end user
print ('Your score is', average, 'percent.', 'Which is', rating)
 



