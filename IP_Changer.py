from tkinter import *
import os

def setting_1():
    root = Toplevel()
    root.title('IP')
    root.geometry('200x150+550+400')
    lebel = Label(root, text="IP 입력")
    lebel.pack(padx=10, pady=10)
    entry = Entry(root)
    entry.pack(padx=10, pady=10)
    entry.focus()

    # 입력필요인 부분은 환경에 맞게 변경하고 사용해야 합니다.
    def change_ethernet_setting(event=True):
        ip_address = entry.get()
        subnetmask = '입력필요'
        ip_split = ip_address.split('.') # IP를 .단위로 스플릿
        gateway = '.'.join(ip_split[:3] + ['254']) # 스플릿 값 중 3개만 가져옴 +254
        dns1 = '입력필요'
        dns2 = '입력필요'
        print(ip_address, subnetmask, gateway, dns1, dns2)
        # os.system('netsh interface ip set address "이더넷" static '+input_ip+' 255.255.255.0 '+input_gate)
        # os.system('netsh -c int ip set dns name="이더넷" static "10.10.41.10" primary')
        # os.system('netsh -c int ip add dns name="이더넷" "10.10.41.11" index=2')
        
    def end_setting(event=True):
        root.destroy()
        
    change_btn = Button(root, text='적용', width=15, command=change_ethernet_setting)
    change_btn.pack(padx=10, pady=10)

    entry.bind('<Return>', change_ethernet_setting)
    root.bind('<Escape>', end_setting)









win = Tk()
win.title('IP')
win.geometry('250x290+500+400')
win.resizable(False, False)	
intro = Label(win, text='''
IP변경 프로그램

1. 망 구분 선택 클릭 (민수/방산)
    A. 민수PC
    B. 방산PC

2. IP 입력창에 IP 입력

3. 적용 버튼 클릭
''', justify  = 'left')
intro.pack()
btn1 = Button(win, text='민수PC', width=20, command=setting_1)
btn1.pack(padx=5, pady=10)

# btn2 = Button(win, text='방산PC', width=20, command=pop81)
# btn2.pack(padx=5, pady=10)




# 메인 윈도우를 ESC로 종료하기
def end_window(event=True):
    win.destroy()
win.bind('<Escape>', end_window)


win.mainloop()

