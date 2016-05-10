# LEG Processor for Education
# Copyright (C) 2016  Max Waugaman

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ./debug.sh
# python-interactive
# import prepare_divide_conquer
# prepare_divide_conquer.go_dump()

import gdb, re, math
import qemu_monitor

def getFnName():
	return gdb.selected_frame().name()

def go():
	gdb.execute('add-symbol-file ~/nvmlx 0x18000')
	gdb.execute('add-symbol-file ~/nvmlx 0x5a5880')
	gdb.execute('set pagination off')
	gdb.execute('set logging on')
	gdb.execute('rbreak .')
	gdb.execute('enable once 1-$bpnum')
	states = [];
	try:
		while True:
			instrct = qemu_monitor.getQemuInstrCt()
			pc = qemu_monitor.getQemuPC()
			fnname = getFnName()
			states.append([instrct, pc, fnname])
			print "{} instructions: 0x{:x} ({})".format(instrct, pc, fnname)
			cont_str = gdb.execute("continue", to_string=True)
			if "SIGINT" in cont_str:
				break
	except KeyboardInterrupt:
		pass
	print "DONE!"
	return states

states = None
def go_dump():
	global states
	states = go()
	import cPickle as pickle
	pickle.dump(states, open('output/divide_conquer_states.pickle','w'))