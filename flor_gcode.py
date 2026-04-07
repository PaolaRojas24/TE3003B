# Dibujo bidimencional de una Flor de fuego usando G-code y tres colores.
# Materia: Integración de robótica y sistemas inteligentes
# Módulo 1: Tecnologías emergentes
# Alumno: Paola Rojas Domínguez

# Importar librerías
import os
import sys
import time
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

# Configuración de IP
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)

# Variables con coordenadas base
base_x = 150
base_y = 320
base_z = 140

# Inicialización
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.move_gohome(wait=True)

# Posición inicial
arm.set_position(x=base_x, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))

# Espera de inicio manual
cont = 0
x = 's'
while x != "a":
    x = input()

# Contar líneas del primer G-code
with open("flor1_0001.ngc", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)
start_time = time.time()

# Posición de inicio de dibujo
arm.set_position(x=base_x  , y=base_y , z=base_z, roll=180, pitch=0, yaw=0, speed=100, wait=True)
altura = 1

# Ajuste manual de altura (colocar color verde)
while x != "q":
    if x == "a": 
        arm.set_position(x=base_x  , y=base_y , z=base_z - altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)
        altura = altura + 1
    x = input()

# Lectura de primer G-code y movimiento para dibujar
with open('flor1_0001.ngc') as gcode:
    for line in gcode:
        line = line.strip()
        coord = re.findall(r'[XY].?\d+.\d+', line)

        if coord :
            xx = coord[0].split('X')
            xx = xx[1]
            yy = coord[1].split('Y')
            yy = yy[1]

            arm.set_position(x=base_x - float(xx) , y=base_y - float(yy), z=base_z-altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)
            
            cont = cont + 1
            if cont % 100 == 0:
                print (str(cont) + " lines. Lines to finish "  + str(lines - cont) + "\r")

# Volver a posición inicial
arm.move_gohome(wait=True)

arm.set_position(x=base_x, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))

# Espera de inicio manual
cont = 0
x = 's'
while x != "a":
    x = input()

# Contar líneas del segundo G-code
with open("flor2_0001.ngc", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)
start_time = time.time()

# Posición de inicio de dibujo
arm.set_position(x=base_x  , y=base_y , z=base_z, roll=180, pitch=0, yaw=0, speed=100, wait=True)
altura = 1

# Ajuste manual de altura (colocar color naranja)
while x != "q":
    if x == "a": 
        arm.set_position(x=base_x  , y=base_y , z=base_z - altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)
        altura = altura + 1
    x = input()

# Lectura de segundo G-code y movimiento para dibujar
with open('flor2_0001.ngc') as gcode:
    for line in gcode:
        line = line.strip()
        coord = re.findall(r'[XY].?\d+.\d+', line)

        if coord :
            xx = coord[0].split('X')
            xx = xx[1]
            yy = coord[1].split('Y')
            yy = yy[1]
            
            arm.set_position(x=base_x - float(xx) , y=base_y - float(yy), z=base_z-altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)

            cont = cont + 1
            if cont % 100 == 0:
                print (str(cont) + " lines. Lines to finish "  + str(lines - cont) + "\r")

# Volver a posición inicial
arm.move_gohome(wait=True)

arm.set_position(x=base_x, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))

# Espera de inicio manual
cont = 0
x = 's'
while x != "a":
    x = input()

# Contar líneas del tercer G-code
with open("flor3_0001.ngc", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)
start_time = time.time()

# Posición de inicio de dibujo
arm.set_position(x=base_x  , y=base_y , z=base_z, roll=180, pitch=0, yaw=0, speed=100, wait=True)
altura = 1

# Ajuste manual de altura (colocar color amarillo)
while x != "q":
    if x == "a": 
        arm.set_position(x=base_x  , y=base_y , z=base_z - altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)
        altura = altura + 1
    x = input()

# Lectura de tercer G-code y movimiento para dibujar
with open('flor3_0001.ngc') as gcode:
    for line in gcode:
        line = line.strip()
        coord = re.findall(r'[XY].?\d+.\d+', line)

        if coord :
            xx = coord[0].split('X')
            xx = xx[1]
            yy = coord[1].split('Y')
            yy = yy[1]
            
            arm.set_position(x=base_x - float(xx) , y=base_y - float(yy), z=base_z-altura, roll=180, pitch=0, yaw=0, speed=100, wait=True)

            cont = cont + 1
            if cont % 100 == 0:
                print (str(cont) + " lines. Lines to finish "  + str(lines - cont) + "\r")

# Finalización            
print("--- %s seconds ---" % (time.time() - start_time))
arm.set_position(x=base_x, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))
arm.set_position(x=base_x+50, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))
arm.set_position(x=base_x-50, y=base_y, z=base_z+50, roll=180, pitch=0, yaw=0, speed=100, wait=True)
print(arm.get_position(), arm.get_position(is_radian=True))

# Regresar a home
arm.move_gohome(wait=True)
arm.disconnect()