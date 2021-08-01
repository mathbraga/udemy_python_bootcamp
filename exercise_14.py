from PIL import Image

mask = Image.open("src/mask.png")
matrix = Image.open("src/word_matrix.png")

mask = mask.resize(matrix.size)
mask.putalpha(128)
matrix.paste(mask, (0,0), mask)
matrix.save("src/answer.png")