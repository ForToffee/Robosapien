import robo, time

rs=robo.Robo(21)
#rs.send_code(0xB1)
#time.sleep(10)
rs.send_code(0x82)
rs.send_code(0x85)
rs.send_code(0x8A)
rs.send_code(0x8D)
rs.send_code(0x86)
time.sleep(10)
rs.send_code(0x8E)


print "fin"
