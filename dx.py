import pygame
import random
import math
import os
import array


pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

# ল্যাপটপের অটোমেটিক ফুল স্ক্রিন রেজোলিউশন সেটআপ
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("DX Ball - Week 1 Setup")
clock = pygame.time.Clock()


BLACK = (6, 8, 14)
PANEL_BG = (14, 20, 34)
WHITE = (255, 255, 255)
CYAN = (0, 235, 255)
GOLD = (255, 210, 0)
RED = (235, 45, 45)
GREEN = (45, 235, 110)
PURPLE = (180, 90, 255)
SILVER = (180, 190, 210)
DARK_SILVER = (70, 80, 100)


def create_tone_sound(freq, duration_ms, volume=0.25, wave_type="sine"):
    sample_rate = 44100
    num_samples = int(sample_rate * duration_ms / 1000)
    buf = array.array('h', [0] * num_samples)
    for i in range(num_samples):
        t = i / sample_rate
        decay = 1.0 - (i / num_samples)
        if wave_type == "sine":
            val = math.sin(2 * math.pi * freq * t)
        elif wave_type == "square":
            val = 0.6 if math.sin(2 * math.pi * freq * t) > 0 else -0.6
        buf[i] = int(32767 * volume * val * decay)
    return pygame.mixer.Sound(buffer=buf)

def create_bg_music():
    sample_rate = 44100
    notes = [261.63, 329.63, 392.00, 523.25, 392.00, 329.63, 293.66, 349.23, 440.00, 349.23, 329.63, 246.94]
    note_dur = 0.22
    total_samples = int(sample_rate * note_dur * len(notes))
    buf = array.array('h', [0] * total_samples)
    
    idx = 0
    for freq in notes:
        n_samples = int(sample_rate * note_dur)
        for i in range(n_samples):
            if idx < total_samples:
                t = i / sample_rate
                env = math.sin(math.pi * (i / n_samples))
                val = math.sin(2 * math.pi * freq * t) * 0.5 + math.sin(2 * math.pi * (freq * 0.5) * t) * 0.5
                buf[idx] = int(32767 * 0.12 * val * env)
                idx += 1
    return pygame.mixer.Sound(buffer=buf)

SND_HIT = create_tone_sound(540, 45, 0.3, "sine")
SND_POWER = create_tone_sound(1050, 140, 0.35, "sine")
BG_MUSIC = create_bg_music()
BG_MUSIC.play(loops=-1)

class GameData:
    def __init__(self):
        self.coins = 60
        self.high_score = 0

game_data = GameData()

def draw_3d_sphere(surface, cx, cy, radius, main_col, dark_col, glow_col=None):
    if glow_col:
        pygame.draw.circle(surface, glow_col, (int(cx), int(cy)), int(radius + 4))
    steps = 10
    for i in range(steps):
        ratio = i / steps
        r = int(radius * (1.0 - ratio * 0.65))
        offset_x = int(-radius * 0.25 * ratio)
        offset_y = int(-radius * 0.25 * ratio)
        col = (
            int(dark_col[0] + (main_col[0] - dark_col[0]) * ratio),
            int(dark_col[1] + (main_col[1] - dark_col[1]) * ratio),
            int(dark_col[2] + (main_col[2] - dark_col[2]) * ratio),
        )
        pygame.draw.circle(surface, col, (int(cx + offset_x), int(cy + offset_y)), max(1, r))
    pygame.draw.circle(surface, WHITE, (int(cx - radius * 0.35), int(cy - radius * 0.35)), max(2, int(radius * 0.22)))

font_logo = pygame.font.SysFont("Arial Black", 64, bold=True)
font_btn = pygame.font.SysFont("Arial", 22, bold=True)
font_sm = pygame.font.SysFont("Arial", 15)

rot_angle = 0.0


running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            cx = SCREEN_WIDTH // 2
            exit_btn = pygame.Rect(cx - 140, 380, 280, 52)
            if exit_btn.collidepoint(mx, my):
                running = False

    cx = SCREEN_WIDTH // 2

 
    banner_rect = pygame.Rect(cx - 280, 45, 560, 110)
    pygame.draw.rect(screen, PANEL_BG, banner_rect, border_radius=12)
    pygame.draw.rect(screen, CYAN, banner_rect, 4, border_radius=12)
    
    logo_txt = font_logo.render("DX Ball", True, WHITE)
    logo_shadow = font_logo.render("DX Ball", True, CYAN)
    screen.blit(logo_shadow, (cx - logo_txt.get_width()//2 + 3, 62))
    screen.blit(logo_txt, (cx - logo_txt.get_width()//2, 59))

  
    menu_items = [
        ("PLAY GAME", pygame.Rect(cx - 140, 240, 280, 52), CYAN),
        ("3D BALL SHOP", pygame.Rect(cx - 140, 310, 280, 52), GOLD),
        ("EXIT GAME", pygame.Rect(cx - 140, 380, 280, 52), RED),
    ]
    for text, rect, col in menu_items:
        pygame.draw.rect(screen, PANEL_BG, rect, border_radius=10)
        pygame.draw.rect(screen, col, rect, 2, border_radius=10)
        t = font_btn.render(text, True, WHITE)
        screen.blit(t, (rect.centerx - t.get_width()//2, rect.centery - t.get_height()//2))

    stat_txt = font_btn.render(f"HIGH SCORE: {game_data.high_score}   |   COINS: {game_data.coins}", True, GOLD)
    screen.blit(stat_txt, (cx - stat_txt.get_width()//2, 470))

    rot_angle += 0.035
    bx = int(SCREEN_WIDTH * 0.80)
    by = SCREEN_HEIGHT - 190
    br = 135
    draw_3d_sphere(screen, bx, by, br, (240, 240, 245), (110, 110, 125))

    tip_txt = font_sm.render("Week 1: Project Setup, Pygame Fullscreen & Welcome Menu", True, DARK_SILVER)
    screen.blit(tip_txt, (cx - tip_txt.get_width()//2, SCREEN_HEIGHT - 30))

    pygame.display.flip()

pygame.quit()