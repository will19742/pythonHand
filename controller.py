import pyfirmata

comport = 'COM3'
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:9:o')
led_2 = board.get_pin('d:10:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:12:o')
led_5 = board.get_pin('d:13:o')

def led(fingerUp):
    # Apagar todos los LEDs primero
    led_1.write(0)
    led_2.write(0)
    led_3.write(0)
    led_4.write(0)
    led_5.write(0)

    # Encender los LEDs correspondientes a los dedos levantados
    if fingerUp[0] == 1:
        led_1.write(1)
    if fingerUp[1] == 1:
        led_2.write(1)
    if fingerUp[2] == 1:
        led_3.write(1)
    if fingerUp[3] == 1:
        led_4.write(1)
    if fingerUp[4] == 1:
        led_5.write(1)
