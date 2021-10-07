
import re
import io
import shutil
import os
import pathlib
from typing import Dict, List, Match, Pattern, Tuple, Callable

## Printing with indentation

indent_list: List[str] = []
on_line_start: bool = True

def indent_push(indent: str):
	""" Indent future lines printed via print_indent. """
	global indent_list
	indent_list.append(indent)

def indent_pop():
	""" Cancels the matching indent_push call. """
	global indent_list
	indent_list.pop()

def print_indent(*args, sep = " ", end = "\n"):
	""" Prints like the builtin print function, but with indentation
	managed via indent_push and indent_pop. """
	global indent_list, on_line_start
	capture = io.StringIO()
	print(*args, sep = sep, end = end, file = capture)
	lines = capture.getvalue().split("\n")
	capture.close()
	for line in lines[:-1]:
		if on_line_start:
			print("".join(indent_list), end = "")
		print(line, end = "\n")
		on_line_start = True
	line = lines[-1]
	if line != "":
		if on_line_start:
			print("".join(indent_list), end = "")
		print(line, end = "")
		on_line_start = False

## Page generation tools

def tag_re(tag_name: str) -> Pattern[str]:
	return re.compile(rf"""
		(?P<indent>((^|(?<=\n))[\ \t]*)?)
		<\s*
		(?:{tag_name})
		(?:
			\s*(?:\w+)\s*=\s*
			\"(?:[^\"]*)\"
		)*
		\s*/>
		(?P<newline>\n?)
	""", re.VERBOSE)

def prop_re() -> Pattern[str]:
	return re.compile(rf"""
		\s*(?P<name>\w+)\s*=\s*
		\"(?P<value>[^\"]*)\"
	""", re.VERBOSE)

def props_in_tag(tag_code: str) -> Dict[str, str]:
	return {
		match.group("name") : match.group("value")
		for match in re.finditer(prop_re(), tag_code)
	}

def content_indent(text: str, indent: str, newline: bool) -> str:
	capture = io.StringIO()
	print(text, file = capture)
	lines = capture.getvalue().split("\n")
	capture.close()
	while lines:
		if lines[-1] == "":
			lines.pop()
		else:
			break
	output = io.StringIO()
	for line in lines:
		print(indent, end = "", file = output)
		print(line, end = "\n", file = output)
	content = output.getvalue().rstrip()
	if newline:
		content += "\n"
	return content

def handle_custom_tags(page_code: str, page: Page) -> str:
	""" Expands the custom tags such as <insert ... /> into the designated
	content with correct formatting to not break indentation.
	It is recusive, so that custom tags in the inserted content are also
	expanded, etc. """

	def repl(match: Match) -> str:
		indent = match.group("indent")
		newline = match.group("newline") != ""
		props = props_in_tag(match.group())

		# Get content from file
		if file_name := props.get("file", None):
			file_path = f"src/{file_name}"
			print_indent(f"Inserting from file {file_path}")
			content = open(file_path, "r").read()
		
		# Get content from page description
		elif content_name := props.get("what", None):
			print_indent(f"Inserting from member {content_name}")
			content = page.__dict__[content_name]

		else:
			print_indent(f"\x1b[31mOh nyo >< {props}\x1b[39m")
			assert False
		
		# Format content
		content = content_indent(content.strip(), indent, newline)
		return content

	new_code, modif_count = re.subn(tag_re("insert"), repl, page_code)
	if modif_count != 0:
		new_code = handle_custom_tags(new_code, page)
	return new_code

def file_content(file_path):
	return open(file_path, "r").read()

def handle_path_macros(page_code: str, page: Page) -> str:
	gen_path_from_home = pathlib.Path(page.path_gen).parts
	gen_path_to_home = "/".join([".."] * (len(gen_path_from_home)-1))
	return page_code.replace("HOME", gen_path_to_home)

## Page definition and generation

class Page:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		if "tab_name" not in self.__dict__:
			self.tab_name = self.name

page_list: List[Page] = [
	Page(
		name = "Home Page",
		tab_name = "Anima Libera",
		path_src = "src/template.html",
		path_gen = "gen/home.html",
		content = file_content("src/home.html"),
	),
	Page(
		name = "404 Page",
		path_src = "src/template.html",
		path_gen = "404.html",
		content = "Oh nyo, error 404 &gt;&lt;",
	),
	Page(
		name = "Tabs Page",
		path_src = "src/template.html",
		path_gen = "gen/tabs.html",
		content = file_content("src/tabs.html"),
	),
	Page(
		name = "Test Page",
		path_src = "src/template.html",
		path_gen = "gen/test.html",
		content = "awa ^^",
	),
]

# Clean up gen directory
if os.path.isdir("gen"):
	shutil.rmtree("gen")
os.mkdir("gen")

for page in page_list:
	print_indent(f"Generating \"{page.name}\" to {page.path_gen}")
	indent_push("| ")
	src_file = open(page.path_src, "r")
	src_code = src_file.read()
	src_file.close()

	gen_code = src_code
	gen_code = handle_custom_tags(gen_code, page)
	gen_code = handle_path_macros(gen_code, page)

	gen_file = open(page.path_gen, "w")
	gen_file.write(gen_code)
	gen_file.close()
	indent_pop()
