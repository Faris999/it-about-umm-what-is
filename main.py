from scene import SCENES, Option
from copy import deepcopy

history = []

# main game loop
def main():
    current_scene = SCENES['beginning']
    while True:
        current_scene = current_scene.play()
        history.append(current_scene.name)
        if history[-6:] == ['library', 'east hall', 'west hall', 'east hall', 'library', 'west hall'] and 'continue reading' in history:
            current_scene = deepcopy(current_scene)
            current_scene.options.options.append(Option('Go to the door', 'secret'))
        if history.count('talk') >= 8 and current_scene.name == 'talk' and 'long' not in history:
            current_scene = deepcopy(current_scene)
            current_scene.options.options.append(Option('Hmm...', 'long'))
        if current_scene == SCENES['empty']:
            # should be unreachable because there is no end scene
            print("You won!")
            break

if __name__ == '__main__':
    main()
