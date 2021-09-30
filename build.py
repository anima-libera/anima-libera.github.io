
import re

class Page:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

page_list = [
	Page(
		name = "Home Page",
		path_src = "src/home.html",
		path_gen = "gen/home.html",
	),
	Page(
		name = "Tabs Page",
		path_src = "src/tabs.html",
		path_gen = "gen/tabs.html",
	),
]

def handle_insert_tags(code):
	def replace_insert(match):
		file = open(f"src/{match.group(1)}", "r")
		content = file.read()
		file.close()
		return content
	return re.sub(r"<\s*insert\s+file\s*=\s*\"([^\"]*)\"\s*/>",
		replace_insert, code)

transformation_list = [
	handle_insert_tags,
]

for page in page_list:
	print(f"Generating \"{page.name}\" to {page.path_gen}")
	src_file = open(page.path_src, "r")
	src_code = src_file.read()
	src_file.close()

	gen_code = src_code
	for transformation in transformation_list:
		print(f"Applying {transformation.__name__}")
		gen_code = transformation(gen_code)

	gen_file = open(page.path_gen, "w")
	gen_file.write(gen_code)
	gen_file.close()
