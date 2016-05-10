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


import difflib
import pdb

class bugsearcher(object):
	"""Used by debug.py to perform a binary search for memory related bugs.
	LEG tries lockstepping at various step counts after a given address.
	The instruction at which the resulting bug changes indicates the source
	of the current bug.
	"""
	
	def __init__(self):
		self.created = True

	def isEqLockstepOutput(self, a, b):
		"""Compare two lockstep outputs to determine if the bugs detected
		are the same"""
		eqDiff = 23 # Threshold for a output being the same

		a = a.splitlines(1)
		b = b.splitlines(1)

		# Diff the two lockstep outputs
		difflist = []
		diff = difflib.unified_diff(a,b)
		for line in diff:
			difflist.append(line)

		ignorelist = ['\n', ' \n']
		filtered = [x for x in difflist if x not in ignorelist]

		if(len(filtered) < eqDiff):
			return True
		
		return False		
