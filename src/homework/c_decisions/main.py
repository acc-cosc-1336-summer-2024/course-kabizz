#
import decisions
#Get input from user           
average = decisions.get_options_ratio(int(input('Enter your test score: ')), int(input('Enter total possible points that can be made on test: ')))
rating = decisions.get_faculty_rating (average)
print ('Your score is', average, 'percent.', 'Which is', rating)
 



