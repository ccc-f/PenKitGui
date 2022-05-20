set ws=WScript.CreateObject("WScript.Shell")
currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
GUI_Tools = currentpath & "\penkitgui.bat"
ws.Run GUI_Tools,0