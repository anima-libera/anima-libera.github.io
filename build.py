
import re

class Page:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

def tag_regex(tag_name, property_name):
	return r"<\s*{tag}\s+{property}\s*=\s*\"([^\"]*)\"\s*/>".format(
		tag = tag_name, property = property_name)

def handle_insert_tags(code, page):
	def repl(match):
		file_path = f"src/{match.group(1)}"
		print(f"Inserting {file_path}")
		return open(file_path, "r").read()
	return re.sub(tag_regex("insert", "file"), repl, code)

def handle_placeholder_tags(code, page):
	def repl(match):
		what = match.group(1)
		print(f"Filling placeholder {what}")
		return page.__dict__[what]
	return re.sub(tag_regex("placeholder", "what"), repl, code)

transf_all = [
	handle_insert_tags,
	handle_placeholder_tags,
]

page_list = [
	Page(
		name = "Home Page",
		path_src = "src/home.html",
		path_gen = "gen/home.html",
		transf_list = transf_all,
	),
	Page(
		name = "Tabs Page",
		path_src = "src/tabs.html",
		path_gen = "gen/tabs.html",
		transf_list = transf_all,
	),
	Page(
		name = "Test Page",
		path_src = "src/template.html",
		path_gen = "gen/test.html",
		transf_list = transf_all,
		content = "awa ^^",
	),
]

for page in page_list:
	print(f"Generating \"{page.name}\" to {page.path_gen}")
	src_file = open(page.path_src, "r")
	src_code = src_file.read()
	src_file.close()

	gen_code = src_code
	for transformation in page.transf_list:
		print(f"Applying {transformation.__name__}")
		gen_code = transformation(gen_code, page)

	gen_file = open(page.path_gen, "w")
	gen_file.write(gen_code)
	gen_file.close()
