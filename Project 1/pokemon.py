import csv
from collections import Counter

#round function check
#variable reduction check
#spacing

def isNaN(num):
    return num!= num

#Assignment 1.1
#Reading CSV file into a dictionary and creating a list of dictionaries.
with open('pokemonTrain.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    list_of_dictionaries=[{}] 
    list_of_dictionaries.remove({})
    total_fire_pokemon=0
    above_level=0
    #variables to find average attack, defence and hp values of pokemons above level 40 and below level 40 
    avg_atk_above_40=0
    avg_defence_above_40=0
    avg_hp_above_40=0
    avg_atk_below_40=0 
    avg_defence_below_40=0 
    avg_hp_below_40=0
    avg_atk_41_count=0
    avg_def_41_count=0
    avg_hp_41_count=0
    avg_atk_40_count=0
    avg_def_40_count=0
    avg_hp_40_count=0
#assignment 1.1 and 1.2
    for line in csv_reader:
        if line.get("type")=="fire": 
            if float(line.get('level'))>40:
                above_level=above_level+1       
            total_fire_pokemon=total_fire_pokemon+1
        list_of_dictionaries.append(line)
        #getting values of atk and def for assignment 1.2
        temp_atk= float(line.get("atk"))             
        if not isNaN(temp_atk) and float(line.get("level"))>40:
            avg_atk_above_40=temp_atk+avg_atk_above_40
            avg_atk_41_count=avg_atk_41_count+1
        temp_def= float(line.get("def"))
        if not isNaN(temp_def) and float(line.get("level"))>40:
            avg_defence_above_40=temp_def+avg_defence_above_40
            avg_def_41_count=avg_def_41_count+1
        temp_hp= float(line.get("hp"))
        if not isNaN(temp_hp) and float(line.get("level"))>40:
            avg_hp_above_40=temp_hp+avg_hp_above_40
            avg_hp_41_count=avg_hp_41_count+1
        
        temp_atk= float(line.get("atk"))
        if not isNaN(temp_atk) and float(line.get("level"))<40:
            avg_atk_below_40=temp_atk+avg_atk_below_40
            avg_atk_40_count=avg_atk_40_count+1
        temp_def= float(line.get("def"))
        if not isNaN(temp_def) and float(line.get("level"))>40:
            avg_defence_below_40=temp_def+avg_defence_below_40
            avg_def_40_count=avg_def_40_count+1
        temp_hp= float(line.get("hp"))
        if not isNaN(temp_hp) and float(line.get("level"))>40:
            avg_hp_below_40=temp_hp+avg_hp_below_40
            avg_hp_40_count=avg_hp_40_count+1

     
file = open('pokemon1.txt','w')
file.write( 'Percentage of fire type Pokemons at or above level 40 = '+str(round((above_level/total_fire_pokemon)*100,0)))
file.close()


#Assingment 1.2
#print(list_of_dictionaries)
common_type=[]

for pokemon in list_of_dictionaries:
   # print(pokemon)
    if pokemon['type']=="NaN":                                  #Check if a pokemon has NaN type
        weakness = pokemon.get('weakness')                      #if yes, then get the weakness of that pokemon
        for a in list_of_dictionaries:                          #Go through weakness of all pokemon
            if a['weakness']== weakness :                       #if weakness of a pokemon matches the weakness of the NaN pokemon
                common_type.append(a['type'])
        result = Counter(common_type).most_common(1)[0][0]
        pokemon['type']=result
        common_type.clear()

    #Assignment 1.3
    if isNaN(float(pokemon.get("atk"))) and float(pokemon['level'])>40:
        pokemon['atk']=round(avg_atk_above_40/avg_atk_41_count,0)
    elif isNaN(float(pokemon.get("atk"))) and float(pokemon['level'])<=40:
        pokemon['atk']=round(avg_atk_below_40/avg_atk_40_count,0)
    
    if isNaN(float(pokemon.get("def"))) and float(pokemon['level'])>40:
        pokemon['def']=round(avg_defence_above_40/avg_def_41_count,0)
    elif isNaN(float(pokemon.get("def"))) and float(pokemon['level'])<=40:
        pokemon['def']=round(avg_defence_below_40/avg_def_40_count,0)
    
    if isNaN(float(pokemon.get("hp"))) and float(pokemon['level'])>40:
        pokemon['hp']=round(avg_hp_above_40/avg_hp_41_count,0)
    elif isNaN(float(pokemon.get("hp"))) and float(pokemon['level'])<=40:
        pokemon['hp']=round(avg_hp_below_40/avg_hp_40_count,0)


#writing to CSV file
keys = list_of_dictionaries[0].keys()
with open("pokemonResult.csv",'w',newline='') as outputfile:
    dict_writer = csv.DictWriter(outputfile, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_of_dictionaries)
    
#print(list_of_dictionaries)

#Assignment 1.4
result_personality=[]
def add_personalities(pokemon_type,list_of_personalities):
    #for line in list_of_personalities:
        for Item in list_of_personalities:
          if Item not in result_personality:
            result_personality.append(Item)
          


#Assignment 1.4
pokemon_personalities={}
for line in list_of_dictionaries:
    pokemon_type=line.get('type')
    if not (pokemon_personalities.get((pokemon_type))):
        pokemon_personalities[pokemon_type]=[]

for pokemon_type in pokemon_personalities:
    personalities_list=[]
    for dictionary in list_of_dictionaries:
        if(pokemon_type==dictionary['type']):
                pokemon_personality=dictionary.get('personality')
                if (pokemon_personality not in personalities_list):
                    personalities_list.append(pokemon_personality)
    sorted_list= sorted(personalities_list)
    pokemon_personalities[pokemon_type]=sorted_list   
#print("\n")
#print(pokemon_personalities)

#print("\n")

sorted_dict = dict(sorted(pokemon_personalities.items(),key=lambda x:x[0].lower()))
#print(sorted_dict)

# Assignment 5
average_hp=0
count=0


for pokemon in list_of_dictionaries:
    hp_level=pokemon.get('stage')
    #print(hp_level)
    if hp_level == "3.0":
        count=count+1
        average_hp=average_hp+float(pokemon['hp'])


#print(" Average hit point for Pokemons of stage 3.0 = ",round((average_hp/count),0))     
file = open('pokemon5.txt','w')
file.write( 'Average hit point for Pokemons of stage 3.0 = '+str(round((average_hp/count),0)))
file.close()
csv_file.close()
outputfile.close()

