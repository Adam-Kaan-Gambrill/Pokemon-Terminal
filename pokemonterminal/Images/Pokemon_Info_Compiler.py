import os
import Pokemon_Image_Brightness_Finder as imageBrightness
import requests

# folderPath = '/home/mark/Adams_Dev_Test/Pokemon-Terminal/pokemonterminal/Images/HQ_Images/'
folderPath = '/home/adam/Pokemon_Images/Pokemon/assets/HQ_Images/'

list = os.listdir(folderPath)
list.sort()

# open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Temp.txt', 'w').close()
# open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Log_Temp.txt', 'w').close()
open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Temp.txt', 'w').close()
open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Log_Temp.txt', 'w').close()

# pkmnTypeVariants = open('/home/mark/Adams_Dev_Test/Pokemon_Mega_And_Regional_Type_Variations.py').read().split()
# pkmnNameLog = open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Log.txt').read().split()
pkmnTypeVariants = open('/home/adam/Pokemon_Images/Adams_Tests/Pokemon_Mega_And_Regional_Type_Variations.py').read().split()
pkmnNameLog = open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Log.txt').read().split()

testCount = 0

for fileName in list:
    # if fileName in pkmnNameLog:
    #     continue
    # if fileName in pkmnTypeVariants:
    #     testCount = testCount + 1
    #     print(testCount)
    #     print(fileName)
    #     # with open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Temp.txt', 'a') as amendCompiledCsv:
    #     with open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Temp.txt', 'a') as compiledCsv:
    #         amendCompiledCsv.write(str(pokemonDexNoFixed) + '\t' + pokemonName.title() + '\t' + str(imageBrightness.pokemonImageBrightnessFinder(folderPath, fileName)) + multipleTypes.title() + '\n')
        # continue


    
    pokemonDexNo = fileName[:4]
    pokemonDexNo = int(pokemonDexNo)
    pokemonDexNoFixed = ("{:04d}".format(pokemonDexNo))
    pokemonName = fileName[5:-4]
    fixedPokemonName = pokemonName.replace('_', '-')
    pkmnSearchVariable = requests.get("https://pokeapi.co/api/v2/pokemon/" + fixedPokemonName)

    pkmnNameVariable = pkmnSearchVariable.json()['name']

    pkmnTypesVariable = pkmnSearchVariable.json()['types']

    pkmnAbilitiesVariable = pkmnSearchVariable.json()['abilities']

    # pkmnTypesVariable = disp
    # pkmnAbilitiesVariable = pkmnAbilitiesVariable



    print(pkmnNameVariable)

    for item in pkmnTypesVariable:
        print(item['type']['name'])



    for item in pkmnAbilitiesVariable:
        if not item['is_hidden']:
            test = (item['ability']['name']).title()
            print(test)

    for item in pkmnAbilitiesVariable:
        if item['is_hidden']:
            testing = (item['ability']['name']).title()
            print(testing)

    # pokemonTypes = ['Fire', 'Psychic']
    multipleTypes = ''


# print(pkmnTypesVariable)
# print(pkmnAbilitiesVariable)


    # for pokeType in pkmnTypesVariable:
    #     multipleTypes = multipleTypes + '\t' + pokeType
    # with open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Temp.txt', 'a') as compiledCsv:
    # # with open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Temp.txt', 'a') as compiledCsv:
    #     compiledCsv.write(str(pokemonDexNoFixed) + '\t' + pokemonName.title() + '\t' + str(imageBrightness.pokemonImageBrightnessFinder(folderPath, fileName)) + multipleTypes.title() + '\n')
    # with open('/home/mark/Adams_Dev_Test/Pokemon_Compiled_Info_Log_Temp.txt', 'a') as infoLog:
    # # with open('/home/adam/Pokemon_Images/Pokemon_Compiled_Info_Log_Temp.txt', 'a') as infoLog:
    #     infoLog.write(fileName + '\n')
