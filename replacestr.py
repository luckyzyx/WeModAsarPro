
import json
dir="unpack/package.json"
js = json.load(open(dir,'r',encoding='UTF-8'))
print(js["version"])

str1='get badge(){'
str1fix='get badge(){this.account.subscription=true;'

# copyAppVersion() 复制版本号函数

filename="unpack/output/app-bundle.js"
with open(filename,'r',encoding='UTF-8') as file:
	data = file.read()
	data = data.replace(str1, str1fix)
with open(filename,'w',encoding='UTF-8') as file:
	file.write(data)
	file.close
