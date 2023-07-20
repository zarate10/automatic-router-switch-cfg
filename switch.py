###############################################
##                  SWITCH                   ##
###############################################
import pyautogui
import time

screen_width, screen_height = pyautogui.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y)

hostname = ""
default_gateway = "" # ip de la interfaz a la que está conectado el switch. 
vlan_ip = "" # si no lo especifica, es 1 menos que la default gateway.
submask = ""
exec_privilegiado_pass = ""
console_password = "" # line console 0 password
dominio_ssh = "" # CCNA-lab.com generalmente
bits_ssh = "" # 1024 generalmente
user_privilegio = "admin 15 2" # "<username> <privilegio> <pass>"
block = "180 4 120" # block <cantidad_tiempo> cuando <cantidad_intentos> en tantos <segundos>

pyautogui.moveTo(center_x, center_y)
time.sleep(4)
pyautogui.press("enter")
pyautogui.click()

def insert_cmd(cmd, args=False): 
    if (args):
        pyautogui.typewrite(cmd + " " + args)
    else: 
        pyautogui.typewrite(cmd)
    pyautogui.press("enter")

insert_cmd("en")
insert_cmd("conf term")
insert_cmd("hostname", hostname)
insert_cmd("ip default-gateway", default_gateway)
insert_cmd("no ip domain-lookup")
insert_cmd("banner motd", "# Acceso no autorizado para personas no autorizadas, tenga en cuenta que le caera todo el peso de la ley. #")
insert_cmd("enable secret", exec_privilegiado_pass)
insert_cmd("service password-encryption")
insert_cmd("interface vlan 1")
insert_cmd("ip address", (vlan_ip + " " + submask))
insert_cmd("no shutdown")
insert_cmd("exit")
insert_cmd("line console 0")
insert_cmd("password", console_password)
insert_cmd("login")
insert_cmd("exec-timeout 5 0")
insert_cmd("exit")
insert_cmd("ip domain-name", dominio_ssh)
insert_cmd("crypto key generate rsa general-keys modulus", bits_ssh)
insert_cmd("line vty 0")
insert_cmd("login local")
insert_cmd("exit")
insert_cmd("line vty 0 15")
insert_cmd("exec-timeout 5 0")
insert_cmd("transport input ssh")
insert_cmd("exit")
insert_cmd(("username " 
            + user_privilegio.split(" ")[0] 
            + " privilege "
            + user_privilegio.split(" ")[1] 
            + " secret "
            + user_privilegio.split(" ")[2]
            ))
insert_cmd("line vty 0 15")
insert_cmd("exec-timeout 5 0")
insert_cmd("end")
insert_cmd("copy running-config startup-config")