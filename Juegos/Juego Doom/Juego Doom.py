import pygame
import math
import sys

"""Antes de ejecutarlo tienes que agregar a la misma carpeta donde guardes el código, ciertas imagenes png (para los dos enemigos, el arma y el arma al disparar)
Por ahí en el código están los nombres que le tienes que poner a esas imagenes.

Creo que son weapon.png, weaponshoot.png cosas así
Cacodemon.png y imp.png
También tienes que buscar un .mp3 que haga de sonido de disparo pero puede simplemente ir a la linea que lo pide y ponerlo como comentario pa que te deja ejecutarlo"""

# Configuraciones
WIDTH, HEIGHT = 800, 600
FPS = 60
HALF_HEIGHT = HEIGHT // 2
FOV = math.pi / 3  # 60 grados
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = (NUM_RAYS / (2 * math.tan(FOV / 2)))
SCALE = WIDTH // NUM_RAYS


# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (110, 110, 110)
GREEN = (0, 220, 0)


# Mapa (1 = pared, 0 = espacio vacío)
game_map = [
    '111111111111111',
    '1             1',
    '1    11       1',
    '1             1',
    '1   1         1',
    '1   1  1      1',
    '1      1      1',
    '1             1',
    '111111111111111',
]


TILE = 50


# Enemigos con nombre, posición y sprite
class Enemy:
    def __init__(self, name, x, y, sprite):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.health = 100


enemies = []


# --- Jugador ---
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.angle = 0
        self.speed = 3


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)


        keys = pygame.key.get_pressed()
        dx, dy = 0, 0


        if keys[pygame.K_w]:
            dx += cos_a * self.speed
            dy += sin_a * self.speed
        if keys[pygame.K_s]:
            dx += -cos_a * self.speed
            dy += -sin_a * self.speed
        if keys[pygame.K_a]:
            dx += sin_a * self.speed
            dy += -cos_a * self.speed
        if keys[pygame.K_d]:
            dx += -sin_a * self.speed
            dy += cos_a * self.speed


        if not wall_collision(self.x + dx, self.y):
            self.x += dx
        if not wall_collision(self.x, self.y + dy):
            self.y += dy


        if keys[pygame.K_LEFT]:
            self.angle -= 0.04
        if keys[pygame.K_RIGHT]:
            self.angle += 0.04
        self.angle %= 2 * math.pi


def wall_collision(x, y):
    map_x = int(x // TILE)
    map_y = int(y // TILE)
    if 0 <= map_x < len(game_map[0]) and 0 <= map_y < len(game_map):
        return game_map[map_y][map_x] == '1'
    return True


# Raycasting paredes
def ray_casting(screen, player_pos, player_angle):
    cur_angle = player_angle - FOV / 2
    depth_buffer = [float('inf')] * NUM_RAYS  # Para ocultar enemigos detrás de paredes


    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)


        for depth in range(MAX_DEPTH):
            x = player_pos[0] + depth * cos_a
            y = player_pos[1] + depth * sin_a


            map_x = int(x // TILE)
            map_y = int(y // TILE)


            if 0 <= map_x < len(game_map[0]) and 0 <= map_y < len(game_map):
                if game_map[map_y][map_x] == '1':
                    depth_corr = depth * math.cos(player_angle - cur_angle)  # ojo de pez corregido
                    depth_buffer[ray] = depth_corr
                    wall_height = 21000 / (depth_corr + 0.0001)
                    color = 255 / (1 + depth_corr * depth_corr * 0.0001)
                    pygame.draw.rect(screen, (color, color, color),
                                     (ray * SCALE, HALF_HEIGHT - wall_height // 2, SCALE, wall_height))
                    break
        cur_angle += DELTA_ANGLE


    return depth_buffer


def draw_minimap(screen, player):
    mini_map_scale = 5
    for y, row in enumerate(game_map):
        for x, char in enumerate(row):
            color = DARKGRAY if char == '1' else WHITE
            rect = pygame.Rect(x * TILE // mini_map_scale, y * TILE // mini_map_scale,
                               TILE // mini_map_scale - 2, TILE // mini_map_scale - 2)
            pygame.draw.rect(screen, color, rect)


    pygame.draw.circle(screen, GREEN, (int(player.x // mini_map_scale), int(player.y // mini_map_scale)), 5)


    # Enemigos minimapa
    for enemy in enemies:
        pygame.draw.circle(screen, (220, 0, 0), (int(enemy.x // mini_map_scale), int(enemy.y // mini_map_scale)), 5)


def draw_enemies_3d(screen, player, depth_buffer):
    for enemy in enemies:
        dx = enemy.x - player.x
        dy = enemy.y - player.y


        distance = math.hypot(dx, dy)
        theta = math.atan2(dy, dx)


        gamma = theta - player.angle
        if gamma > math.pi:
            gamma -= 2 * math.pi
        if gamma < -math.pi:
            gamma += 2 * math.pi


        if -FOV / 2 < gamma < FOV / 2 and distance > 30:
            depth = distance * math.cos(gamma)


            ray = int((gamma + FOV / 2) / DELTA_ANGLE)
            if 0 <= ray < NUM_RAYS and depth < depth_buffer[ray]:
                sprite_scale = 21000 / (depth + 0.0001)
                sprite = pygame.transform.scale(enemy.sprite, (int(sprite_scale), int(sprite_scale)))


                sprite_x = ray * SCALE - sprite.get_width() // 2
                sprite_y = HALF_HEIGHT - sprite.get_height() // 2


                screen.blit(sprite, (sprite_x, sprite_y))


def draw_weapon(screen, weapon_sprite):
    # Cambia estos valores para ajustar el tamaño del arma
    desired_width = 250
    desired_height = 200
    scaled_weapon = pygame.transform.scale(weapon_sprite, (desired_width, desired_height))


    pos_x = WIDTH // 2 - desired_width // 2
    pos_y = HEIGHT - desired_height
    screen.blit(scaled_weapon, (pos_x, pos_y))


def shoot(player, enemies):
    # Dispara hacia el centro del FOV y reduce vida del enemigo si está apuntado
    SHOOT_RANGE = 300
    SHOOT_ANGLE = math.radians(5)  # ±5 grados


    for enemy in enemies:
        dx = enemy.x - player.x
        dy = enemy.y - player.y


        distance = math.hypot(dx, dy)
        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if gamma > math.pi:
            gamma -= 2 * math.pi
        if gamma < -math.pi:
            gamma += 2 * math.pi


        if -SHOOT_ANGLE < gamma < SHOOT_ANGLE and distance <= SHOOT_RANGE:
            enemy.health -= 50
            print(f"Disparado a {enemy.name}! Vida restante: {enemy.health}")
            if enemy.health <= 0:
                enemies.remove(enemy)
            break  # Solo un enemigo por disparo


def main():
    pygame.init()
    pygame.mixer.init()


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Doom Raycasting con Enemigos y Arma")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)


    # Cargar sprites enemigos y arma
    try:
        imp_sprite = pygame.image.load("imp.png").convert_alpha()#Enemigo 1
        cacodemon_sprite = pygame.image.load("cacodemon.png").convert_alpha() #Enemigo 2
        weapon_sprite = pygame.image.load("weapon.png").convert_alpha()  # sprite normal arma
        weapon_shoot_sprite = pygame.image.load("weaponshoot.png").convert_alpha()  # sprite disparo arma
        #caco_sound = pygame.mixer.Sound("cacosound.mp3")
        shoot_sound = pygame.mixer.Sound("shoot.mp3")
    except Exception as e:
        print("Error cargando archivos:", e)
        print("Coloca imp.png, cacodemon.png, weapon.png, weaponshoot.png, cacosound.mp3 y shoot.mp3 en la carpeta.")
        pygame.quit()
        sys.exit()


    global enemies
    enemies = [
        Enemy("Imp", 200, 200, imp_sprite),
        Enemy("Cacodemon", 350, 300, cacodemon_sprite)
    ]


    player = Player()


    caco_sound_playing = False
    SOUND_RANGE = 150


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()


        player.movement()


        # Sonido Cacodemon
        caco = next((e for e in enemies if e.name == "Cacodemon"), None)
        """if caco:
            dist_caco = math.hypot(caco.x - player.x, caco.y - player.y)
            if dist_caco < SOUND_RANGE and not caco_sound_playing:
                caco_sound.play(-1)
                caco_sound_playing = True
            elif dist_caco >= SOUND_RANGE and caco_sound_playing:
                caco_sound.stop()
                caco_sound_playing = False"""


        weapon_is_shooting = False


        # Disparo con barra espaciadora
        if keys[pygame.K_SPACE]:
            shoot(player, enemies)
            shoot_sound.play()
            weapon_is_shooting = True


        screen.fill(BLACK)
        depth_buffer = ray_casting(screen, (player.x, player.y), player.angle)
        draw_enemies_3d(screen, player, depth_buffer)
        draw_minimap(screen, player)


        # Dibuja arma con sprite según si dispara o no
        if weapon_is_shooting:
            draw_weapon(screen, weapon_shoot_sprite)
        else:
            draw_weapon(screen, weapon_sprite)


        y_offset = 10
        for enemy in enemies:
            text = font.render(f"{enemy.name} HP: {enemy.health}", True, WHITE)
            screen.blit(text, (10, y_offset))
            y_offset += 30


        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()



