#!/bin/bash

set -e
#
# create_ptf_tests.sh
#
# Usage:
#     create_ptf_tests.sh <program_name>
#
# This simple utility populates a given directory with the templates from
# ~/tools and slightly customizes them.
#
# It creates 3 files:
#    1. p4_program_test.py is copied from ~/tools
#    2. <program_name>.py  is the template for the base test class for a given
#                          program. The user is supposed to specify the tables
#                          they plan to manipulate/clear as well as the
#                          field annotations
#    3. test.py            is a template for a very first test
#

TEMPLATE_DIR=~/tools/ptf-template

help() {
    cat <<EOF
Usage:
    $0 <program_name>

This simple utility populates a given directory with the templates from
$TOOLS and slightly customizes them.

It creates 3 files:
   1. p4_program_test.py is copied from ~/tools
   2. <program_name>.py  is the template for the base test class for a given
                         program. The user is supposed to specify the tables
                         they plan to manipulate/clear as well as the
                         field annotations
   3. test.py            is a template for a very first test
   4. README.md          is a simple explanation file

EOF
}

main() {
    PROG=$1

    cp $TEMPLATE_DIR/p4_program_test.py .
    PROG=$PROG envsubst < $TEMPLATE_DIR/program_template.py  > ./${PROG}.py
    PROG=$PROG envsubst < $TEMPLATE_DIR/test_template.py     > ./test.py
    TOOL=$0 PROG=$PROG envsubst < $TEMPLATE_DIR/README.md    > ./README.md
}

if [ $# != 1 ]; then
    help
    exit 1
fi

if [ -z `which envsubst` ]; then
    cat <<EOF
ERROR: envsubst utility cannot be found
       Please, install it first, e.g.:
            apt install gettext-base 
EOF
fi

main $1
