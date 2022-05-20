import os 

base_dir = os.getcwd()
python = 'D:\pythonProject\fsafe-venv\python3.7\Scripts\python.exe'
tools = {
'渗透测试':{
        '打开渗透测试目录':
        ['pentest_btn', " 'start {}\gui_pentest\' ".format(base_dir)],

        '打开Powershell':
        ['p1_btn', " \"start powershell -NoExit cd {}\gui_pentest\ \" ".format(base_dir)],

        'Godzilla v4.0':
        ['God_btn', "'cd gui_pentest/Godzilla && ' + java8_path + ' -jar ' + 'Godzilla.jar'"],
        
        '冰蝎 T00ls 专版v3.0 Beta 11':
        ['Beh_btn', "'cd gui_pentest/Behinder T00l专版 && ' + java8_path + ' -jar ' + 'Behinder.jar'"],
        
        '冰蝎魔改版 v3.3.2':
        ['BehMod_btn'," 'cd gui_pentest/Behinder-Mode && ' + java8_path + ' -jar ' + 'Behinder-Mode.jar' "],
        
        '天蝎权限管理工具':
        ['Tianxie_btn'," 'cd gui_pentest/TianXie && ' + java8_path + ' -jar ' + '天蝎权限管理工具.jar' "],
        
        'BurpSuite_pro v2022.3 ':
        ['Burp_btn',"'cd gui_other/BurpSuite_Pro && ' + java9_path + ' -javaagent:BurpSuiteLoader_v2022.3.jar -noverify -jar burpsuite_pro_v2022.3.jar'"],
        
        'CobaltStrike v4.4':
        ['Cob_btn',"'cd gui_other/CobaltStrike/Cobalt_Strike_4.4 && ' + java8_path + ' -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Xms512M -Xmx1024M -Dfile.encoding=UTF-8 -javaagent:CobaltStrikeCN.jar -jar cobaltstrike.jar $*'"]
},
'信息收集':{
        '打开信息收集目录':
        ['info_btn', " 'start {}\gui_shouji\' ".format(base_dir)],

        '打开Powershell':
        ['p2_btn', " \"start powershell -NoExit cd {}\gui_shouji\ \" ".format(base_dir)],

        '御剑扫描珍藏版 v1.1':
        ['Yuj_btn',"'cd gui_shouji/yjdirscanv1.1 && 御剑目录扫描专业版v1.1.exe'"],

        'Dirscan v3.0':
        ['Dir_btn',"'cd gui_shouji/dirscan_3.0 && ' + java9_path + ' -jar ' + 'scandir-3.0.jar'"],

        'WebFinder v3.2':
        ['WebF_btn',"'cd gui_shouji && ' + java8_path + ' -jar ' + 'webfinder-3.2.jar'"],

        'Fofa_viewer v1.8':
        ['Fofa_btn',"'cd gui_shouji/fofaviewer && ' + java8_path + ' -jar ' + 'fofaviewer.jar'"],
        
        'Sqlmap':
        ['Sqlm_btn',"'start cmd /k \"cd gui_shouji/sqlmap\" '"],

        'Oneforall':
        ['Onef_btn',"'start cmd /k \"cd gui_shouji/oneforall\" '"],

        'JsFinder':
        ['JsF_btn',"'start cmd /k \"cd gui_shouji/jsfinder\" '"],

        'PackerFuzzer v1.3':
        ['Pac_btn',"' start cmd /k \"cd gui_shouji/Packer-Fuzzer-1.3\" '"],


},              
'漏洞利用':{
        '打开漏洞利用目录':
        ['scan_btn', " 'start {}\gui_scan\' ".format(base_dir)],

        '打开Powershell':
        ['p3_btn', " ' start powershell -NoExit cd {}\gui_scan\ ' ".format(base_dir)],

        '403bypasser':
        ['bypass403_btn'," 'start cmd /k \" cd gui_scan/403bypasser \" ' "],

        '通达OA综合利用工具 v1.0':
        ['ToDa_btn',"'cd gui_scan && ' + java8_path + ' -jar ' + 'TODA.jar'"],

        'Gr33k漏洞利用工具集':
        ['Gr3_btn'," '{python} gui_scan/Gr33k/Gr33k.py ' ".format(python=python)],

        'Cas反序列化利用工具v1.1':
        ['Cas_btn'," ' cd gui_scan && ' + java8_path + ' -jar ' + 'CAS_cc2_Exploit-1.0-SNAPSHOTv1.1-all.jar' "],
        
        '神机 v1.9':
        ['Sj_btn',"  ' cd gui_scan && ' + java8_path + ' -jar ' + 'SJ-V1.9.jar' "],

        'ThinkPHP综合利用工具 v2.3':
        ['Thp_btn'," ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkPHP.V2.3.by.jar' "],

        'ThinkPhp漏洞利用工具 v1.2':
        ['ThpLog_btn'," ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkphpGUI-1.2-SNAPSHOT.jar' "],
        
        'ThinkPhp命令执行检测工具':
        ['ThpRce_btn'," 'cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'thinkphp命令执行检测工具.jar' "],
        
        'Weblogic-framework v0.2.3':
        ['Webl_btn'," ' cd gui_scan/weblogic/weblogic-framework-0.2.3 && ' + java8_path + ' -jar ' + 'weblogic-framework-0.2.3-all-jar-with-dependencies.jar' "],
        
        'Weblogic-Exp-Snapshot-all v1.0':
        ['Webe_btn'," ' cd gui_scan/weblogic && ' + java8_path + ' -jar ' + 'weblogic_exploit-1.0-SNAPSHOT-all.jar' "],
        
        '深X服edr任意用户登陆检测工具':
        ['Edr_btn'," ' cd gui_scan && ' + java8_path + ' -jar ' + '深X服edr任意用户登陆检测工具.jar' "],
        
        'Shiro-exp_v2.51_by飞鸿':
        ['Shiro1_btn'," ' cd gui_scan/shiro/ShiroExploit.V2.51 && ' + java8_path + ' -jar ' + 'ShiroExploit-v2.51.jar' "],
        
        'ShiroScan反序列化回显工具v1.1_fupinglee':
        ['Shiro2_btn'," ' cd gui_scan/shiro && ' + java8_path + ' -jar ' + 'ShiroScan-1.1.jar' "],
        
        'Shiro attack v2.2_j1anFen':
        ['Shiro3_btn'," 'cd gui_scan/shiro/shiro_attack_2.2 && ' + java8_path + ' -jar ' + 'shiro_attack-2.2.jar' "],
        
        'Spring 漏洞利用工具v1.3':
        ['Sprboot_btn', " 'cd gui_scan/Spring/SpringBootExploit-1.3-SNAPSHOT-all && ' + java8_path + ' -jar ' + 'SpringBootExploit-1.3-SNAPSHOT-all.jar' "],

        'Log4j':
        ['Log4j2_btn', " 'cd gui_scan/Log4j/ && ' + java8_path + ' -jar ' + 'woodpecker-framework.1.3.3.jar' "],

        'OracleShellv1.0':
        ['Oracle_btn'," ' cd gui_scan && ' + java8_path + ' -jar ' + 'oracleShell.jar' "],
        
        'Tomcat弱密码检查':
        ['TomcatP_btn'," ' cd gui_scan/tomcat && ' + java8_path + ' -jar ' + 'tomcat.jar' "],
        
        'FastJson反序列化检查工具':
        ['FastJ_btn'," ' cd gui_scan/json && json反序列化检查工具.exe ' "],
        
        'Aliyun_AKTools_by_T00ls':
        ['Alit_btn'," 'cd gui_scan/AliyunAkTools && AliyunAkTools.exe' "],
        
        'MDUT数据库利用工具':
        ['Mdut_btn'," ' cd gui_scan/Multiple.Database.Utilization.Tools.-.v2.0.6 && ' + java8_path + ' -jar ' + 'MDUT.jar' "],

},
}
# themes_list = ['superhero','purse','yeti','lumen','journal']
themes = 'superhero'
line_count = 4
width = 1400
height = 700
button_width = 25

import os
import platform
#获取当前绝对路径
tools_path = os.getcwd()
if platform.system() == 'Windows' :
    java8_path = (tools_path + "\Java_path\jre_1.8_win\\bin\java").replace('\\','\\\\')
    java9_path = (tools_path + "\Java_path\java9_win\\bin\java").replace('\\','\\\\')
else:
    #MacOS和Linux的java绝对路径
    java8_path = tools_path + "/Java_path/java_1.8/bin/java"
    java9_path = tools_path + "/Java_path/java9/bin/java"