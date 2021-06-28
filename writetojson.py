import json
import os

entitynames = []

def get_entities(testdata):
    entityPath = 'testData\\' + testdata
    result = []
    for entity in os.listdir(entityPath):
        result.append(entity.split('=')[1].lower())
    return result

def write_param(entity_name):
    param_path = 'params\\'
    with open(param_path + 'param_raw_' + entity_name + '.json', mode='w+') as f:
        dict_params = {
            'Actions': {
                'isSpcifyDay': "true",
                'job-bookmark-enable': 'job-bookmark-enable'
            }
        }
        json.dump(dict_params, f, indent=4)
    f.close()

casePath = 'case\\'
case_files = os.listdir(casePath)
for case in case_files:
    with open(casePath + case, encoding='utf8') as f:
        datas = json.load(f)
        entitynames = get_entities(datas['TestData'])
        f.close()
    for entity in entitynames:
        with open(casePath + case, mode='w+') as f:
            datas["Triggers"].append({"TriggerName": "trigger1","CrawlerName": "clawer1" + entity})
            # case_004 skip
            datas["Query"].append({"QueryName": "query1", "ExpectedData": "expected1" + entity})
            json.dump(datas, f, indent=4)
        f.close()
        write_param(entity)
