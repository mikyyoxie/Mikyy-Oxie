import sys
import os
os.system('clear')
import requests
import threading
import time
import json,requests,time
from time import strftime
from tqdm import tqdm
from pystyle import Colorate, Colors, Write, Add, Center
 
def banner():
    print(f'''        
                   \033[1m\033[38;5;51m TOOLS BY MIKYY OXE
         
\033[1;37m╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮''')
t=(Colorate.Horizontal(Colors.white_to_black,"- - - - - - - - - - - - - - - - - - - - - - - - -"))
print(t)
def clear():
    if(sys.platform.startswith('win')):
        os.system('clear')
    else:
        os.system('clear')
gome_token = []
def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',

        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
    
def main_share():
    clear()
    banner()
    print()
    input_file = open(input(" ─> \033[1m\033[38;5;51m Input Cookie , Format ( txt ) : \033[1;37m")).read().split('\n')
    id_share = input(" ─> \033[1m\033[38;5;51m ID / URL Link Postingan : \033[1;37m")
    delay = int(input(" ─> \033[1m\033[38;5;51m Delay Share : \033[1;37m"))
    total_share = int(input(" ─> \033[1m\033[38;5;51m Jumlah Share : \033[1;37m"))
    print()
    print('\033[1;31m     [Loading] \x1b[38;2;233;233;233mSabar Ya ...', end='\r')
    all = get_token(input_file)
    total_live = len(all)
    print(f'\033[1;37m╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯''')
    print(f'\033[1;31m                    [ Live : \x1b[38;2;233;233;233m{total_live} \033[1;31mCookies ]')
    if total_live == 0:
        sys.exit()
    print(f'\033[1;37m╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮''')
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'             \033[1;37m[\033[1;37m{stt}\033[1;37m]\033[1;37m STATUS \033[1;37m|\033[1m\033[38;5;51m BERHASIL \033[1;37m|ID|\033[1;37m\033[1;93m {id_share} \033[1;37m|\n', end='\r')
            time.sleep(delay)
        if stt == total_share:
            break
    gome_token.clear()
    print(f'\033[1;37m╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯''')
    print()   
    input('  \033[1;37m[\033[1;31m SUKSES \033[1;37m] \033[1;37m Postingan Berhasil Di Bagikan | Tekan [\033[1m\033[38;5;51m Enter \033[1;37m] Ulangi \033[0m\033[0m')
while True:
    try:
        main_share()
    except KeyboardInterrupt:
        print('\n\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] \033[38;5;9m Terimakasih \033[0m')
        sys.exit()
