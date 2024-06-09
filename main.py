from PIL import Image

def crop_image(image_path, num_cols, num_rows):
    # Load ảnh gốc
    image = Image.open(image_path)

    # Tính kích thước ảnh gốc
    width, height = image.size

    # Tính kích thước của mỗi bức ảnh nhỏ
    small_width = width // num_cols
    small_height = height // num_rows

    cropped_images = []
    for row in range(num_rows):
        for col in range(num_cols):
            # Tính vị trí cắt của mỗi bức ảnh nhỏ
            left = col * small_width
            upper = row * small_height
            right = left + small_width
            lower = upper + small_height

            # Cắt và lưu trữ bức ảnh nhỏ
            cropped_image = image.crop((left, upper, right, lower))
            cropped_images.append(cropped_image)

    return cropped_images

# Đường dẫn của ảnh gốc
image_path = "img.png"

# Số ảnh cắt ngang và số ảnh cắt dọc
num_cols = 9
num_rows = 1

# Cắt ảnh thành các bức ảnh nhỏ
cropped_images = crop_image(image_path, num_cols, num_rows)

# Lưu trữ các bức ảnh nhỏ
for i, image in enumerate(cropped_images):
    image.save(f"small_image_{i}.png")