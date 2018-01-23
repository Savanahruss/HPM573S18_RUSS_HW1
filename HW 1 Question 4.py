#-----Question 4
yours=['Yale','MIT','Berkley']
mine=['Geneseo','Yale','Duke']

ours1=mine+yours

ours2=[]
ours2.append(mine)
ours2.append(yours)

#Question 4.1
print(ours1)
print(ours2)
#Ours1 and Ours2 do not differ by the variables they have listed
#they only differ by the annotation because ours1 has all the names of schools
#in one list with no separation and ours2 has the names of schools but separated
#by two sets of square brackets


#Question 4.2
yours[1]='Stony Brook'
print(ours1)
print(ours2)
#After altering yours to include Stony Brook as the second element, we can see that the change only affects ours2
#because ours2 includes yours through the append function which allows for the list to be mutable whereas ours1
#includes yours through a simple list combination which does not allow for the updating of the list as changes
#are made to it through commands made later on in the code.


