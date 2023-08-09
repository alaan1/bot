from telebot import TeleBot
from telebot import types
from requests import *
from uuid import uuid4
from random import *
from os import system,path
from json import (dumps,loads)
from datetime import datetime
from time import sleep
SESSION = uuid4()
bot = TeleBot("5062270147:AAHHD9LiOtC3dAA4nO1do3GQ4cKX0gvwtJA")

kay =types.InlineKeyboardMarkup()
cls = types.InlineKeyboardMarkup()
ka = types.InlineKeyboardMarkup()
yes = types.InlineKeyboardMarkup()
Info = types.InlineKeyboardMarkup()
call = types.InlineKeyboardButton("تسجيل الدخول بحسابك 🔛",callback_data="click")
cal = types.InlineKeyboardButton("التحكم بالحساب  ▶️",callback_data="cont")
ca = types.InlineKeyboardButton("الرجوع 🔙",callback_data="back")
Dev = types.InlineKeyboardButton("مبرمج البوت ➰",url="t.me/M_L_F")
kay.add(call,cal)
clea= types.InlineKeyboardButton(" حذف جلسة الحساب ( يتم تسجيل الخروج من حسابك فقط ⚠️ ) ",callback_data="clear")
info= types.InlineKeyboardButton("معلومات حسابك ❕",callback_data="info")
kay.add(Dev)
ye = types.InlineKeyboardButton("نعم ❕",callback_data="yes")
gift= types.InlineKeyboardButton("إضافة كود هدية 🎁",callback_data="gift")
ka.add(ca)
cls.add(clea,ca)
yes.add(ye,ca)
Info.add(info,gift)
Info.add(ca)
@bot.message_handler(commands=['start'])

def start(message):
	
	bot.reply_to(message,"Welcome To The FlashCharge Bot 🔛 • \n\n- Your Name : "+str(message.chat.first_name)+"\n"+"- Your Id : "+str(message.chat.id)+"\n- UserName : @"+str(message.from_user.username)+"\n\n"+"-"*78+'\n'+"من خلال البوت يمكنك التحكم بحسابك على منصة  •",reply_markup=kay)
	

@bot.callback_query_handler(func=lambda call:True)


def alex(call):
	message = call.message

	if call.message:
		
		if call.data == "click":
			@bot.message_handler(content_types=['text'])
			def msg(message):
				login(message)
			m= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- حسناً ارسل رقمك مع كلمة السر مثال :\n\n- 077******** : xxx\n\n- الرقم على اليسار والـxxx هي كلمة سر حسابك •",reply_markup=ka)
			bot.register_next_step_handler(m,login)
			
		elif call.data == "back":
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- Your Name : "+str(message.chat.first_name)+"\n"+"- Your Id : "+str(message.chat.id)+"\n\n"+"-"*78+'\n'+"من خلال البوت يمكنك التحكم بحسابك على منصة  •",reply_markup=kay)
			
			
		elif call.data== "cont":
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- ستتم إضافة خيارات اخرى قريباً ❕",reply_markup=Info)
		if call.data == 'info':
				if path.exists("flashcharge.json") == True:
					with open('flashcharge.json','r') as c:
						Cooki=loads(c.read())
					Token = Cooki['cookies']['token']
					Rem = Cooki['cookies']['Rememper-me']
					InFo = post("https://api.flashcharge.cfd/user/get",headers={'Accept':'*/*',
'Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'Content-Length':'0','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Cookie':f'SESSION={Token}; remember-me={Rem}; token={Token}',
'Origin':'https://flashcharge.cfd',
'Referer':'https://flashcharge.cfd/',
'Req-Role':'user','Sec-Ch-Ua':'"Not)A;Brand";v="24", "Chromium";v="116"',
'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'"Android"','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-site','User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',})
					if '"code":0' in InFo.text and 'balance' in InFo.text:
						
						if "realName" in InFo.text and 'bankCode' in InFo.text:
							Number = '+964'+str(InFo.json()['detail']['accountInfo']['account'])
							Pas = InFo.json()['detail']['accountInfo']['password']
							n = int(InFo.json()['detail']['accountInfo']['createTime'])
							u = (f'{n}').split('000')[0]
							Creat = datetime.fromtimestamp(int(u))
							print(u)
							Balanes = InFo.json()['detail']['balance']
							Link = "https://flashcharge.cfd/register?code="+str(InFo.json()['detail']['shareCode'])
							Id = InFo.json()['detail']['accountInfo']['id']
							Name = InFo.json()['detail']['realName']
							if InFo.json()['detail']['bankCode'] == '86' :
								Bank = "ZainCash"
								
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''- الرقم : {Number} •
- كلمة السر : {Pas} •
- تأريخ إنشاء الحساب : {Creat} •
- الرصيد : {Balanes} •
- رابط الدعوه : {Link} •
- ايدي حسابك : {Id} •
----------------------------------

 • حساب البنك •
- الاسم : {Name} •
- طريقة الدفع : {Bank} •
- رقم الحساب : {Number} •''',reply_markup=ka)
						
							elif InFo.json()['detail']['bankCode'] == '87':
								Bank = "Fastbay"
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''- الرقم : {Number} •
- كلمة السر : {Pas} •
- تأريخ إنشاء الحساب : {Creat} •
- الرصيد : {Balanes} •
- رابط الدعوه : {Link} •
- ايدي حسابك : {Id} •
----------------------------------

 • حساب البنك •
- الاسم : {Name} •
- طريقة الدفع : {Bank} •
- رقم الحساب : {Number} •''',reply_markup=ka)
							elif InFo.json()['detail']['bankCode'] == None:
								
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''- الرقم : {Number} •
- كلمة السر : {Pas} •
- تأريخ إنشاء الحساب : {Creat} •
- الرصيد : {Balanes} •
- رابط الدعوه : {Link} •
- ايدي حسابك : {Id} •
----------------------------------

- لم تتم إضافة حساب بنكي (ZainCash ,  Fastbay) ⚠️ ''',reply_markup=ka)
								
						else:
							
							Number = '+964'+str(InFo.json()['detail']['accountInfo']['account'])
							Pas = InFo.json()['detail']['accountInfo']['password']
							n = int(InFo.json()['detail']['accountInfo']['createTime'])
							u = (f'{n}').split('000')[0]
							Creat = datetime.fromtimestamp(int(u))
							Balanes = InFo.json()['detail']['balance']
							Link = "https://flashcharge.cfd/register?code="+str(InFo.json()['detail']['shareCode'])
							Id = InFo.json()['detail']['accountInfo']['id']
							bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''- الرقم : {Number} •
- كلمة السر : {Pas} •
- تأريخ إنشاء الحساب : {Creat} •
- الرصيد : {Balanes} •
- رابط الدعوه : {Link} •
- ايدي حسابك : {Id} •
----------------------------------

- لم تتم إضافة حساب بنكي (ZainCash ,  Fastbay) ⚠️ ''',reply_markup=ka)
					elif '"code":403' in InFo.text and '"success":false' in InFo.text:
						bot.reply_to(message,"تم انتهاء جلسة حسابك ، هل تريد اعادة تسجيل الدخول  ؟!",reply_markup=yes)
						
							
							
					else:
						bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=InFo.text,reply_markup=ka)				
					
		
		elif call.data == 'gift':
				if path.exists("flashcharge.json") == True:
					@bot.message_handler(content_types=['text'])
					def ms(message):
						Gift(message)
					g = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="يمكنك اضافة كود الهدية في الوقت الحالي ✔️",reply_markup=ka)
					bot.register_next_step_handler(g,Gift)
				else:
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="يجب عليك تسجيل الدخول الى حسابك اولاً ❗",reply_markup=ka)
		elif call.data == 'clear':
				if path.exists("flashcharge.json") == True:
					system('rm -rf flashcharge.json')
					system('rm -rf flashchargeaccount.json')
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="تم حذف جلسة حسابك من البوت بنجاح 🟢",reply_markup=ka)
				elif path.exists('flashcharge.json') == False:
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="يجب عليك تسجيل الدخول الى حسابك اولاً ❗",reply_markup=ka)
		elif call.data == 'yes':
			m= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- حسناً ارسل رقمك مع كلمة السر مثال :\n\n- 077******** : xxx\n\n- الرقم على اليسار والـxxx هي كلمة سر حسابك •",reply_markup=ka)
			bot.register_next_step_handler(m,login)
			
		elif call.data == 'back':
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- Your Name : "+str(message.chat.first_name)+"\n"+"- Your Id : "+str(message.chat.id)+"\n\n"+"-"*78+'\n'+"من خلال البوت يمكنك التحكم بحسابك على منصة  •",reply_markup=kay)
				
				
			
def Gift(message):
	ms=message.text
	
	with open('flashcharge.json','r') as c:
		Cooki=loads(c.read())
	Token = Cooki['cookies']['token']
	GetGift = post("https://api.flashcharge.cfd/user/gift/get",headers={'Accept':'*/*',
'Accept-Language':'en-US,ar;q=0.9,en-US;q=0.8,en;q=0.7','Content-Length':'13',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
'Cookie':f'SESSION={Token}; token={Token}',
'Origin':'https://flashcharge.cfd',
'Referer':'https://flashcharge.cfd/',
'Req-Role':'user','Sec-Ch-Ua':'"Not)A;Brand";v="24", "Chromium";v="116"',
'Sec-Ch-Ua-Mobile':'?1',
'Sec-Ch-Ua-Platform':'"Android"','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-site','User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'},data={"code":str(ms)})
	if 'error_gift_already_taken' in GetGift.text:
		bot.reply_to(message,"كود الهدية تم استلامه من قبل بالفعل او تم استنفاذه ❗",reply_markup=ka)
	elif 'error_invalid_gift_code' in GetGift.text:
		bot.reply_to(message,"كود الهدية خطأ ‼️",reply_markup=ka)
	elif '"code":0' in GetGift.text and '"success":true' in GetGift.text:
		Denar = GetGift.json()['detail']
		bot.reply_to(message,f"تم أضافة ~> {Denar} ✔️ ",reply_markup=ka)
	elif "error_gift_min_buy" in GetGift.text:
		bot.reply_to(message,"كود الهدية هذا فقط للمستثمرين (الشاحنين بـ 5$ واكثر ) ⚠️",reply_markup=ka)
	elif '"code":403' in GetGift.text and '"success":false' in GetGift.text:
		bot.reply_to(message,"تم انتهاء جلسة حسابك ، هل تريد اعادة تسجيل الدخول تلقائياً ؟!",reply_markup=yes)
		
	else:
		bot.reply_to(message,GetGift.text)
					
			
def login(message):
		
			msg=message.text
			if ':' in msg:
				Number = msg.split(':')[0]
				pas = msg.split(':')[1]
				Login = post("https://api.flashcharge.cfd/signin",headers={'Accept':'*/*',
'Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','Content-Length':'39',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Cookie':f'SESSION={SESSION}',
'Origin':'https://flashcharge.cfd','Referer':'https://flashcharge.cfd/','Req-Role':'user','Sec-Ch-Ua':'"Not)A;Brand";v="24", "Chromium";v="116"','Sec-Ch-Ua-Mobile':'?1',
'Sec-Ch-Ua-Platform':'"Android"','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-site',
'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'},
data={'username':str(Number),
'password':str(pas)})
				if "error_pasword_error" in Login.text:
					bot.reply_to(message,"🔴 كلمة السر او الرقم غير صحيحين •",reply_markup=ka)
				elif "token" in Login.text:
					Cooki={};cookies='cookies'
					Cooki[cookies]= {"token":str(Login.json()['detail']['token']),"SiS":str(Login.json()['detail']['token']),"Rememper-me":str(Login.cookies.get_dict()['remember-me'])}
					with open('flashcharge.json','w') as alx:
						alx.write(dumps(Cooki))
						bot.reply_to(message,'🟢 تم تسجيل الدخول الى حسابك •',reply_markup=ka)
			
		

bot.infinity_polling()