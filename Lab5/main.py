import Registration as reg
import DesktopReg as dr
import WebReg as wr
import QuickReg as qr

registration = reg.Registration("1", "22.10.2021", "Abraham Lincoln", "387-835-6447")
desktopReg = dr.DesktopReg("2", "22.10.2021", "Jason Statham", "+1-289-524-4535", "Vin Diesel")
webReg = wr.WebReg("3", "23.10.2021", "Paul Walker", "+1-289-524-4535", "Google Chrome", "31.223.56.122")
quickReg = qr.QuickReg("", "", "Johnny Silverhand", "1-958-943-2355")

registration.print_info()
desktopReg.print_info()
webReg.print_info()
quickReg.print_info()
