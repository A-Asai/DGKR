# Reference by Guruprasad Ananda's tool.
import os
import shutil
import sys


def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()


def main():
    outfile = sys.argv[1]
    infile = sys.argv[2]

    if len(sys.argv) < 4:
        shutil.copyfile(infile, outfile)
        sys.exit()

    cmdline = "paste %s " % (infile)
    for inp in sys.argv[3:]:
        cmdline = cmdline + inp + " "
    cmdline = cmdline + ">" + outfile
    try:
        os.system(cmdline)
    except Exception:
        stop_err("Error encountered with paste.")


if __name__ == "__main__":
    main()
