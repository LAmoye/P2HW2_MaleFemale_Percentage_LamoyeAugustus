# Gives Male and Female Percentage of a class
# Date
# CTI-110 P2HW2 - Male Female Percentage
# Lamoye Augustus

# Get class info on class total.
# Get info on Female total.
# Get info on Male total.
# Calculate precentage of males and females.
# Display results in precentage form.


classTotal = int(input("How many students are in your class? "))
print ()
femTotal = int(input("How many female students are in your class? "))
print ()
maleTotal = int(input("How many male students are in your class? "))
print ()
print ()
prcntMale = maleTotal / classTotal
prcntFem = femTotal / classTotal
print ("The percentage of females in this class are: ",format( prcntFem,'.0%'))
print ()
print ("The percentage of males in this class are: ",format( prcntMale,'.0%'))
