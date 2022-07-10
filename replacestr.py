
import json
dir="unpack/package.json"
js = json.load(open(dir,'r',encoding='UTF-8'))
print(js["version"])

str1='if(this.account.subscription){return"pro"}return null}'
str1fix='if(true){return"pro"}return null}'
str2='!account.subscription'
str2fix='false'
filename="unpack/output/app-bundle.js"
with open(filename,'r',encoding='UTF-8') as file:
	data = file.read()
	data = data.replace(str1, str1fix)
	data = data.replace(str2, str2fix)
with open(filename,'w',encoding='UTF-8') as file:
	file.write(data)
