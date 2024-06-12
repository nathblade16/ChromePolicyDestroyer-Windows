import winreg as wrg
print("chrome policy destroyer for windows")
print("WARNING, THIS SOFTWARE IS BOTH UNTESTED AND COMES WITH NO WARRENTY, WE TAKE NO RESPONSIBILITY FOR ANYTHING BAD HAPPENING AS A RESULT OF USING THIS SOFTWARE")
choice = input("Would you still like to run it?")
def set_reg(name, value):
  location = wrg.HKEY_LOCAL_MACHINE
  chrome = wrg.OpenKey(location, "Software\\Policies\\Google\\Chrome\\ExtensionInstallAllowlist") 
  wrg.SetValueEx(chrome, name, 0, wrg.REG_SZ, value) 
def destroy():
  print("work in progress")
if(choice[0].lower() = "y"):
  destroy()
  
