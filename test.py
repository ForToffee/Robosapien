# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien

# command codes from http://www.aibohack.com/robosap/ir_codes.htm
import robo

rs=robo.Robo(21)	#create Robo object for GPIO 21
rs.send_code(0xB1)	#Issue reset command
raw_input('Enter')
rs.send_code(0x81)	#Right arm up
rs.send_code(0x81)
rs.send_code(0x82)	#Right wrist out
rs.send_code(0x85)	#Right wrist in
rs.send_code(0x82)
rs.send_code(0x85)

raw_input('Enter')
rs.send_code(0x89)	#Left arm up
rs.send_code(0x89)
for i in range(0,2):
	rs.send_code(0x8B)	#Tilt left
	rs.send_code(0x83)	#Tilt right	
	rs.send_code(0x83)
	rs.send_code(0x8B)
rs.send_code(0x8C)	#Left arm down
rs.send_code(0x84)	#Right arm down
rs.send_code(0x8C)
rs.send_code(0x84)

raw_input('Enter')
rs.send_code(0xC4)	#Hi 5

raw_input('Enter')
rs.send_code(0xCE)	#Roar

print "fin"

