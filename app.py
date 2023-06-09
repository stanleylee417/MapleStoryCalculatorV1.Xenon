import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from Calculator import Ui_Form


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #page0
        self.ui.page0_btn[0].clicked.connect(self.submit_ui)
        self.ui.page0_btn[1].clicked.connect(self.save_data)
        self.ui.page0_btn[2].clicked.connect(self.read_data)
        #page1
        self.ui.page1_btn[0].textChanged.connect(self.equivalent)
        self.ui.page1_btn[1].activated.connect(self.equivalent)
        for i in range(12):
            self.ui.page1_data1[i].textChanged.connect(self.improve)
        #page2
        self.ui.page2_btn[0].clicked.connect(self.star)
        #page3
        self.ui.level.activated.connect(self.setlevel)
        for i in range(7):
            self.ui.page3_data1[i].textChanged.connect(self.StarFire)
        #Description
        self.ui.connection.activated.connect(self.connection)
        
        self.move(20,20)
        self.show()
    
    def submit_ui(self):
        empty=[30,56,56,56,64.4,64.4,64.4,56,56,56,152.145,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.page0_data=[]
        for i in range(len(self.ui.page0_data)):    #取得並檢查UI能力值
            try:
                if i==18:
                    num=float(self.ui.page0_data[i].currentText())
                else:
                    num=float(self.ui.page0_data[i].text())
                    if num<empty[i]:
                        num=empty[i]
            except Exception:
                num=empty[i]
                pass
            if i!=18:
                self.ui.page0_data[i].setText(str(int(num)))
            self.page0_data.append(num)

        try:#計算屬性
            self.ui_set()
            self.equivalent()
            self.improve()
            #self.star()
            #self.StarFire()
            #啟用增幅設定
            for i in self.ui.page1_btn:
                i.setEnabled(True)
            for i in self.ui.page1_data1:
                i.setEnabled(True)
            for i in self.ui.page2_data:
                for j in i:
                    j.setEnabled(True)
            for i in self.ui.page2_data1:
                i.setEnabled(True)
            for i in self.ui.page2_btn:
                i.setEnabled(True)
            for i in self.ui.page3_data1:
                i.setEnabled(True)
        except Exception:   #重設UI
            for i in range(26):
                if i!=18:
                    self.ui.page0_data[i].setText(str(empty[i]))
            self.submit_ui()
            pass
        
    def ui_set(self):
        setPER=[11,12,13,14,15,16,18,25]
        for i in setPER:
            self.page0_data[i]/=100
        #攻擊力
        self.att = self.page0_data[10] / ((4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))*(1+self.page0_data[16])*(1+self.page0_data[11])*(1+self.page0_data[12])*0.01*1.3125)
        #不吃%力敏幸
        self.ns  = self.page0_data[19]+self.page0_data[22]+self.page0_data[17]*3.9
        self.nd  = self.page0_data[20]+self.page0_data[23]+self.page0_data[17]*3.9
        self.nl  = self.page0_data[21]+self.page0_data[24]+self.page0_data[17]*3.9
        #力敏幸%
        self.sp  = round((self.page0_data[4]-self.page0_data[1]) / (self.page0_data[7]*self.page0_data[18]),2)-1
        self.dp  = round((self.page0_data[5]-self.page0_data[2]) / (self.page0_data[8]*self.page0_data[18]),2)-1
        self.lp  = round((self.page0_data[6]-self.page0_data[3]) / (self.page0_data[9]*self.page0_data[18]),2)-1
        #吃%的力敏幸
        self.ys  = (self.page0_data[4]-self.ns) / (1+self.sp) - (self.page0_data[7])*(1+self.page0_data[18])
        self.yd  = (self.page0_data[5]-self.nd) / (1+self.dp) - (self.page0_data[8])*(1+self.page0_data[18])
        self.yl  = (self.page0_data[6]-self.nl) / (1+self.lp) - (self.page0_data[9])*(1+self.page0_data[18])
        
    def save_data(self):
        try:
            self.submit_ui()
            fileName,filetype=QFileDialog.getSaveFileName(self,"另存新檔","./","aries (*.aries)")
            data=open(fileName,"w")
            data_save=[]
            for i in range(len(self.ui.page0_data)):
                if i==18:
                    data_save.append(str(self.ui.page0_data[i].currentIndex())+"\n")
                else:
                    data_save.append(str(int(self.ui.page0_data[i].text()))+"\n")
            data.writelines(data_save)
            data.close()
        except Exception:
            pass
    
    def read_data(self):
        try:
            fileName, filetype = QFileDialog.getOpenFileName(self,"選擇檔案","./","aries (*.aries)")
            data=open(fileName,"r")
            data_save=[]
            for i in iter(data):
                i=i.replace("\n","")
                data_save.append(i)
            for i in range(len(self.ui.page0_data)):
                if i==18:
                    self.ui.page0_data[i].setCurrentIndex(int(data_save[i]))
                else:
                    self.ui.page0_data[i].setText(str(data_save[i]))
            data.close()
            self.submit_ui()
        except Exception:
            pass

    def equivalent(self):
        try:
            input=float(self.ui.page1_btn[0].text())
        except Exception:
            input=1
            self.ui.page1_btn[0].setText(str(input))
            pass
        curIndex=self.ui.page1_btn[1].currentIndex()
        list_Index=[0,1,2,3,4,5,11,6,7,8,9]
        true_Index=[6,7,0,1,11,2,3,8,4,5,9]
        data=self.calc()
        
        page1_data=[]
        for i in range(11):
            page1_data.append((data[list_Index[curIndex]]-1)/(data[true_Index[i]]-1))
        
        for i in range(11):
            self.ui.page1_data[i].setText(str(round(page1_data[i]*input,2)))
        
    def improve(self):
        input=[]
        for i in range(12):
            if i==9:
                try:
                    num=float(self.ui.page1_data1[i].text())
                except Exception:
                    num=0
                    self.ui.page1_data1[i].setText(str(num))
                    pass
            else:
                try:
                    num=int(float(self.ui.page1_data1[i].text()))
                except Exception:
                    num=0
                    pass
                self.ui.page1_data1[i].setText(str(num))
            input.append(num)
        
        data=self.calc(input[0],input[1],input[2],input[3],input[4],input[5],input[6],input[7],input[8],input[9],input[10],input[11])
        for i in range(12):
            self.ui.page1_data1[i+12].setText("增幅 "+str(round((data[i]-1)*100,2))+"%")
        total=1
        for i in range(12):
            total*=data[i]
        self.ui.page1_data1[24].setText("總共 "+str(round((total-1)*100,2))+"%")
        
        setPER=[1,3,5,7,8,9,10,11]
        for i in setPER:
            input[i]/=100
        text=[0,0,0,0,0,0,0,0,0,0,0]
        text[0]=(self.ys+input[0]+(self.page0_data[7])*(1+self.page0_data[18]))*(1+self.sp+input[1])+self.ns   #力量
        text[1]=self.sp+input[1]+input[11]  #力量%
        text[2]=(self.yd+input[2]+(self.page0_data[8])*(1+self.page0_data[18]))*(1+self.dp+input[3])+self.nd   #敏捷
        text[3]=self.dp+input[3]+input[11]  #敏捷%
        text[4]=(self.yl+input[4]+(self.page0_data[9])*(1+self.page0_data[18]))*(1+self.lp+input[5])+self.nl   #幸運
        text[5]=self.lp+input[5]+input[11]  #幸運%
        text[6]=self.att+input[6] #攻擊
        text[7]=self.page0_data[16]+input[7]  #攻擊%
        text[8]=self.page0_data[11]+self.page0_data[13]+input[8]    #總傷+B傷
        text[9]=self.page0_data[15]+input[9]  #爆傷
        text[10]=1-(1-self.page0_data[14])*(1-input[10]) #無視
        setPER=[1,3,5,7,8,9,10]
        for i in setPER:
            text[i]*=100
        for i in range(11):
            if i>=10:
                self.ui.page1_data2[i].setText(str(round(text[i],3)))
            else:
                self.ui.page1_data2[i].setText(str(int(text[i])))
        
    def star(self):
        page2_data=[]
        for i in range(3):
            page2_data.append([])
            for j in range(7):
                try:
                    num=int(self.ui.page2_data[i][j].text())
                except Exception:
                    num=0
                    pass
                self.ui.page2_data[i][j].setText(str(int(num)))
                page2_data[i].append(num)
        page2_data1=[0,0,0,0]
        for i in range(2):
            page2_data1[i]=self.ui.page2_data1[i].currentIndex()
            try:
                num=int(self.ui.page2_data1[i+2].text())
            except Exception:
                num=0
                pass
            self.ui.page2_data1[i+2]
            page2_data1[i+2]=num
        
        page2_data2=[0,0,0]
        for i in range(7):
            page2_data2[0]+=page2_data[0][i]*11
            page2_data2[0]+=page2_data[1][i]*13
            page2_data2[0]+=page2_data[2][i]*15
            page2_data2[1]+=page2_data[0][i]*(9+i)
            page2_data2[1]+=page2_data[1][i]*(10+i)
            page2_data2[1]+=page2_data[2][i]*(12+i)
        page2_data2[1]+=page2_data[0][6]
        page2_data2[1]+=page2_data[1][6]
        page2_data2[1]+=page2_data[2][6]
        
        if page2_data1[0]==6:
            page2_data2[0]-=page2_data1[2]*2
        if page2_data1[1]==6:
            page2_data2[0]+=page2_data1[3]*2
        
        set_reel=[0,4,5,7,8,9,9]
        page2_data2[1]-=set_reel[page2_data1[0]]*page2_data1[2]
        page2_data2[1]+=set_reel[page2_data1[1]]*page2_data1[3]
        
        data=self.calc(page2_data2[0],0,page2_data2[0],0,page2_data2[0],0,page2_data2[1],0,0,0,0,0)
        total=1
        for i in data:
            total*=i
        self.ui.page2_data2[0].setText("全屬性增加 "+str(page2_data2[0]))
        self.ui.page2_data2[1].setText("攻擊增加 "+str(page2_data2[1]))
        self.ui.page2_data2[2].setText("總增幅 "+str(round((total-1)*100,2))+"%")

    def setlevel(self):
        index=self.ui.level.currentIndex()
        a  =["45" ,"45" ,"57" ,"57" ,"60" ,"60" ,"72" ,"72" ,"87"]
        att=["12%","12%","12%","12%","12%","12%","15%","15%","18%"]
        hp =["900","990","1080","1170","1260","1350","1440","1530","1800"]
        self.ui.page3_data[0].setText("+ "+a[index])
        self.ui.page3_data[1].setText("+ "+hp[index])
        self.ui.page3_data[2].setText("+ "+att[index])

    def StarFire(self):
        page3_data1=[]
        for i in range(7):
            try:
                input=int(float(self.ui.page3_data1[i].text()))
            except Exception:
                input=0
                pass
            page3_data1.append(input)
            self.ui.page3_data1[i].setText(str(input))
        data=self.calc(page3_data1[0],0,page3_data1[1],0,page3_data1[2],0,page3_data1[4],0,page3_data1[5]+page3_data1[6],0,0,page3_data1[3])
        basic=self.calc()
        total=1
        for i in data:
            total*=i
        x=(total-1)/(basic[6]-1)

        self.ui.page3_data1[7].setText("大約= "+str(round(x,2))+" 攻擊")

    def calc(self,s=1,sp=1,d=1,dp=1,l=1,lp=1,att=1,attp=1,dmg=1,strike=1,ignore=1,ap=1):
        sp/=100
        dp/=100
        lp/=100
        attp/=100
        dmg/=100
        strike/=100
        ignore/=100
        ap/=100
        
        data=[0,0,0,0,0,0,0,0,0,0,0,0]
        x=(self.ys+s+self.page0_data[7]*(1+self.page0_data[18]))*(1+self.sp)+self.ns
        data[0]=(4*(x+self.page0_data[5]+self.page0_data[6]))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        x=(self.ys+self.page0_data[7]*(1+self.page0_data[18]))*(1+self.sp+sp)+self.ns
        data[1]=(4*(x+self.page0_data[5]+self.page0_data[6]))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        
        x=(self.yd+d+self.page0_data[8]*(1+self.page0_data[18]))*(1+self.dp)+self.nd
        data[2]=(4*(self.page0_data[4]+x+self.page0_data[6]))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        x=(self.yd+self.page0_data[8]*(1+self.page0_data[18]))*(1+self.dp+dp)+self.nd
        data[3]=(4*(self.page0_data[4]+x+self.page0_data[6]))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        
        x=(self.yl+l+self.page0_data[9]*(1+self.page0_data[18]))*(1+self.lp)+self.nl
        data[4]=(4*(self.page0_data[4]+self.page0_data[5]+x))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        x=(self.yl+self.page0_data[9]*(1+self.page0_data[18]))*(1+self.lp+lp)+self.nl
        data[5]=(4*(self.page0_data[4]+self.page0_data[5]+x))/(4*(self.page0_data[4]+self.page0_data[5]+self.page0_data[6]))
        
        data[6]=(self.att+att)/self.att
        data[7]=(1+self.page0_data[16]+attp)/(1+self.page0_data[16])
        data[8]=(1+self.page0_data[11]+self.page0_data[13]+dmg)/(1+self.page0_data[11]+self.page0_data[13])
        data[9]=(1.35+self.page0_data[15]+strike)/(1.35+self.page0_data[15])
        x=1-(1-self.page0_data[14])*(1-ignore)
        x=1-(self.page0_data[25]*(1-x))
        y=1-(self.page0_data[25]*(1-self.page0_data[14]))
        if x<0:
            data[10]=1
        elif y<0:
            data[10]=101
        else:
            data[10]=x/y
        
        x=(self.ys+self.page0_data[7]*(1+self.page0_data[18]))*(1+self.sp+ap)+self.ns
        y=(self.yd+self.page0_data[8]*(1+self.page0_data[18]))*(1+self.dp+ap)+self.nd
        z=(self.yl+self.page0_data[9]*(1+self.page0_data[18]))*(1+self.lp+ap)+self.nl
        data[11]=(x+y+z)/(self.page0_data[4]+self.page0_data[5]+self.page0_data[6])
        return data
    
    def connection(self):
        address=["home.gamer.com.tw/homeindex.php?owner=leehosen"
                ,"stanleylee417@gmail.com"]
        self.ui.report.setText(address[self.ui.connection.currentIndex()])
    
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())