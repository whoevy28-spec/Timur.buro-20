from PIL import Image
import os


for num in range(5):
    file_path = f"photo_end_{num}"
    os.mkdir(file_path)

    img = Image.open(f"photo_{num}.jpg")
    img.save(f"photo_end_{num}/photo_{num}.png", "png")
    img = Image.open(f"photo_end_{num}/photo_{num}.png")

    vk = img.resize((1400, 1400))
    vk.save(f"photo_end_{num}/photo_vk{num}.jpg")

    inst = img.resize((1080, 1080))
    inst = inst.crop((10, 0, inst.width - 10, inst.height))
    inst.save(f"photo_end_{num}/photo_inst{num}.jpg")

    fb = img.resize((1200, 628))
    fb.save(f"photo_end_{num}/photo_fb{num}.jpg")