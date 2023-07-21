###############################################
##                 INTERFACES                ##
###############################################
import pyautogui
import time

screen_width, screen_height = pyautogui.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y)
time.sleep(3)
pyautogui.press("enter")
pyautogui.click()

def insert_cmd(cmd, args=False): 
    if (args):
        pyautogui.typewrite(cmd + " " + args)
    else: 
        pyautogui.typewrite(cmd)
    pyautogui.press("enter")

ip_address = "192.168.0.1"
subnet_mask = "255" 
ipv6 = "2001:acad:db8:100::24/64"
link_local = "FE80::1"

insert_cmd("ip address " + ip_address + " " + "255.255.255." + subnet_mask)
insert_cmd("ipv6 address " + ipv6)
insert_cmd("ipv6 address " + link_local + " link-local")
insert_cmd("description ejemplo_descripcion")
insert_cmd("no shutdown")