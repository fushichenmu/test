import xmltodict
import json

def xml2dict(xml_file,rootTable='xml'):
    with open(xml_file,encoding = 'utf-8') as file_object :
        all_the_xmlStr = file_object.read()
        convertedDict = xmltodict.parse(all_the_xmlStr)
        #ensure_ascii 设置为False 中文可以转换
        jsonStr = json.dumps(convertedDict,ensure_ascii=False)
        convertedDict = json.loads(jsonStr)
        if rootTable:
            convertedDict=convertedDict[rootTable]
    return convertedDict

def dict2xml(self,file_Str_Dict):
    self.init_data(file_Str_Dict)
    if isinstance(self.data,str):
        try:
            self.data=json.loads(self.data)
        except:
            print('传入参数非json或dict类型，无法转换。')
            # traceback.print_exc()
            return None
    return xmltodict.unparse(self.data,pretty=True,encoding='utf-8')



if __name__ == '__main__':
    convertedDict = xml2dict('second_params.xml')
    print(convertedDict)

