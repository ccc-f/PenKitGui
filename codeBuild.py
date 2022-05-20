from setting import tools,line_count,themes,width,button_width,height

def gen_click():
    with open('penkit.py','w',encoding='utf-8')as f:
        f.write("""
import subprocess
from setting import java8_path
from setting import java9_path
class PenKit():
        """
        )
        for t in tools.values():
            for btn in t.values():
                f.write("""
    def {func}():
        subprocess.Popen( {cmd} , shell=True)
                """.format(func=btn[0],cmd=btn[1]))

def gen_body():
    i = 0
    with open('penkitgui.py','w',encoding='utf-8')as f:
        f.write("""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from penkit import PenKit

root = ttk.Window(
                title="【综合化图形化渗透工具】by Scb0y",
                themename="{themes}",
                size=({width}, {height}),
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
        """.format(themes=themes,width=width,height=height))
        for title,tool in tools.items():
            f.write("""
#################### {title} ####################
f_{number} = ttk.Frame(pk)
            """.format(title=title,number=i))
            col = 0
            row = 1
            for tool_name,tool_info in tool.items():
                col += 1
                if col % (line_count+1) == 0:
                    col = 1
                    row += 1
                f.write("""
ttk.Button(f_{number},text="{tool}", bootstyle=(PRIMARY, "success-outline-toolbutton"),
            width={button_width}, command=PenKit.{tool_btn}).grid(row={row},column={col},padx=20,pady=10)
                """.format(number=i,tool=tool_name,button_width=button_width,tool_btn=tool_info[0],row=row,col=col))
            f.write("""
pk.add(f_{number}, text='     {title}    ')
            """.format(number=i,title=title))
            i += 1
        f.write("""
root.mainloop()
        """)    
if __name__ == "__main__":
    gen_click()
    gen_body()