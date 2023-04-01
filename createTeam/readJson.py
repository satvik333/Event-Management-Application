import json

class readjson:
    def readJsonFile(filePath):
        try:
            file = open(filePath)
            fileData = json.loads(file.read())
            return fileData
        except Exception as e:
            print('Error while reading a file', e)