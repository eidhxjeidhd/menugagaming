import os
import time
from pystyle import Colors, Colorate

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    logo = """
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""
    print(Colorate.Diagonal(Colors.yellow_to_red, logo))
    
    thong_tin = f"""\033[1;97mTool By: \033[1;32mGà gaming            \033[1;97mPhiên Bản: \033[1;32mV4    
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m LINK ZALO\033[1;31m : \033[1;36mhttps://zalo.me/0338976200
\033[1;97m[\033[1;91m<>\033[1;93m YOUTUBE\033[1;31m : \033[1;32mGà gaming 
\033[1;97m[\033[1;91m<>\033[1;32m ADMIN\033[1;31m : \033[1;33mGà gaming 
\033[97m════════════════════════════════════════════════  
"""
    print(thong_tin)

def hien_thi_menu_lua_chon():
    banner()
    print("\033[1;36m[✦] MENU CHỨC NĂNG CÀY CUỐC ĐỘC QUYỀN GÀ GAMING:")
    print("\033[1;32m[1] => Auto Chạy Job GoLike TikTok")
    print("\033[1;32m[2] => Auto Buff Tương Tác TikTok")
    print("\033[1;32m[3] => Cấu hình tài khoản hệ thống")
    print("\033[1;31m[0] => Thoát Tool")
    print("\033[1;30m════════════════════════════════════════════════")

hien_thi_menu_lua_chon()
