#  place this code at the top of server.py uncommented to bypass the entire system to see xbox controller events
#
# import pygame
#
# print("Getting Xbox Controller Events")
#
# os.environ["SDL_VIDEODRIVER"] = "dummy"
#
# pygame.init()
#
# pygame.joystick.init()
# joystick_count = pygame.joystick.get_count()
# print("joystick_count is ", joystick_count)
# if joystick_count > 0:
#    joystick = pygame.joystick.Joystick(0)
#    joystick.init()
#
# while True:
#    for event in pygame.event.get():
#        print("event is ", event)
#        if event.type == pygame.JOYBUTTONUP:
#            print("button up ", event.button)
#        elif event.type == pygame.JOYBUTTONDOWN:
#            print("button down ", event.button)
#        elif event.type == pygame.JOYAXISMOTION:
#            print("event.axis ", event.axis, "value: ", event.value)
#        elif event.type == pygame.JOYHATMOTION:
#            print("event.hat ", event.hat, "value: ", event.value, "instance_id:", event.instance_id)
#        else:
#            print("Unprocessed event:", event)
#
#    time.sleep(0.2)
