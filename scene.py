import helper
import dialogue_parser as parser

class Scene():
    def __init__(self, name, texts, options):
        self.name = name
        self.texts = texts
        self.options = options

    def play(self):
        for text in self.texts:
            print(text)
            input()
        return self.options.print_options()

class Options():
    def __init__(self, options):
        self.options = options

    def print_options(self):
        for i, option in enumerate(self.options): 
            print(f'{i+1}. {option.text}')
        choice = input("> ")
        if choice == "exit":
            helper.exit_game()
        elif choice == "help":
            helper.help_menu()
            return self.print_options()
        elif choice in [str(i+1) for i in range(len(self.options))]:
            return self.options[int(choice)-1].get_next_scene()
        else:
            print("Invalid choice")
            return self.print_options()

class Option():
    def __init__(self, text, next_scene):
        self.text = text
        self.next_scene = next_scene

    def get_next_scene(self):
        return resolve_scene(self.next_scene)

SCENES = parser.parse('dialogues.txt')

SCENES['empty'] = Scene('empty', [], Options([]))

def empty_option(text):
    return Options([Option('...', Scene('empty', text, Options([])))])

def resolve_scene(scene_name):
    return SCENES[scene_name]