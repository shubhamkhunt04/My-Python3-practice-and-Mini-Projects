import  pygame
pygame.mixer.init()
pygame.mixer.music.load("musics1.mp3")
pygame.mixer.music.play(-1)

print("write stop")
while True:
    input1 = input()
    if input1 == "stop":
        pygame.mixer.music.stop()
        break




