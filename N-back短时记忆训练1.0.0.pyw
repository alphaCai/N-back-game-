'''
给出连续数字，加入N-1模式，第N个数字是否与上1个数字相同，
来长期锻炼短时记忆储存的容量,可以通过N-2、N-3等模式拓展能力。
'''
import tkinter as tk
from random import randint
from time import sleep

n = 1
number = list(range(9))
count = 1
count_right = 0
count_wrong = 0
judgement = lambda x,y:x==y

def change_n1():
    global n,count,count_right,count_wrong,change_select1
    n,count,count_right,count_wrong = 1,1,0,0

def change_n2():
    global n,count,count_right,count_wrong,change_select2
    n,count,count_right,count_wrong = 2,1,0,0

def change_n3():
    global n,count,count_right,count_wrong,change_select3
    n,count,count_right,count_wrong = 3,1,0,0
   

def set_number():
    global number,n
    number = []
    for i in range(n):
        number.append(randint(0,9))
    label2['text'] = str(number)

def start_number():#开始时候 选择n-1、n-2、n-3等模式
    global number,n
    text = '开始回合数字{0}个,请记忆......'.format(n)
    label1['text'] = text
    sleep(1)
    set_number()
    '''
    for i in range(n):
        sleep(2)
        text = '第{0}个:{1}'.format(i+1,number[i])
        ###label1.config(text = text)
    '''
    return add_number()
             
def add_number():#每回合更新数字、更新提示语句和回合数
    global count
    number.append(randint(0,9))
    label1['text'] = '第{0}回合，数字是:{1}'.format(count,number[len(number)-1])
    count +=1
    ##label2['text'] = ' '
    
def com_yes():
    global number,count_right,count_wrong,text2,n
    x,y=number[len(number)-1],number[len(number)-1-int(n)]
    if judgement(x,y) == True:
        label2['text'] = '正确'
        count_right +=1
    else:
        label2['text'] = '错误'
        count_wrong +=1
    label3['text'] = '正确:' + str(count_right)
    label4['text'] = '错误:' + str(count_wrong)
    return add_number()

def com_no():
    global number,count_right,count_wrong,text2,n
    x,y=number[len(number)-1],number[len(number)-1-int(n)]
    if judgement(x,y) == False:
        label2['text'] = '正确'
        count_right +=1
    else:
        label2['text'] = '错误'
        count_wrong +=1
    label3['text'] = '正确:' + str(count_right)
    label4['text'] = '错误:' + str(count_wrong)
    return add_number()

if __name__ == '__main__':
    main = tk.Tk()
    main.geometry('680x480')
    main.title('短时记忆模拟训练')

    text1 = '实时消息'
    label1 = tk.Label(main,text=text1,bg='yellow',font=('Arial',16),width=40,height=3)
    label1.pack()
    label2 = tk.Label(main,text='初始数字(从左至右)',bg='purple',font=('Arial',12),width=30,height=3)
    label2.pack()
    label3 = tk.Label(main,text='正确:0',bg='blue',font=('Arial',12),width=10,height=3)
    label3.pack(side='left')
    label4 = tk.Label(main,text='错误:0',bg='red',font=('Arial',12),width=10,height=3)
    label4.pack(side='right')

    menuline = tk.Menu(main) #创建菜单栏
    file = tk.Menu(menuline,tearoff=0) #在菜单栏插入新下拉菜单，默认不下拉
    menuline.add_cascade(label='File',menu=file) #菜单栏的下拉菜单file名称为File

    file.add_command(label='N-1模式',command=change_n1)
    file.add_command(label='N-2模式',command=change_n2)
    file.add_command(label='N-3模式',command=change_n3)

    button1 = tk.Button(main,text='是',font=('Arial',12),width=30,height=2,command=com_yes)
    button1.pack()
    button2 = tk.Button(main,text='否',font=('Arial',12),width=30,height=2,command=com_no)
    button2.pack()
    button3 = tk.Button(main,text='开始',font=('Arial',12),width=8,height=2,command=start_number)
    button3.pack(side='bottom') 

    main.config(menu=menuline) #启用菜单
    main.mainloop()

    set_number()
    while True:
        add_number()
        sleep(1)

