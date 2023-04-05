from tkinter import *
from tkinter import messagebox
import os
import socket





font=('맑은 고딕', 10)



# 자동설정
def setting_auto():
    if messagebox.askyesno('확인', '입력된 IP가 제거됩니다.\n\n변경 하시겠습니까?'):
        print('netsh interface ip set address "이더넷" dhcp')
        print('netsh interface ip set dns name="이더넷" dhcp')
        os.system('netsh interface ip set address "이더넷" dhcp')
        os.system('netsh interface ip set dns name="이더넷" dhcp')
    else:
        pass

# 수동설정 1
def setting_1():
    root = Toplevel()
    root.title('IP')
    root.geometry('200x150+700+300')
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
        print('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        print('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        print('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        os.system('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        os.system('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        os.system('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        messagebox.showinfo('완료', ip_address+'로 변경 되었습니다.')
        root.destroy()
        
    def end_setting(event=True):
        root.destroy()
        
    change_btn = Button(root, text='적용', width=15, command=change_ethernet_setting, relief='groove')
    change_btn.pack(padx=10, pady=10)
    
    entry.bind('<Return>', change_ethernet_setting)
    root.bind('<Escape>', end_setting)



# 수동설정 2
def setting_2():
    root = Toplevel()
    root.title('IP')
    root.geometry('200x150+700+300')
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
        print('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        print('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        print('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        os.system('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        os.system('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        os.system('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        messagebox.showinfo('완료', ip_address+'로 변경 되었습니다.')
        root.destroy()
        
    def end_setting(event=True):
        root.destroy()
        
    change_btn = Button(root, text='적용', width=15, command=change_ethernet_setting, relief='groove')
    change_btn.pack(padx=10, pady=10)
    
    entry.bind('<Return>', change_ethernet_setting)
    root.bind('<Escape>', end_setting)



def root_window():
    if messagebox.askyesno('매뉴얼', '[변경 방법]을 확인하고 [예]를 클릭해주세요.\n\n1. 변경 옵션 선택 [민수/방산]\n\n2. 변경할 [IP 입력]\n\n3. [적용] 버튼 클릭'):
        win = Tk()
        win.title('IP 변경')
        win.geometry('250x220+400+300')
        win.resizable(False, False)	
        lab_ip = Label(win, text=' 현재 IP : '+socket.gethostbyname(socket.gethostname())+' ', justify ='left', background='darkgreen', fg='white', font=('맑은 고딕', 12))
        lab_ip.pack(padx=5, pady=15)
        # lab_manual = Label(win, text='버튼을 누르고 IP를 변경하세요.', justify ='left', font=font)
        # lab_manual.pack(padx=5, pady=10)
        btn1 = Button(win, text='민수 IP 설정', width=20, command=setting_1, font=font, relief='groove')
        btn1.pack(padx=5, pady=10)
        btn2 = Button(win, text='방산 IP 설정', width=20, command=setting_2, font=font, relief='groove')
        btn2.pack(padx=5, pady=10)
        btn_auto = Button(win, text='자동 IP 설정', width=20, command=setting_auto, font=font, relief='groove')
        btn_auto.pack(padx=5, pady=10)
        # 메인 윈도우를 ESC로 종료하기
        def end_window(event=True):
            win.destroy()
        win.bind('<Escape>', end_window)
        win.mainloop()
    else:
        pass
root_window()