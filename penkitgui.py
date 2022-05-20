
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
            width=25, command=PenKit.pentest_btn).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_0,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.p1_btn).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_0,text="Godzilla v4.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.God_btn).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_0,text="冰蝎 T00ls 专版v3.0 Beta 11", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Beh_btn).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_0,text="冰蝎魔改版 v3.3.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.BehMod_btn).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_0,text="天蝎权限管理工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Tianxie_btn).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_0,text="BurpSuite_pro v2022.3 ", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Burp_btn).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_0,text="CobaltStrike v4.4", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Cob_btn).grid(row=2,column=4,padx=20,pady=10)
                
pk.add(f_0, text='     渗透测试    ')
            
#################### 信息收集 ####################
f_1 = ttk.Frame(pk)
            
ttk.Button(f_1,text="打开信息收集目录", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.info_btn).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.p2_btn).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_1,text="御剑扫描珍藏版 v1.1", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Yuj_btn).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_1,text="Dirscan v3.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Dir_btn).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_1,text="WebFinder v3.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.WebF_btn).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="Fofa_viewer v1.8", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Fofa_btn).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_1,text="Sqlmap", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Sqlm_btn).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_1,text="Oneforall", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Onef_btn).grid(row=2,column=4,padx=20,pady=10)
                
ttk.Button(f_1,text="JsFinder", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.JsF_btn).grid(row=3,column=1,padx=20,pady=10)
                
ttk.Button(f_1,text="PackerFuzzer v1.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Pac_btn).grid(row=3,column=2,padx=20,pady=10)
                
pk.add(f_1, text='     信息收集    ')
            
#################### 漏洞利用 ####################
f_2 = ttk.Frame(pk)
            
ttk.Button(f_2,text="打开漏洞利用目录", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.scan_btn).grid(row=1,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="打开Powershell", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.p3_btn).grid(row=1,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="403bypasser", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.bypass403_btn).grid(row=1,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="通达OA综合利用工具 v1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.ToDa_btn).grid(row=1,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Cas反序列化利用工具v1.1", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Cas_btn).grid(row=2,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="神机 v1.9", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Sj_btn).grid(row=2,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPHP综合利用工具 v2.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Thp_btn).grid(row=2,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPhp漏洞利用工具 v1.2", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.ThpLog_btn).grid(row=2,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="ThinkPhp命令执行检测工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.ThpRce_btn).grid(row=3,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="Weblogic-framework v0.2.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Webl_btn).grid(row=3,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Weblogic-Exp-Snapshot-all v1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Webe_btn).grid(row=3,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="深X服edr任意用户登陆检测工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Edr_btn).grid(row=3,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Shiro-exp_v2.51_by飞鸿", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Shiro1_btn).grid(row=4,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="ShiroScan反序列化回显工具v1.1_fupinglee", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Shiro2_btn).grid(row=4,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Shiro attack v2.2_j1anFen", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Shiro3_btn).grid(row=4,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="Spring 漏洞利用工具v1.3", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Sprboot_btn).grid(row=4,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Log4j", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Log4j2_btn).grid(row=5,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="OracleShellv1.0", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Oracle_btn).grid(row=5,column=2,padx=20,pady=10)
                
ttk.Button(f_2,text="Tomcat弱密码检查", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.TomcatP_btn).grid(row=5,column=3,padx=20,pady=10)
                
ttk.Button(f_2,text="FastJson反序列化检查工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.FastJ_btn).grid(row=5,column=4,padx=20,pady=10)
                
ttk.Button(f_2,text="Aliyun_AKTools_by_T00ls", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Alit_btn).grid(row=6,column=1,padx=20,pady=10)
                
ttk.Button(f_2,text="MDUT数据库利用工具", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width=25, command=PenKit.Mdut_btn).grid(row=6,column=2,padx=20,pady=10)
                
pk.add(f_2, text='     漏洞利用    ')
            
root.mainloop()
        