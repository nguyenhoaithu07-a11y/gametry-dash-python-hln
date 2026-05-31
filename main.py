# import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Python")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Cấu hình nhân vật
player_rect = pygame.Rect(100, HEIGHT - 90, 40, 40)
player_gravity = 0
is_jumping = False

# Cấu hình chướng ngại vật
obstacle_width = 30
obstacle_height = 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - 90
obstacle_speed = 7

# Điểm số
score = 0
clock = pygame.time.Clock()

# Vòng lặp game chính
while True:
    screen.fill(BLACK)

    # Nhận sự kiện từ bàn phím
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_gravity = -16
                is_jumping = True

    # Vật lý nhảy của nhân vật
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.y >= HEIGHT - 90:
        player_rect.y = HEIGHT - 90
        is_jumping = False

    # Di chuyển gai từ phải sang trái
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        score += 1
        if score % 3 == 0:
            obstacle_speed += 1

    # Tạo Rect ảo để tính toán va chạm chính xác
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    # 💥 KIỂM TRA VA CHẠM (Nếu chạm nhau là chết ngay)
    if player_rect.colliderect(obstacle_rect):
        print(f"Game Over! Điểm của bạn là: {score}")
        score = 0
        obstacle_speed = 7
        obstacle_x = WIDTH          # QUAN TRỌNG: Đẩy cái gai về lại bên phải ngay lập tức để không bị xuyên qua nữa
        player_rect.y = HEIGHT - 90 # Đưa nhân vật về mặt đất
        player_gravity = 0          # Đứng im tại chỗ

    # Tọa độ 3 đỉnh để vẽ hình tam giác (gai nhọn)
    triangle_points = [
        (obstacle_x + obstacle_width // 2, obstacle_y),
        (obstacle_x, obstacle_y + obstacle_height),
        (obstacle_x + obstacle_width, obstacle_y + obstacle_height)
    ]

    # Vẽ mọi thứ lên màn hình
    pygame.draw.line(screen, WHITE, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 3) # Mặt đất
    pygame.draw.rect(screen, BLUE, player_rect)                                # Nhân vật vuông xanh
    pygame.draw.polygon(screen, RED, triangle_points)                          # Gai tam giác đỏ

    pygame.display.flip()
    clock.tick(60)

