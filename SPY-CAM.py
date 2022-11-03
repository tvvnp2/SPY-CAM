BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
from  os import system as DOWNLOAD
try:
	import requests
	import time 
	from requests import get as FX_PY
	from googlesearch import search
	from time import sleep
except :
	print(Yellow+f'= = = = ={White} DOWNLOAD LIBRARY{Yellow} = = = = =')
	DOWNLOAD('pip install requests')
	DOWNLOAD('pip install time')
	DOWNLOAD('pip install google')
	print(Yellow+f'= = = = ={White} DONE DOWNLOAD LIBRARY{Yellow} = = = = =')
	
def insecam():
	json=FX_PY('http://www.insecam.org/en/jsoncountries/',headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
	'Host': 'www.insecam.org',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
	}).json()['countries']
	value=[]
	for i in json:
		sleep(0.1)
		print(Yellow+'['+White+i+Yellow+f'] {White}-  '+json[i]['country']+'   {',json[i]['count'],'}')
		value.append(i)
	print('\n')
	print(' - '*8)
	print('\n')
	Choose=input(f'{White}[{Yellow}+{White}] - To Choose : ')
	if Choose in value :
		r=FX_PY('http://www.insecam.org/en/bycountry/'+Choose+'/',headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
	'Host': 'www.insecam.org',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
		}).text
		s=r.split('pagenavigator("?page=",')[1]
		next=s.split(',')[0]
		next=int(next)
		
		
		S=r.split('"thumbnail-item__wrap" href="')
		for i in S :
			Y=i.split('" ')[0]
			if 'html' in Y:
				pass
			else:
				time.sleep(0.1)
				url='http://www.insecam.org'+Y
				print(url)
				
		info=FX_PY(url,headers={
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
			'Host': 'www.insecam.org',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
				}).text
		for i in range(2,next):
					print(i)
					url='http://www.insecam.org/en/bycountry/RS/?page='+str(i)
					r=FX_PY(url,headers={
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
				'Cache-Control': 'max-age=0',
				'Connection': 'keep-alive',
				'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
				'Host': 'www.insecam.org',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
					}).text
					S=r.split('"thumbnail-item__wrap" href="')
					for i in S :
						Y=i.split('" ')[0]
						time.sleep(0.1)
						if 'html' in Y:
							pass
						else:
							url='http://www.insecam.org'+Y
							print(url)
							
							
						
	else:
		print(f'{White}[{Red}-{White}] - The Code Not Found !')
	
	
	

print(f'''
{Red}
   ___ _____   __    ___   _   __  __ 
  / __| _ \ \ / /__ / __| /_\ |  \/  |
  \__ \  _/\ V /___| (__ / _ \| |\/| |
  |___/_|   |_|     \___/_/ \_\_|  |_|
                                      
                                      
	 {Yellow}[{White}1{Yellow}] {White}- Contry   {Yellow}[{White}2{Yellow}] {White}- Placee
	         {Yellow}[{White}3{Yellow}] {White}- All
''')
print('\n')
Q=f'{White}[{Yellow}+{White}] -'
try:
		choose=int(input(Q+' Choose : '))
		if choose == ' ' :
			print('\nPLEASE CHOOSE NUMBER')
		elif choose == None :
			print('\nPLEASE CHOOSE NUMBER')
		else: 
			pass
except :
		print('\nENTER NUMBER PLEASE')
try:
	str(choose)
except :
	#print('\nPLEASE CHOOSE NUMBER')
	exit()
num=[1,2,3]
if choose in num :
	pass
else :
	print('\nPLEASE CHOOSE NUMBER')
	exit()
print('\n\n')
print(' - '*8)
print('\n'*2)
if choose == 1:
	insecam()
elif choose == 3 :
	webs=[]
	for i in search('webcam7', tld="co.in", num=50000, stop=90000, pause=0):
		webs.append(i)
	for i in webs:
		if 'webcam' in i:
				pass
		else:
				try:
					r=FX_PY(i).text
				except :
					pass
				if 'POWERED BY' in r or 'powered by' in r :
					print(i)
				else:
					pass
	
	
	





if choose == 2:
	json=FX_PY('http://www.insecam.org/en/jsontags/',headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
	'Host': 'www.insecam.org',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
	}).json()['tags']
	tar=0
	jsontags=[]
	for i in json:
		jsontags.append(i)
		
		print(Yellow+'['+White+str(tar)+Yellow+f']{White} - '+i)
		tar+=1
		sleep(0.1)
	print('\n')
	print(' - '*8)
	print('\n')
	try:
		chos=int(input(Q+' Choose : '))
	except :
		print('\nENTER NUMBER PLEASE')
		exit()
	print('\n\n\n')
	
	r=FX_PY('http://www.insecam.org/en/bytag/'+jsontags[chos]+'/',headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
	'Host': 'www.insecam.org',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}).text
	s=r.split('pagenavigator("?page=",')[1]
	next=s.split(',')[0]
	next=int(next)
	S=r.split('"thumbnail-item__wrap" href="')
	for i in S :
		Y=i.split('" ')[0]
		if 'html' in Y:
			pass
		else:
			time.sleep(0.1)
			url='http://www.insecam.org'+Y
			print(url)
			
	info=FX_PY(url,headers={
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
			'Host': 'www.insecam.org',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
				}).text
				
	for i in range(2,next):
					
					url='http://www.insecam.org/en/bycountry/RS/?page='+str(i)
					r=FX_PY(url,headers={
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
				'Cache-Control': 'max-age=0',
				'Connection': 'keep-alive',
				'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
				'Host': 'www.insecam.org',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
					}).text
					S=r.split('"thumbnail-item__wrap" href="')
					for i in S :
						Y=i.split('" ')[0]
						time.sleep(0.1)
						if 'html' in Y:
							pass
						else:
							url='http://www.insecam.org'+Y
							print(url)
	print('- - - - END - - - - ')
							
							
						
	
