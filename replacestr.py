
import json
dir="unpack/package.json"
js = json.load(open(dir,'r',encoding='UTF-8'))
print(js["version"])

str1='if(this.account.subscription){return"pro"}'
str1fix='if(true){/* 主页右上角 */return"pro"}'
str2='!account.subscription'
str2fix='false'
str3='!this.account.subscription'
str3fix='false'
str4='isPro(){return!!this.account?.subscription}'
str4fix='isPro(){return true}'
str5='#ca(){if(this.theme==="default"'
str5fix='#ca(){return false;if(this.theme==="default"'
# copyAppVersion() 复制版本号函数

filename="unpack/output/app-bundle.js"
with open(filename,'r',encoding='UTF-8') as file:
	data = file.read()
	data = data.replace(str1, str1fix)
	data = data.replace(str2, str2fix)
with open(filename,'w',encoding='UTF-8') as file:
	file.write(data)
	file.close
