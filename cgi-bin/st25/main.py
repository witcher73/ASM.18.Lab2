from .group import group

def main(q, selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	group(q, selfurl).f()
