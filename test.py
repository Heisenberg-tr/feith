def texter(text):
	fadeble = ""
	for line in text.splitlines():
	for character in line:
		fadeble += (f"\033[38;2;{50};{50};{50}m{character}\033[0m")
		fadeble += "\n"
		return fadeble

test_text = """
████████╗███████╗███████╗████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
   ██║   █████╗  ███████╗   ██║   
   ██║   ██╔══╝  ╚════██║   ██║   
   ██║   ███████╗███████║   ██║   
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
"""

print(texter(test_text))


