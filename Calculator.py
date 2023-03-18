from PyQt5 import QtCore, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        form_w=348
        form_h=412
        Form.setObjectName("self.Form")
        Form.resize(form_w, form_h)
        Form.setWindowTitle("傑諾裝備效益計算機(V1.0) 作者：牡羊")
        
        self.Calculator = QtWidgets.QTabWidget(Form)
        self.Calculator.setGeometry(QtCore.QRect(5, 5, form_w-10, form_h-10))
        self.Calculator.setObjectName("Calculator")
        
        page=[]
        page_name=["UI","數值","星力 / 卷軸","星火","其他"]
        for i in range(len(page_name)):
            page.append(QtWidgets.QWidget())
            page[i].setObjectName("page"+str(i))
            self.Calculator.addTab(page[i], "")
            self.Calculator.setTabText(self.Calculator.indexOf(page[i]),page_name[i])
        
        self.designPage0(page[0])
        self.designPage1(page[1])
        self.designPage2(page[2])
        self.designPage3(page[3])
        self.Description(page[4])
        
        self.Calculator.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def designPage0(self,page):
        label_name=["等級","楓祝前力量","楓祝前敏捷","楓祝前幸運","楓祝後力量","楓祝後敏捷","楓祝後幸運","力量SP","敏捷SP","幸運SP","最高表攻","傷害%","最終傷害%"
                   ,"BOSS傷害%","無視防禦%","爆擊傷害%","攻擊力%","ARC","楓祝%數","角色卡力量","角色卡敏捷","角色卡幸運","極限力量","極限敏捷","極限幸運","怪物防禦%"]
        self.page0_data=[]
        empty=[30,56,56,56,64,64,64,56,56,56,152,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300]
        for i in range(2):
            for j in range(13):
                curIndex=j+i*13
                self.makelabel(page, 15+i*158, 15+j*25, 72, 20,label_name[curIndex])
                
                if curIndex==18:
                    self.page0_data.append(QtWidgets.QComboBox(page))
                    self.page0_data[18].setGeometry(QtCore.QRect(93+1*158, 15+5*25, 67, 20))
                    self.page0_data[18].setObjectName("page0_data30")
                    self.page0_data[18].addItems(["15","16"])
                else:
                    self.page0_data.append(QtWidgets.QLineEdit(page))
                    self.page0_data[curIndex].setGeometry(QtCore.QRect(93+i*158, 15+j*25, 67, 20))
                    self.page0_data[curIndex].setObjectName("page0_data"+str(curIndex))
                    self.page0_data[curIndex].setText(str(empty[curIndex]))
                    #self.page0_data[curIndex].setText(str(curIndex*-1))
        
        
        self.page0_btn=[]
        btn_name=["確定","儲存檔案","選擇檔案"]
        for i in range(3):
            self.page0_btn.append(QtWidgets.QPushButton(page))
            self.page0_btn[i].setGeometry(QtCore.QRect(221-i*105, 342, 98, 25))
            self.page0_btn[i].setObjectName("submit_ui")
            self.page0_btn[i].setText(btn_name[i])
            
    def designPage1(self,page):
        self.page1_btn=[]
        page1_data_type=[QtWidgets.QLineEdit(page),QtWidgets.QComboBox(page)]
        for i in range(2):
            self.page1_btn.append(page1_data_type[i])
            self.page1_btn[i].setObjectName("page1_btn"+str(i))
            
        self.page1_btn[0].setText("1")
        self.page1_btn[0].setGeometry(QtCore.QRect(15,15, 36, 20))
        self.page1_btn[1].addItems(["力量","力量%","敏捷","敏捷%","幸運","幸運%","全屬%","攻擊","攻擊%","總傷%","爆傷%"])
        self.page1_btn[1].setGeometry(QtCore.QRect(54,15, 60, 20))
        
        self.page1_data=[]
        label_name=["攻","%攻","力","%力","%全","敏","%敏","%總","幸","%幸","%爆"]
        for i in range(2):
            self.page1_data.append(QtWidgets.QLineEdit(page))
            self.page1_data[i].setGeometry(QtCore.QRect(117+i*102,15, 99, 20))
            self.page1_data[i].setEnabled(False)
            self.page1_data[i]=QtWidgets.QLabel(page)
            self.page1_data[i].setGeometry(QtCore.QRect(191+i*102,18, 36, 20))
            self.page1_data[i].setText(label_name[i])
            self.page1_data[i].setEnabled(False)
            self.page1_data[i]=QtWidgets.QLabel(page)
            self.page1_data[i].setGeometry(QtCore.QRect(120+i*102,15, 64, 20))
            self.page1_data[i].setObjectName("page1_data"+str(i))
            self.page1_data[i].setText("0")
        
        for i in range(3):
            for j in range(3):
                curIndex=j+i*3+2
                self.page1_data.append(QtWidgets.QLineEdit(page))
                self.page1_data[curIndex].setGeometry(QtCore.QRect(15+j*102,40+i*25, 99, 20))
                self.page1_data[curIndex].setEnabled(False)
                self.page1_data[curIndex]=QtWidgets.QLabel(page)
                self.page1_data[curIndex].setGeometry(QtCore.QRect(89+j*102,43+i*25, 36, 20))
                self.page1_data[curIndex].setText(label_name[curIndex])
                self.page1_data[curIndex].setEnabled(False)
                self.page1_data[curIndex]=QtWidgets.QLabel(page)
                self.page1_data[curIndex].setGeometry(QtCore.QRect(18+j*102,40+i*25, 64, 20))
                self.page1_data[curIndex].setObjectName("page1_data"+str(curIndex))
                self.page1_data[curIndex].setText("0")

        self.page1_data1=[]
        label_name=[["增加"],["力量","力量%","敏捷","敏捷%","幸運","幸運%","攻擊","攻擊%","總傷%","爆傷%","無視%","全屬%"],["0","增幅 0.0%"]]
        for i in range(2):
            for j in range(12):
                curIndex=j+i*12
                self.makelabel(page, 57-i*40, 120+j*21, 36, 18,label_name[i][j*i])
                if i==0:
                    self.page1_data1.append(QtWidgets.QLineEdit(page))
                else:
                    self.page1_data1.append(QtWidgets.QLabel(page))
                self.page1_data1[curIndex].setGeometry(QtCore.QRect(85+i*45, 120+j*21, 40+i*26, 18))
                self.page1_data1[curIndex].setObjectName("page1_data1"+str(curIndex))
                self.page1_data1[curIndex].setText(label_name[2][i])
            
        self.page1_data1.append(QtWidgets.QLabel(page))
        self.page1_data1[24].setGeometry(QtCore.QRect(203, 351, 114, 18))
        self.page1_data1[24].setObjectName("page1_data1")
        self.page1_data1[24].setText("總共 0%")
        
        self.page1_data2=[]
        label_name=["力量","力量%","敏捷","敏捷%","幸運","幸運%","攻擊","攻擊%","總傷%","爆傷%","無視%"]
        for i in range(11):
            label=QtWidgets.QLineEdit(page)
            label.setGeometry(QtCore.QRect(199, 120+i*20, 120, 21))
            label.setEnabled(False)
            self.makelabel(page, 203, 122+i*20, 36, 16,label_name[i])
            
            self.page1_data2.append(QtWidgets.QLabel(page))
            self.page1_data2[i].setGeometry(QtCore.QRect(250, 122+i*20, 67, 16))
            self.page1_data2[i].setObjectName("page1_data2"+str(i))
            self.page1_data2[i].setText("0")
            #self.page1_data2[i].setText(str(i))
                
        for i in self.page1_btn:
            i.setEnabled(False)
        for i in self.page1_data1:
            i.setEnabled(False)

    def designPage2(self,page):
        label_name=["150級裝備","160級裝備","200級裝備"]
        for i in range(3):
            self.makelabel(page, 70+i*86, 15, 86, 12,label_name[i])
        
        for i in range(7):
            self.makelabel(page, 18, 31+i*22, 30, 20,str(i+16)+"星")
        
        self.page2_data=[]
        for i in range(3):
            self.page2_data.append([])
            for j in range(7):
                self.page2_data[i].append(QtWidgets.QLineEdit(page))
                self.page2_data[i][j].setGeometry(QtCore.QRect(60+i*86, 30+j*22, 78, 20))
                self.page2_data[i][j].setObjectName("page2_data"+str(i))
                self.page2_data[i][j].setText("0")
        
        label=[0,0,0,0]
        self.page2_data1=[0,0,0,0]
        label_name=["卷軸","換成"]
        for i in range(2):
            self.makelabel(page, 19, 189+i*22, 30, 20,label_name[i])
            
            self.page2_data1[i]=QtWidgets.QComboBox(page)
            self.page2_data1[i].setGeometry(QtCore.QRect(60, 188+i*22, 78, 20))
            self.page2_data1[i].addItems(["無","極電","RED","X","V","B飾","B防"])
            self.page2_data1[i].setObjectName("page2_data1"+str(i))
            self.page2_data1[i+2]=QtWidgets.QLineEdit(page)
            self.page2_data1[i+2].setGeometry(QtCore.QRect(146, 188+i*22, 78, 20))
            self.page2_data1[i+2].setObjectName("page2_data1"+str(i+2))
            self.page2_data1[i+2].setText("0")
            
            self.makelabel(page, 232, 189+i*22, 15, 20,"張")
                    
        self.page2_btn=[]
        self.page2_btn.append(QtWidgets.QPushButton(page))
        self.page2_btn[0].setGeometry(QtCore.QRect(15, 235, 297, 25))
        self.page2_btn[0].setObjectName("check_btn")
        self.page2_btn[0].setText("確定")
        
        self.page2_data2=[]
        star_improve_name=["全屬性增加 0","攻擊增加 0","總增幅 0.0%"]
        for i in range(3):
            self.page2_data2.append(QtWidgets.QLabel(page))
            self.page2_data2[i].setGeometry(QtCore.QRect(20+i*103, 270, 99, 16))
            self.page2_data2[i].setObjectName("page2_data2"+str(i))
            self.page2_data2[i].setText(star_improve_name[i])
        
        for i in self.page2_data:
            for j in i:
                j.setEnabled(False)
        for i in self.page2_data1:
            i.setEnabled(False)
        for i in self.page2_btn:
            i.setEnabled(False)
    
    def designPage3(self,page):
        self.makelabel(page, 15, 15+25*0, 50, 20,"裝備等級")
            
        self.level=QtWidgets.QComboBox(page)
        self.level.setGeometry(QtCore.QRect(68, 15+25*0, 50, 20))
        self.level.setObjectName("level")
        self.level.addItems(["100","110","120","130","140","150","160","170","200"])
        
        self.page3_data=[]
        label_name=["屬性最高","ＨＰ最高","攻擊最高"]
        data_name=["45","900","12%"]
        for i in range(len(label_name)):
            self.makelabel(page, 15, 40+25*i, 50, 20,label_name[i])
            
            self.page3_data.append(QtWidgets.QLabel(page))
            self.page3_data[i].setGeometry(QtCore.QRect(68, 40+25*i, 48, 20))
            self.page3_data[i].setObjectName("page3_data"+str(i))
            self.page3_data[i].setText("+ "+data_name[i])
        
        self.page3_data1=[]
        label_name=["力量","敏捷","幸運","%全屬","攻擊","總傷","B傷"]
        x=[4,3]
        for i in range(2):
            for j in range(x[i]):
                curIndex=j+i*4
                self.page3_data1.append(QtWidgets.QLineEdit(page))
                self.page3_data1[curIndex].setGeometry(QtCore.QRect(140+90*i, 15+25*j, 48, 20))
                self.page3_data1[curIndex].setObjectName("page3_data"+str(i))
                self.page3_data1[curIndex].setText("0")
                self.page3_data1[curIndex].setEnabled(False)
                
                self.makelabel(page, 191+90*i, 15+25*j, 36, 20,label_name[curIndex])
            
        self.page3_data1.append(QtWidgets.QLabel(page))
        self.page3_data1[7].setGeometry(QtCore.QRect(142+90, 90, 200, 20))
        self.page3_data1[7].setObjectName("page3_data"+str(i))
        self.page3_data1[7].setText("大約= 0 攻擊")

    def Description(self,page):
        label=[]
        label_name=["問題回報"
                   ,""
                   ,"1. BOSS傷害 與 總傷 相同(合併計算)"
                   ,"2. 星火攻擊指武器白值，防具飾品最高皆為3"]
                   
        for i in range(len(label_name)):
            self.makelabel(page, 15, 15+i*25, 303, 20, label_name[i])
        
        self.connection=QtWidgets.QComboBox(page)
        self.connection.setGeometry(QtCore.QRect(68, 15+25*0, 60, 20))
        self.connection.setObjectName("setup_class")
        self.connection.addItems(["巴哈","信箱"])
        
        self.report=QtWidgets.QLineEdit(page)
        self.report.setGeometry(QtCore.QRect(15, 15+25*1, 300, 20))
        self.report.setObjectName("home_data")
        self.report.setText("home.gamer.com.tw/homeindex.php?owner=leehosen")
        
    def makelabel(self,page,x=10,y=10,w=10,h=20,text="",s=True):
        self.label=QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName("label")
        self.label.setText(text)
        self.label.setEnabled(s)