
import subprocess
from setting import java8_path
from setting import java9_path
class PenKit():
        
    def pentest_btn():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_pentest'  , shell=True)
                
    def p1_btn():
        subprocess.Popen(  "start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_pentest\ "  , shell=True)
                
    def God_btn():
        subprocess.Popen( 'cd gui_pentest/Godzilla && ' + java8_path + ' -jar ' + 'Godzilla.jar' , shell=True)
                
    def Beh_btn():
        subprocess.Popen(  'cd gui_pentest/Behinder T00l专版 && ' + java8_path + ' -jar ' + 'Behinder.jar'  , shell=True)
                
    def BehMod_btn():
        subprocess.Popen(  'cd gui_pentest/Behinder-Mode && ' + java8_path + ' -jar ' + 'Behinder-Mode.jar'  , shell=True)
                
    def Tianxie_btn():
        subprocess.Popen(  'cd gui_pentest/TianXie && ' + java8_path + ' -jar ' + '天蝎权限管理工具.jar'  , shell=True)
                
    def Burp_btn():
        subprocess.Popen( 'cd gui_pentest/BurpSuite_Pro && ' + java9_path + ' -javaagent:BurpSuiteLoader_v2022.3.jar -noverify -jar burpsuite_pro_v2022.3.jar' , shell=True)
                
    def Cob_btn():
        subprocess.Popen( 'cd gui_pentest/CobaltStrike/Cobalt_Strike_4.4 && ' + java8_path + ' -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Xms512M -Xmx1024M -Dfile.encoding=UTF-8 -javaagent:CobaltStrikeCN.jar -jar cobaltstrike.jar $*' , shell=True)
                
    def info_btn():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_shouji'  , shell=True)
                
    def p2_btn():
        subprocess.Popen(  "start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_shouji\ "  , shell=True)
                
    def Yuj_btn():
        subprocess.Popen( 'cd gui_shouji/yjdirscanv1.1 && 御剑目录扫描专业版v1.1.exe' , shell=True)
                
    def Dir_btn():
        subprocess.Popen( 'cd gui_shouji/dirscan_3.0 && ' + java9_path + ' -jar ' + 'scandir-3.0.jar' , shell=True)
                
    def WebF_btn():
        subprocess.Popen( 'cd gui_shouji && ' + java8_path + ' -jar ' + 'webfinder-3.2.jar' , shell=True)
                
    def Fofa_btn():
        subprocess.Popen( 'cd gui_shouji/fofaviewer && ' + java8_path + ' -jar ' + 'fofaviewer.jar' , shell=True)
                
    def Sqlm_btn():
        subprocess.Popen(  'start cmd /k "cd gui_shouji/sqlmap" '  , shell=True)
                
    def Onef_btn():
        subprocess.Popen( 'start cmd /k "cd gui_shouji/oneforall" ' , shell=True)
                
    def JsF_btn():
        subprocess.Popen( 'start cmd /k "cd gui_shouji/jsfinder" ' , shell=True)
                
    def Pac_btn():
        subprocess.Popen( ' start cmd /k "cd gui_shouji/Packer-Fuzzer-1.3" ' , shell=True)
                
    def scan_btn():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_scan'  , shell=True)
                
    def p3_btn():
        subprocess.Popen(  ' start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_scan\ '  , shell=True)
                
    def bypass403_btn():
        subprocess.Popen(  'start cmd /k " cd gui_scan/403bypasser " '  , shell=True)
                
    def ToDa_btn():
        subprocess.Popen( 'cd gui_scan && ' + java8_path + ' -jar ' + 'TODA.jar' , shell=True)
                
    def Cas_btn():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + 'CAS_cc2_Exploit-1.0-SNAPSHOTv1.1-all.jar'  , shell=True)
                
    def Sj_btn():
        subprocess.Popen(   ' cd gui_scan && ' + java8_path + ' -jar ' + 'SJ-V1.9.jar'  , shell=True)
                
    def Thp_btn():
        subprocess.Popen(  ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkPHP.V2.3.by.jar'  , shell=True)
                
    def ThpLog_btn():
        subprocess.Popen(  ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkphpGUI-1.2-SNAPSHOT.jar'  , shell=True)
                
    def ThpRce_btn():
        subprocess.Popen(  'cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'thinkphp命令执行检测工具.jar'  , shell=True)
                
    def Webl_btn():
        subprocess.Popen(  ' cd gui_scan/weblogic/weblogic-framework-0.2.3 && ' + java8_path + ' -jar ' + 'weblogic-framework-0.2.3-all-jar-with-dependencies.jar'  , shell=True)
                
    def Webe_btn():
        subprocess.Popen(  ' cd gui_scan/weblogic && ' + java8_path + ' -jar ' + 'weblogic_exploit-1.0-SNAPSHOT-all.jar'  , shell=True)
                
    def Edr_btn():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + '深X服edr任意用户登陆检测工具.jar'  , shell=True)
                
    def Shiro1_btn():
        subprocess.Popen(  ' cd gui_scan/shiro/ShiroExploit.V2.51 && ' + java8_path + ' -jar ' + 'ShiroExploit-v2.51.jar'  , shell=True)
                
    def Shiro2_btn():
        subprocess.Popen(  ' cd gui_scan/shiro && ' + java8_path + ' -jar ' + 'ShiroScan-1.1.jar'  , shell=True)
                
    def Shiro3_btn():
        subprocess.Popen(  'cd gui_scan/shiro/shiro_attack_2.2 && ' + java8_path + ' -jar ' + 'shiro_attack-2.2.jar'  , shell=True)
                
    def Sprboot_btn():
        subprocess.Popen(  'cd gui_scan/Spring/SpringBootExploit-1.3-SNAPSHOT-all && ' + java8_path + ' -jar ' + 'SpringBootExploit-1.3-SNAPSHOT-all.jar'  , shell=True)
                
    def Log4j2_btn():
        subprocess.Popen(  'cd gui_scan/Log4j/ && ' + java8_path + ' -jar ' + 'woodpecker-framework.1.3.3.jar'  , shell=True)
                
    def Oracle_btn():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + 'oracleShell.jar'  , shell=True)
                
    def TomcatP_btn():
        subprocess.Popen(  ' cd gui_scan/tomcat && ' + java8_path + ' -jar ' + 'tomcat.jar'  , shell=True)
                
    def FastJ_btn():
        subprocess.Popen(  ' cd gui_scan/json && json反序列化检查工具.exe '  , shell=True)
                
    def Alit_btn():
        subprocess.Popen(  'cd gui_scan/AliyunAkTools && AliyunAkTools.exe'  , shell=True)
                
    def Mdut_btn():
        subprocess.Popen(  ' cd gui_scan/Multiple.Database.Utilization.Tools.-.v2.0.6 && ' + java8_path + ' -jar ' + 'MDUT.jar'  , shell=True)
                