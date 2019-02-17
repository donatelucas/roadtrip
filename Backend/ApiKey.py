import sys
import os




class ApiKey():
    '''
    Singleton class whose instance contains a parsed Api.config in a dictionary. search key to return 
    '''
    instance = None

    @staticmethod
    def getInstance(): #call this instead
        if not ApiKey.instance:
            ApiKey.instance = ApiKey()
        return ApiKey.instance



    def __init__(self): #do not call this
        self.__keyDict = {}
        f = open('API.config','r')
        arr = f.read().split(',')
        count = 0
        for i in arr:
            if count % 2 == 0:
                self.__keyDict[arr[count]]=arr[count+1]
            count += 1
        print(self.__keyDict)

    def getKey(self,key):
        value = ''
        try:
            value = self.__keyDict[key]
        except:
            print('ERROR______VALID API KEY NOT ENTERED')
        else:
            value = "no value found"
        return value


