
init python:
    import random
    import time as tp
    import math
    import store
    import pygame




init python:
    def random_color():
        colors = [
            "#ff6c6c", "#495ef7", "#81ff5e", "#f68eff",
            "#00FFD2", "#9156ff", "#FF9C00", "#FFEA00", "#FFFFFF"
        ]
        return renpy.random.choice(colors)

# transform para cambiar colores suavemente
transform color_wipe_anim:
    xalign 0.5 yalign 0.5
    block:
        ease 3.0 matrixcolor TintMatrix(random_color())
        easein 3.0 matrixcolor TintMatrix(random_color()) 
        ease 3.0 matrixcolor TintMatrix(random_color())
        easein 3.0 matrixcolor TintMatrix(random_color())
        ease 3.0 matrixcolor TintMatrix(random_color())
        easein 3.0 matrixcolor TintMatrix(random_color())
        ease 3.0 matrixcolor TintMatrix(random_color())
        easein 3.0 matrixcolor TintMatrix(random_color())
        ease 3.0 matrixcolor TintMatrix(random_color())
        repeat

image pass_bg_color = "infinity_pass.png"


init python:

    class RGBTrail(renpy.Displayable):
        def __init__(self, image="choko/choko_normal.png", offset=8, speed=0.1, **kwargs):
            super(RGBTrail, self).__init__(**kwargs)
            self.image_path = image
            self.offset = offset
            self.speed = speed
            self.time = 0
            self.color_index = 0

            # 🎨 Lista de colores predefinidos (RGB)
            # Puedes editar o añadir más tonos aquí
            predefined_colors = [
                (1.0, 0.3, 0.3),  # rojo suave
                (0.3, 1.0, 0.3),  # verde
                (0.3, 0.3, 1.0),  # azul
                (1.0, 0.8, 0.3),  # amarillo
                (0.7, 0.3, 1.0),  # violeta
                (0.3, 1.0, 1.0)   # cian
            ]

            # 🧠 Precarga imágenes tintadas una sola vez
            self.precolored = [
                im.MatrixColor(Image(self.image_path), im.matrix.tint(r, g, b))
                for (r, g, b) in predefined_colors
            ]

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            self.time += self.speed

            off_x = int(math.sin(self.time) * self.offset)
            off_y = int(math.cos(self.time * 1.3) * self.offset / 2)

            # Cambiar cada cierto tiempo a otro set de color
            if int(self.time * 12) % 15 == 0:
                self.color_index = (self.color_index + 3) % len(self.precolored)

            # Usa tres imágenes de la lista
            for i in range(3):
                img = self.precolored[(self.color_index + i) % len(self.precolored)]
                col_render = renpy.render(img, width, height, st, at)
                if i == 0:
                    render.blit(col_render, (off_x, off_y))
                elif i == 1:
                    render.blit(col_render, (-off_x, off_y))
                else:
                    render.blit(col_render, (0, -off_y))


            renpy.redraw(self, 0.02)
            return render





init python:
    class GlitchSlices(renpy.Displayable):
        def __init__(self, image="glitch_anchor.webp", max_offset=32, num_blocks=10, **kwargs):
            super(GlitchSlices, self).__init__(**kwargs)
            self.image = Image(image) # la imagen que usa
            self.max_offset = max_offset # maximo de movimiento de animacion izquierda y derecha
            self.num_blocks = num_blocks # numero de cuadros por segundo asi cambiara
            self.width = 1280
            self.height = 720

        def render(self, width, height, st, at):
            width = self.width
            height = self.height

            img_render = renpy.render(self.image, width, height, st, at)
            render = renpy.Render(img_render.width, img_render.height)

            block_height = img_render.height // self.num_blocks

            for i in range(self.num_blocks):
                y = i * block_height
                x_offset = random.randint(-self.max_offset, self.max_offset)
                clip_rect = (0, y, img_render.width, block_height)

                render.blit(img_render,
                            (x_offset, y),
                            clip_rect)

            renpy.redraw(self, 0.2)  # Redibuja cada 0.2s para animación fluida
            # puede saturar renpy si es menos
            return render




init python:

    class ParticuleGravity(renpy.Displayable):
        def __init__(self, image, count=12, max_radius=200, duration=1.0, max_size=64, gravity=300.0, **properties):
            super(ParticuleGravity, self).__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.duration = duration
            self.max_size = max_size
            self.gravity = gravity  # gravedad en pixeles por segundo^2
            self.start_time = None
            self.particles = []

            for _ in range(count):
                angle = random.uniform(0, 2 * math.pi) # π
                speed = random.uniform(0.5, 1.0)
                scale = random.uniform(0.5, 1.0)
                initial_vy = random.uniform(-100, -300)  # velocidad vertical inicial (hacia arriba)

                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "scale": scale,
                    "vy0": initial_vy,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            t = elapsed / self.duration

            if t >= 1.0:
                return renpy.Render(width, height)

            rv = renpy.Render(width, height)

            for p in self.particles:
                dist = self.max_radius * p["speed"] * t
                x = int(math.cos(p["angle"]) * dist)

                # Gravedad aplicada aquí
                vy = p["vy0"] + self.gravity * t  # velocidad final
                y = int(math.sin(p["angle"]) * dist + vy * t)

                size = int(self.max_size * p["scale"] * (1.0 - t))
                alpha = int(255 * (1.0 - t))

                particle_img = self.image
                cr = renpy.render(particle_img, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv



init python:

    class AnimationCube(renpy.Displayable):
        def __init__(self, image, count=5, max_size=200, speed=1.0, frequency=1.0, amount=1.0, cycle_duration=2.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_size = max_size
            self.speed = speed
            self.amount = amount
            self.frequency = frequency
            self.cycle_duration = cycle_duration
            self.start_time = None

            # Fase temporal uniforme para cada copia
            self.offsets = [(i / count) * cycle_duration for i in range(count)]
            self.directions = [i * (2 * math.pi / count) for i in range(count)]  # distribución circular

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = (st - self.start_time) % self.cycle_duration
            base_size = 12
            rv = renpy.Render(self.max_size, self.max_size)

            for i in range(self.count):
                phase = (elapsed + self.offsets[i]) % self.cycle_duration

                # Normaliza a [0,1]
                norm_time = phase / self.cycle_duration

                # Cálculo del tamaño con expansión + temblor
                pulse = math.sin(norm_time * math.pi * 2 * self.frequency) * self.amount
                growth = norm_time  # ahora es de 0 a 1 uniforme
                size_factor = growth + pulse * (1 - growth)
                size = int(base_size + (self.max_size - base_size) * size_factor)

                cr = renpy.render(self.image, size, size, st, at)

                angle = self.directions[i]
                radius = 10 + 600 * growth
                dx = int(math.cos(angle) * radius)
                dy = int(math.sin(angle) * radius)

                x = self.max_size // 2 - size // 2 + dx
                y = self.max_size // 2 - size // 2 + dy

                rv.blit(cr, (x, y))

            renpy.redraw(self, 0.02)
            return rv




init python:

    class MultiPulseAnimation(renpy.Displayable):
        def __init__(self, image, count=6, max_size=150, cycle_duration=2.0, frequency=1.0, amount=0.2, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_size = max_size
            self.cycle_duration = cycle_duration
            self.frequency = frequency
            self.amount = amount
            self.start_time = None

            # Distribuir fases y direcciones uniformemente
            self.offsets = [(i / count) * cycle_duration for i in range(count)]
            self.directions = [i * (2 * math.pi / count) for i in range(count)]

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = (st - self.start_time) % self.cycle_duration
            base_size = 12
            render_surface = renpy.Render(self.max_size, self.max_size)

            for i in range(self.count):
                # Tiempo desplazado por copia
                phase = (elapsed + self.offsets[i]) % self.cycle_duration
                norm_time = phase / self.cycle_duration  # de 0 a 1

                # Expansión con pulso
                pulse = math.sin(norm_time * math.pi * 2 * self.frequency) * self.amount
                size_factor = norm_time + pulse * (1 - norm_time)
                size = int(base_size + (self.max_size - base_size) * size_factor)

                # Render individual
                cr = renpy.render(self.image, size, size, st, at)

                # Posición circular
                angle = self.directions[i]
                radius = 10 + 20 * norm_time
                dx = int(math.cos(angle) * radius)
                dy = int(math.sin(angle) * radius)

                x = self.max_size // 2 - size // 2 + dx
                y = self.max_size // 2 - size // 2 + dy

                render_surface.blit(cr, (x, y))

            renpy.redraw(self, 0.02)
            return render_surface




init python:


    class ExplosionParticles(renpy.Displayable):
        def __init__(self, image, count=12, max_radius=200, duration=1.0, max_size=64, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.duration = duration
            self.max_size = max_size
            self.start_time = None
            self.particles = []

            # Generar ángulos y velocidades aleatorios para cada partícula
            for _ in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0.5, 1.0)
                scale = random.uniform(0.5, 1.0)
                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            t = elapsed / self.duration

            if t >= 1.0:
                return renpy.Render(width, height)  # Vacío después de explotar

            rv = renpy.Render(width, height)

            for p in self.particles:
                dist = self.max_radius * p["speed"] * t
                x = int(math.cos(p["angle"]) * dist)
                y = int(math.sin(p["angle"]) * dist)

                size = int(self.max_size * p["scale"] * (1.0 - t))  # Se hace más pequeña
                alpha = int(255 * (1.0 - t))  # Se desvanece

                particle_img = self.image
                cr = renpy.render(particle_img, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv











init python:

    class InfiniteSpiral(renpy.Displayable):
        def __init__(self, image, count=26, max_radius=250, max_size=128, spin_speed=6.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Inicializar partículas distribuidas
            for i in range(count):
                angle = (i / count) * 2 * math.pi
                scale = random.uniform(0.5, 1.0)
                self.particles.append({
                    "angle": angle,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time

            rv = renpy.Render(width, height)

            for p in self.particles:
                # Movimiento circular + expansión/contracción cíclica
                # Usamos un seno para que se acerquen y se alejen constantemente
                phase = (elapsed * 0.5) % 1.0  # 0 → 1 en bucle
                radius = self.max_radius * abs(math.sin(phase * math.pi))

                # Ángulo base + giro infinito
                angle = p["angle"] + self.spin_speed * elapsed

                x = int(math.cos(angle) * radius)
                y = int(math.sin(angle) * radius)

                # Partículas con tamaño "palpitante"
                size_factor = 0.5 + 0.5 * math.sin(elapsed * 2 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)
                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.01)
            return rv



init python:

    class ChaoticSpiral(renpy.Displayable):
        def __init__(self, image, count=25, max_radius=300, max_size=64, spin_speed=4.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Punto de fuga aleatorio (puede ser dentro o fuera del centro)
            self.focal_x = random.randint(-100, 100)
            self.focal_y = random.randint(-100, 100)

            # Configurar partículas con propiedades aleatorias
            for i in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0.5, 1.5)     # cada una se expande a distinta velocidad
                spin_offset = random.uniform(-2, 2)  # diferencia en el giro
                scale = random.uniform(0.4, 1.2)
                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "spin_offset": spin_offset,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            rv = renpy.Render(width, height)

            for p in self.particles:
                # Expansión radial caótica
                radius = self.max_radius * abs(math.sin(elapsed * p["speed"]))  # cada partícula late distinto

                # Ángulo base + giro infinito (desfasado por spin_offset)
                angle = p["angle"] + (self.spin_speed + p["spin_offset"]) * elapsed

                # Posición con punto de fuga (focal_x / focal_y)
                x = int(self.focal_x + math.cos(angle) * radius)
                y = int(self.focal_y + math.sin(angle) * radius)

                # Partículas con tamaño aleatorio + oscilación
                size_factor = 0.6 + 0.4 * math.sin(elapsed * 3 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)

                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv
















init python:

    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square # The size of the square it will wobble within.
            # Include more variables if you'd like to have more control over the positioning.

        def render(self, width, height, st, at):
            # Randomly move the offset of the text's render.
            xoff = (random.random()-.8) * float(self.square)
            yoff = (random.random()-.8) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ScareText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list


    config.custom_text_tags["sc"] = scare_tag




init python:
    # import random
    # import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["sc"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""

            if "font" not in self.tags:
                new_string += "{font=font/lick_big.ttf}"
                new_string += "{color=#FF6E6E}"

            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            if "font" not in self.tags:
                new_string += "{/color}"
                new_string += "{/font}"

            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string


