
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

def insert_footer(code):
	footer_file = open("src/footer.html", "r")
	footer_code = footer_file.read()
	footer_file.close()
	return code.format(footer = "\n" + footer_code)

transformation_list = [
	insert_footer,
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
