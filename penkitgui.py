
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from penkit import PenKit

root = ttk.Window(
                title="【综合化图形化渗透工具】by Scb0y",
                themename="superhero",
                size=(1400, 700),
                resizable=(True, True),
                )
f = ttk.Frame(root)
f.pack(pady=5, fill=X, side=TOP)
pk = ttk.Notebook(f)
pk.pack(
    side=LEFT,
    padx=(10, 0),
    expand=YES,
    fill=BOTH
)
        
#################### 渗透测试 ####################
f_0 = ttk.Frame(pk)
            
ttk.Button(f_0,text="打开渗透测试目录", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_1).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_0,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_2).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_0,text="Godzilla v4.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_3).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_0,text="冰蝎 T00ls 专版v3.0 Beta 11", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_4).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_0,text="冰蝎魔改版 v3.3.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_5).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_0,text="天蝎权限管理工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_6).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_0,text="BurpSuite_pro v2022.3 ", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_7).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_0,text="CobaltStrike v4.4", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_8).grid(row=2,column=4,padx=20,pady=10)
                
pk.add(f_0, text='     渗透测试    ')
            
#################### 信息收集 ####################
f_1 = ttk.Frame(pk)
            
ttk.Button(f_1,text="打开信息收集目录", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_9).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_10).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_1,text="御剑扫描珍藏版 v1.1", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_11).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_1,text="Dirscan v3.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_12).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_1,text="WebFinder v3.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_13).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="Fofa_viewer v1.8", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_14).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_1,text="Sqlmap", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_15).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_1,text="Oneforall", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_16).grid(row=2,column=4,padx=20,pady=10)
                
ttk.Button(f_1,text="JsFinder", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_17).grid(row=3,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="PackerFuzzer v1.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_18).grid(row=3,column=2,padx=20,pady=10)
                
pk.add(f_1, text='     信息收集    ')
            
#################### 漏洞利用 ####################
f_2 = ttk.Frame(pk)
            
ttk.Button(f_2,text="打开漏洞利用目录", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_19).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_20).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="403bypasser", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_21).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="通达OA综合利用工具 v1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_22).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Cas反序列化利用工具v1.1", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_23).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="神机 v1.9", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_24).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPHP综合利用工具 v2.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_25).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPhp漏洞利用工具 v1.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_26).grid(row=2,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPhp命令执行检测工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_27).grid(row=3,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="Weblogic-framework v0.2.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_28).grid(row=3,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Weblogic-Exp-Snapshot-all v1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_29).grid(row=3,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="深X服edr任意用户登陆检测工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_30).grid(row=3,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Shiro-exp_v2.51_by飞鸿", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_31).grid(row=4,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="ShiroScan反序列化回显工具v1.1_fupinglee", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_32).grid(row=4,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Shiro attack v2.2_j1anFen", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_33).grid(row=4,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="Spring 漏洞利用工具v1.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_34).grid(row=4,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Log4j", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_35).grid(row=5,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="OracleShellv1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_36).grid(row=5,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Tomcat弱密码检查", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_37).grid(row=5,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="FastJson反序列化检查工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_38).grid(row=5,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Aliyun_AKTools_by_T00ls", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_39).grid(row=6,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="MDUT数据库利用工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.btn_40).grid(row=6,column=2,padx=20,pady=10)
                
pk.add(f_2, text='     漏洞利用    ')
            
root.mainloop()
        