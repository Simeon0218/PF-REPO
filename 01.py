PAPER = 5.8
MATERIAL = 7.2
GLUE = 1.2

paper_count = int(input())
material_count = int(input())
glue_litres = float(input())
discount = int(input()) / 100

total_paper = paper_count * PAPER
total_material = material_count * MATERIAL
total_glue = glue_litres * GLUE



total_cost = total_glue + total_material + total_paper
total_discounted = total_cost - total_cost * discount

print(f"{total_discounted:.3f}")
