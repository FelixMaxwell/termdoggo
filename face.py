from curses import wrapper
import curses

class FacePart:
	def __init__(self, x, y, buf):
		self.x = x
		self.y = y
		self.buf = buf
		self.children = {} 
		self.visible = True

	def write(self, scr, xo=0, yo=0):
		if not self.visible: return

		yoff = self.y + yo
		xoff = self.x + xo

		for i in range(len(self.buf)):
			for j in range(len(self.buf[i])):
				if self.buf[i][j] != " ":
					scr.addch(yoff + i, xoff + j, self.buf[i][j])

		for _, c in self.children.items():
			c.write(scr, xoff, yoff)

	def __setitem__(self, name, child):
		self.children[name] = child

	def __getitem__(self, name):
		return self.children[name]

def main(stdscr):
	stdscr.clear()
	curses.curs_set(False)

	p = FacePart(5, 5, ['###########', '#         #', '# __   __ #', '#    #    #', '#         #', '#  #####  #', '#         #', '###########'])
	p["l"] = FacePart(2,2,["##"])
	p["r"] = FacePart(7,2,["##"])
	p["mouth"] = FacePart(2,4, ["#     #"])

	while True:
		stdscr.clear()
		p.write(stdscr)
		stdscr.refresh()

		k = stdscr.getch()
		if k == curses.KEY_LEFT:
			p.x -= 1
		elif k == curses.KEY_RIGHT:
			p.x += 1
		elif k == curses.KEY_UP:
			p.y -= 1
		elif k == curses.KEY_DOWN:
			p.y += 1
		elif k == ord("b"):
			p["l"].visible = not p["l"].visible
			p["r"].visible = not p["r"].visible
		elif k == ord("l"):
			p["l"].visible = not p["l"].visible
		elif k == ord("r"):
			p["r"].visible = not p["r"].visible
		elif k == ord("w"):
			p["mouth"].y -= 1
		elif k == ord("s"):
			p["mouth"].y += 1
		else:
			break

wrapper(main)
