import file

class ApiKey():
    instance = None

    @staticmethod
    def getInstance():
        if not ApiKey.instance:
            ApiKey.instance = ApiKey.__init__()
        return ApiKey.instance



    def __init__(self):
        self.__keyDict = {}
        f = open('API.config','r')
        arr = f.read().split(',')
        count = 0;
        for i in arr:
            if count % 2 == 0:
                self.__keyDict[arr[count]]=arr[count+1]
        print(self.__keyDict)

