##lesson14
##ex1
## copy()
list_subjects=["Math","Phisics","Programming"]
new_list=list_subjects.copy()
print(new_list)

##ex2
##
list_subjects=["Math","Phisics","Programming"]
new_list=list(list_subjects)
print(new_list)


##ex3
## 

list_subjects=["Math","Phisics","Programming"]
new_list=["Math2","Phisics2","Programming2"]
sum_list=list_subjects + new_list
print(sum_list)

##ex4
## 

list_subjects=["Math","Phisics","Programming"]
list_subjects2=["Math2","Phisics2","Programming2"]

for x in list_subjects2:
    list_subjects.append(x)


print(list_subjects)
print(list_subjects2)



##ex5
## 

list_subjects=["Math","Phisics","Programming"]
list_subjects2=["Math2","Phisics2","Programming2"]

list_subjects.extend(list_subjects2)

print(list_subjects)
print(list_subjects2)

###tuples
##ex6
games=("Pubg","Freeefire","Fifa 2025")
print(games)

##ex7
games=("Pubg","Freeefire","Fifa 2025","Pubg")
print(games)


##ex8
games=("Pubg","Freeefire","Fifa 2025","Pubg")
print(len(games))

##ex9
games=("Pubg")
print(games,type(games))

##ex10
games=tuple("Pubg")
print(games,type(games))

##ex11
games=("Pubg",)
print(games,type(games))




##ex12
games=(1000,)
print(games,type(games))
##ex13
games=(1000)
print(games,type(games))



#$##
##ex14
games=(1,22,33)
print(games)


##ex15
games=(False,22,"33")
print(games)






##ex16
games=tuple(("Pubg","Freeefire","Fifa 2025"))
print(games)



##ex17
games=tuple(("Pubg","Freeefire","Fifa 2025"))
print(games[0])


##ex18
games=tuple(("Pubg","Freeefire","Fifa 2025"))
print(games[2])


##ex19
games=tuple(("Pubg","Freeefire","Fifa 2025"))
print(games[-1])


##ex20
games=tuple(("Pubg","Freeefire","Fifa 2025"))
print(games[1:])




##ex21
games=tuple(("Pubg","Freeefire","Fifa 2025"))
if "Pubg" in games:
    print("yes we have \"Pubg\"")
print(games[1:])



##ex22
games=tuple(("Pubg","Freeefire","Fifa 2025"))
games_list=list(games)
games_list[1]="freefire"
games=tuple(games_list)
print(games)

##ex23
games=tuple(("Pubg","Freeefire","Fifa 2025"))
games_list=list(games)

games_list.append("cards")
games=tuple(games_list)
print(games)


##ex24
games=tuple(("Pubg","Freeefire","Fifa 2025"))
games_tuple2=tuple(("Pubg2","Freeefire2","Fifa 20252"))
##games=games+games_tuple2
games+=games_tuple2
print(games)



##ex25
games=tuple(("Pubg","Freeefire","Fifa 2025"))
games_tuple2=tuple(("Pubg2",))
##games=games+games_tuple2
games+=games_tuple2
games_tuple2+=games
print(games)
print(games_tuple2)

##ex26
games=tuple(("Pubg","Freeefire","Fifa 2025"))
games_list=list(games)

games_list.remove("Freeefire")
games=tuple(games_list)
print(games)


##ex27
games=tuple(("Pubg","Freeefire","Fifa 2025"))

del games
##print(games)


##ex28
games=tuple(("Pubg","Freeefire","Fifa 2025"))

game1=games[0]
game2=games[1]
game3=games[2]

print(games,game1,game2,game3)


##ex29
games=tuple(("Pubg","Freeefire","Fifa 2025"))

(game1,game2,game3)=games

print(games,game1,game2,game3)


##ex30
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))

(game1,game2,*game3)=games

print(games,game1,game2,game3)



##ex31
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))

game1,*game2,game3=games

print(games,game1,game2,game3)


##ex32
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))

for x in games:
    print(x)


##ex33
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))

for i in range(len(games)):
    print(games[i])

##ex34
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
i=0
while i<len(games):
    print(games[i])
    i+=1



##ex35
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
i=-1
while i<len(games) - 1:
    i+=1
    print("----", games[i])



##ex36
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
games2=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
games3=games+games2
print(games3)


##ex37
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))

print(games * 2)
print(games * 3)

##ex38
## count
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
num=games.count("Pubg")
print(num)

games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty","Pubg","Freeefire","Fifa 2025","call of duty"))
num=games.count("Pubg")
print(num)



##ex38
## count
games=tuple(("Pubg","Freeefire","Fifa 2025","call of duty"))
num=games.index("Pubg")
print(num)



