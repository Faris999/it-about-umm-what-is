from scene import SCENES

# main game loop
def main():
    current_scene = SCENES['beginning']
    while True:
        current_scene = current_scene.play()
        if current_scene == SCENES['empty']:
            # should be unreachable because there is no end scene
            print("You won!")
            break

if __name__ == '__main__':
    main()