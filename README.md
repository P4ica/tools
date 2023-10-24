# Intel Connectivity Academy tools by P4ica

This directory contains a set of tools created for Intel Connectivity Academy
Students. mostly keep them in the same directory with minimal hierarchy for
the ease of use and installation.

Below are some descriptions.

## ba-labs-set-resolution.sh

Usage: `sudo ~/tools/ba-labs-set-resolution.sh <x-resolution>x<y-resolution>`

This script allows you to set the desired resolution for your Xvnc desktop,
since it does not change itself automatically when you resize your  browser
window. Instead, the image is scaled to fit the window.

We recommend using the full-screen mode for the browser window and set the
resolution to the native resolution of your monitor.

You need to do it only once -- the setting is preserved between the VM reboots.

## bfrt_python.sh (also bfrt_python.py and bfrt_clear_all.py)

Usage: `~/tools/bfrt_python.sh`

This script invokes `bfrt_python` (obviously, you need to have the user-space
driver process, `bf_switchd` running), but with a "twist" -- it "sources" the
file `bfrt_python.py` before switching to the interactive mode.

This allows the developer (who gets in the habit of using this tool) to easily
extend `bfrt_python` with new commands and utilities. As an example, this file
pulls in (imports) `bfrt_clear_all.py` that implements `clear_all` command. This
command safely clears all the tables and it pretty elaborate to implement.

## bfrt_starter.py

Usage: `~/tools/bfrt_starter.py`

This is the minimal script that demonstrates how to connect to a running 
BF Runtime gRPC server using `bfrt_grpc.client` module. 

The script itself is not doing much, but you should be easily extend it and create your own Python-based control plane prototypes easily.

## clean_sde.sh

Usage: `cd $SDE; ~/tools/clean_sde.sh`

This simple script removes log files from the SDE root directory so that it
looks "clean"

## create_ptf_tests.sh (and ptf-template directory)

Usage: `~/tools/create_ptf_tests.sh <program_name>`

This program creates creates a PTF test template (described in ICA-XFG-101
course) ready to be filled in with the actual content.

## dummy*

These files allow the developers to create (and destroy) dummy network
interfaces and properly connect them to the model and PTF tests. Using these
interfaces is more efficient compared to Virtual Ethernet (veth) ones and they
have fewer bugs. They also have a more consistent naming.

TBC
