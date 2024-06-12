#Returns the Ratio of the score
def get_options_ratio(option, total):
    return (option / total)

#Ratings compared to test score
Excellent = .9
Very_Good = .8
Good = .7
Needs_Improvement = .6
Unacceptable = 0
def get_faculty_rating(ratio):
 #Returns rating compared to test score     
      if ratio >= Excellent:
        return ('Excellent')
      elif ratio >= Very_Good:
        return ('Very Good')    
      elif ratio >= Good:
        return ('Good')
      elif ratio >= Needs_Improvement:
        return ('Needs Improvement')
      else: ratio >= Unacceptable 
      return ('Unacceptable')
   
           

           