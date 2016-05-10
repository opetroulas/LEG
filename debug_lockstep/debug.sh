#!/bin/bash

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

COMMAND="['interactive']"
noirq="false"
dump="false"
dumpdir=""
js_cmd=""
js="false"

while [[ $# > 0 ]]
do
key="$1"

case $key in
	-t|--test)
	TESTFILE="$2"
	shift # past argument
	;;
	-a|--auto)
	COMMAND="['autorun']"
	;;
	--bugcheckpoint)
	COMMAND="['bugcheckpoint', '$2', '$3']"
	shift # past argument
	shift # past argument
	;;
	-d|--dump)
	dump="true"
	dumpdir="$2"
	shift
	;;
	-js)
	js="true"
	js_cmd="$2"
	shift
	;;
	--divideandconquer)
	COMMAND="['divideandconquer', '$2', $3, $4"
	if [ "$dump" = "true" ]; then
		COMMAND="$COMMAND, '--dump', '$dumpdir'"
	fi
	if [ "$noirq" = "true" ]; then
		COMMAND="$COMMAND, '--noirq'"
	fi
	if [ "$js" = "true" ]; then
		COMMAND="$COMMAND, '-js', '$js_cmd'"
	fi
	COMMAND="$COMMAND]"
	shift # past argument
	shift # past argument
	shift # past argument
		# COMMAND="['divideandconquer', '$2', $3, $4, '--dump', '$dumpdir', '--noirq']"
	;;
	--noirq)
	noirq="true"
	;;
	-h|--help)
	echo "Usage:"
	echo "  -t TEST, --test TEST             Load a test (.bin) from the given path"
	echo "  -a, --auto                       Automatically run the test noninteractively"
	echo "  --dump, --dump [file]			 Dump qemu state to file for loading in modelsim"
	echo "  -stepm [n]			 		 	 Step n instructionc before lockstepping"
	echo "  --noirq 						 Run test with IRQ interrupts disabled"
	# Hidden option:
	# echo "  --bugcheckpoint BUGFILE DEST   Automatically create a checkpoint for BUGFILE."
	# echo "  --divideandconquer RUNDIR START END   Automatically run a divide-and-conquer section from START to END"
	exit 0
	;;
	*)
	echo "Unknown option: $key"
	exit 1
	;;
esac
shift # past argument or value
done

source configuration.py

# UNCOMMENT THIS FOR LEG DISTRIBUTION
PYTHONPATH=./ \
	$gdb_path/arm-none-eabi-gdb-py -q \
	-ex "python TEST_FILE=\"$TESTFILE\"" \
	-ex "python COMMAND=$COMMAND" \
	-x debug.py

rm transcript
