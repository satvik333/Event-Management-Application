from readJson import readjson

class readinputfile:
    def read_input_file(inputFilePath):
        try:
            inputFileData = readjson.readJsonFile(inputFilePath)
            return inputFileData
        except Exception as e:
            print('Error while reading input file:', e)
            return None