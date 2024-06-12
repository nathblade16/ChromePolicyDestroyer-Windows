import winreg as wrg
import json
print("chrome policy destroyer for windows by nathblade16")
print("WARNING, THIS SOFTWARE IS BOTH UNTESTED AND COMES WITH NO WARRENTY, I TAKE NO RESPONSIBILITY FOR ANY DAMAGES AS A RESULT OF USING THIS SOFTWARE")
choice = input("Would you still like to run it?")
def set_reg(name, value):
  location = wrg.HKEY_LOCAL_MACHINE
  chrome = wrg.OpenKey(location, "Software\\Policies\\Google\\Chrome\\ExtensionInstallAllowlist") 
  wrg.SetValueEx(chrome, name, 0, wrg.REG_SZ, value)
def destroy():
  try:
    file = open("managed_policies.json", "r")
  except:
    raise ValueError("policies file missing, did you download the all the files?")
  try:
    policies = file.read()
  except:
    raise ValueError("policies file missing, did you download the all the files?")
  decoded_policies = json.loads(policies)
  for key, value in decoded_policies.items():
    set_reg(key, value)
if(choice[0].lower() = "y"):
  destroy()
  
