import scene

def parse(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    scenes = {}
    lines_iter = iter(lines)
    while (line := next(lines_iter, None)) is not None:
        scene_name = line.strip()[1:-1]
        texts = []
        while (line := next(lines_iter, None)) != '\n' and line is not None:
            texts.append(line)
        options = []
        while (line := next(lines_iter, None)) != '\n' and line is not None:
            split = line.strip().split('[')
            option_text = split[0].strip()
            next_scene_name = split[1][:-1]
            options.append(scene.Option(option_text, next_scene_name))
        scenes[scene_name] = scene.Scene(scene_name, texts, scene.Options(options))

    return scenes