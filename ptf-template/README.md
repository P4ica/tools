This directory contains PTF tests for the program $PROG

It has been created using the command

        ${TOOL} ${PROG}

It contains the following files:

1. `README.md` -- this file
2. `p4_program_test.py` -- the file that contains `P4ProgramTest` class that is rescribed in ICA classes and is derived from the standard `BfRuntimeTest` class provided by the SDE
3. `${PROG}.py` -- the file that contains `BaseProgramTest` class derived from `P4ProgramTest`. This file (and the class in it) should be customized for your pwn program. That's where you can specify "shortcut" names for the tables, turn on annotations, etc.
4. `test.py` -- this file contains a template for an individual test. It does nothing, but shows what typically goes in there. You can put as many test classes as you want into one file or you can have multiple files with multiple test cases in them

Obviously, the customization can be very extensive -- this is just a simple starter.
