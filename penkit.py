
import subprocess
from setting import java8_path
from setting import java9_path
class PenKit():
        
    def btn_1():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_pentest'  , shell=True)
                
    def btn_2():
        subprocess.Popen(  "start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_pentest\ "  , shell=True)
                
    def btn_3():
        subprocess.Popen( 'cd gui_pentest/Godzilla && ' + java8_path + ' -jar ' + 'Godzilla.jar' , shell=True)
                
    def btn_4():
        subprocess.Popen(  'cd gui_pentest/Behinder T00l专版 && ' + java8_path + ' -jar ' + 'Behinder.jar'  , shell=True)
                
    def btn_5():
        subprocess.Popen(  'cd gui_pentest/Behinder-Mode && ' + java8_path + ' -jar ' + 'Behinder-Mode.jar'  , shell=True)
                
    def btn_6():
        subprocess.Popen(  'cd gui_pentest/TianXie && ' + java8_path + ' -jar ' + '天蝎权限管理工具.jar'  , shell=True)
                
    def btn_7():
        subprocess.Popen( 'cd gui_pentest/BurpSuite_Pro && ' + java9_path + ' -javaagent:BurpSuiteLoader_v2022.3.jar -noverify -jar burpsuite_pro_v2022.3.jar' , shell=True)
                
    def btn_8():
        subprocess.Popen( 'cd gui_pentest/CobaltStrike/Cobalt_Strike_4.4 && ' + java8_path + ' -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Xms512M -Xmx1024M -Dfile.encoding=UTF-8 -javaagent:CobaltStrikeCN.jar -jar cobaltstrike.jar $*' , shell=True)
                
    def btn_9():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_shouji'  , shell=True)
                
    def btn_10():
        subprocess.Popen(  "start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_shouji\ "  , shell=True)
                
    def btn_11():
        subprocess.Popen( 'cd gui_shouji/yjdirscanv1.1 && 御剑目录扫描专业版v1.1.exe' , shell=True)
                
    def btn_12():
        subprocess.Popen( 'cd gui_shouji/dirscan_3.0 && ' + java9_path + ' -jar ' + 'scandir-3.0.jar' , shell=True)
                
    def btn_13():
        subprocess.Popen( 'cd gui_shouji && ' + java8_path + ' -jar ' + 'webfinder-3.2.jar' , shell=True)
                
    def btn_14():
        subprocess.Popen( 'cd gui_shouji/fofaviewer && ' + java8_path + ' -jar ' + 'fofaviewer.jar' , shell=True)
                
    def btn_15():
        subprocess.Popen(  'start cmd /k "cd gui_shouji/sqlmap" '  , shell=True)
                
    def btn_16():
        subprocess.Popen( 'start cmd /k "cd gui_shouji/jsfinder" ' , shell=True)
                
    def btn_17():
        subprocess.Popen( ' start cmd /k "cd gui_shouji/Packer-Fuzzer-1.3" ' , shell=True)
                
    def btn_18():
        subprocess.Popen(  'start D:\pythonProject\PenKitGui\gui_scan'  , shell=True)
                
    def btn_19():
        subprocess.Popen(  ' start powershell -NoExit cd D:\pythonProject\PenKitGui\gui_scan\ '  , shell=True)
                
    def btn_20():
        subprocess.Popen(  'start cmd /k " cd gui_scan/403bypasser " '  , shell=True)
                
    def btn_21():
        subprocess.Popen( 'cd gui_scan && ' + java8_path + ' -jar ' + 'TODA.jar' , shell=True)
                
    def btn_22():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + 'CAS_cc2_Exploit-1.0-SNAPSHOTv1.1-all.jar'  , shell=True)
                
    def btn_23():
        subprocess.Popen(   ' cd gui_scan && ' + java8_path + ' -jar ' + 'SJ-V1.9.jar'  , shell=True)
                
    def btn_24():
        subprocess.Popen(  ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkPHP.V2.3.by.jar'  , shell=True)
                
    def btn_25():
        subprocess.Popen(  ' cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'ThinkphpGUI-1.2-SNAPSHOT.jar'  , shell=True)
                
    def btn_26():
        subprocess.Popen(  'cd gui_scan/thinkphp && ' + java8_path + ' -jar ' + 'thinkphp命令执行检测工具.jar'  , shell=True)
                
    def btn_27():
        subprocess.Popen(  ' cd gui_scan/weblogic/weblogic-framework-0.2.3 && ' + java8_path + ' -jar ' + 'weblogic-framework-0.2.3-all-jar-with-dependencies.jar'  , shell=True)
                
    def btn_28():
        subprocess.Popen(  ' cd gui_scan/weblogic && ' + java8_path + ' -jar ' + 'weblogic_exploit-1.0-SNAPSHOT-all.jar'  , shell=True)
                
    def btn_29():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + '深X服edr任意用户登陆检测工具.jar'  , shell=True)
                
    def btn_30():
        subprocess.Popen(  ' cd gui_scan/shiro/ShiroExploit.V2.51 && ' + java8_path + ' -jar ' + 'ShiroExploit.jar'  , shell=True)
                
    def btn_31():
        subprocess.Popen(  ' cd gui_scan/shiro && ' + java8_path + ' -jar ' + 'ShiroScan-1.1.jar'  , shell=True)
                
    def btn_32():
        subprocess.Popen(  'cd gui_scan/shiro/shiro_attack_2.2 && ' + java8_path + ' -jar ' + 'shiro_attack-2.2.jar'  , shell=True)
                
    def btn_33():
        subprocess.Popen(  'cd gui_scan/Spring/SpringBootExploit-1.3-SNAPSHOT-all && ' + java8_path + ' -jar ' + 'SpringBootExploit-1.3-SNAPSHOT-all.jar'  , shell=True)
                
    def btn_34():
        subprocess.Popen(  'cd gui_scan/Log4j/ && ' + java8_path + ' -jar ' + 'woodpecker-framework.1.3.3.jar'  , shell=True)
                
    def btn_35():
        subprocess.Popen(  ' cd gui_scan && ' + java8_path + ' -jar ' + 'oracleShell.jar'  , shell=True)
                
    def btn_36():
        subprocess.Popen(  ' cd gui_scan/tomcat && ' + java8_path + ' -jar ' + 'tomcat.jar'  , shell=True)
                
    def btn_37():
        subprocess.Popen(  ' cd gui_scan/json && json反序列化检查工具.exe '  , shell=True)
                
    def btn_38():
        subprocess.Popen(  'cd gui_scan/AliyunAkTools && AliyunAkTools.exe'  , shell=True)
                
    def btn_39():
        subprocess.Popen(  ' cd gui_scan/Multiple.Database.Utilization.Tools.-.v2.0.6 && ' + java8_path + ' -jar ' + 'MDUT.jar'  , shell=True)
                