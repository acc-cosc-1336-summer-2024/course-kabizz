import decisions
#Get test score from user 
score = int(input('Enter your test score: ')) 
#Get total points possible points in test from user
total = int(input('Enter total possible points that can be made on test: '))  
#This calculates the score to be displayed for user     
average = decisions.get_options_ratio(score, total)
#This calculates the rating to be displayed for user
rating = decisions.get_faculty_rating (average)
#This displays the score and the rating to the user
print ('Your score is', average, 'percent.', 'Which is', rating)
 



