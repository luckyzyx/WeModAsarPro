
import json
dir="unpack/package.json"
js = json.load(open(dir,'r',encoding='UTF-8'))
print(js["version"])

str1='if(this.account.subscription){return"pro"}return null'
str1fix='/*主页右上角*/return"pro"'
str2='if(!this.account.subscription){this.#qt.open()}break;'
str2fix='break;'
str3='#ca(){if(this.theme==="default"||this.subscription){return false}this.#i.dispatch(n.ACTION_SET_SETTINGS,{theme:"default"},"theme_applier",true);return true}'
str3fix='#ca(){return false}'
str4='isPro(){return!!this.account?.subscription}'
str4fix='isPro(){return true}'
str5='!this.account.subscription'
str5fix='false'
str6='!account.subscription'
str6fix='false'

# copyAppVersion() 复制版本号函数

filename="unpack/output/app-bundle.js"
with open(filename,'r',encoding='UTF-8') as file:
	data = file.read()
	data = data.replace(str1, str1fix)
	data = data.replace(str2, str2fix)
	data = data.replace(str3, str3fix)
	data = data.replace(str4, str4fix)
	data = data.replace(str5, str5fix)
	data = data.replace(str6, str6fix)
with open(filename,'w',encoding='UTF-8') as file:
	file.write(data)
	file.close
