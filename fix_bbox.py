def fix_bbox(file):

    import subprocess
    
    subprocess.call(['epstool --quiet --copy --bbox '+file+' temp.eps'], shell=True)
    subprocess.call(['rm '+file], shell=True)
    subprocess.call(['mv temp.eps '+file], shell=True)


if __name__ == "__main__":

    import sys

    fix_bbox(sys.argv[1])