import os

query_result_path='expected\\queryResult\\'
for casefolder in os.listdir(query_result_path):
    index = 1
    for entity in os.listdir(query_result_path + casefolder):
        file = os.listdir(query_result_path + casefolder + '\\' + entity)[0]
        os.rename(query_result_path + casefolder + '\\' + entity + '\\' + file, query_result_path+ '..\\' + casefolder + '_' + entity.lower() + '_' + str(1000 + index)[2:4] + '.json')
        index = index + 1