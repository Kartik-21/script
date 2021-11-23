# pandas
# xlwriter
# openxl
# opencv
# numpy


import json
from googletrans import Translator
import sys
import time, os

languageCode = 'gu'
file = open('E:\\app_en.arb')
fileString = file.read()

print(file.name)

path = file.name[:file.name.rindex('\\') + 1]
print(path)
# convert json to python object
parsedJson = json.loads(fileString)
print(parsedJson)
translator = Translator()
#
for item in parsedJson:
    if not item[0] == '@':
        print(item)
        translatedString = translator.translate(parsedJson[item], src='en', dest=languageCode).text
        time.sleep(0.5)
        # print(translatedString)
        parsedJson[item] = translatedString
        # print(item)
        print(parsedJson[item])
#
print('=========Translated JSON =========\n')
# convert python to json object
print(json.dumps(parsedJson, ensure_ascii=False, indent=4))
#
newFile = open(path + 'app_' + languageCode + '.arb', 'w+', encoding='utf8')
newFile.write(json.dumps(parsedJson, indent=4, ensure_ascii=False))
#
# # command = "flutter pub run intl_translation:generate_from_arb --output-dir=lib/l10n " \
# #           "--no-use-deferred-loading lib/l10n/intl_messages.arb lib/l10n/intl_"+languageCode+".arb " \
# #           "lib/Utils/GenericLocalizations.dart"
# # os.system(command)
