
import json
dir="unpack/package.json"
js = json.load(open(dir,'r',encoding='UTF-8'))
print(js["version"])

# 主页右上角
str1='if(this.account.subscription){return"pro"}return null'
str1fix='return"pro"'
# 一般特殊
str2='#ca(){if'
str2fix='#ca(){return false;if'
str3='isPro(){return!!this.account?.subscription}'
str3fix='isPro(){return true}'
# returnfalse 无空格特殊
str4='case"pro":return!this.account.subscription;'
str4fix='case"pro":return false;'
str5='get shouldShowActivatingCheatsCoachingTip(){return!this.account.subscription&&!this.hasUsedHotkeys}'
str5fix='get shouldShowActivatingCheatsCoachingTip(){return false&&!this.hasUsedHotkeys}'
# 通用
str6='!this.account.subscription'
str6fix='false'
str7='!account.subscription'
str7fix=' false'
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
	data = data.replace(str7, str7fix)
with open(filename,'w',encoding='UTF-8') as file:
	file.write(data)
	file.close
