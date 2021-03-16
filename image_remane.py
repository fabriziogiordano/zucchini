import os
import uuid

def rename(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in files:
        print(f)
        # u = uuid.uuid4().urn[9:]
        # f_from = os.path.join(directory, f)
        # f_to = os.path.join(directory, u) + '.jpg'
        # os.rename(f_from, f_to)
        # os.system('ls -l')
        e = f'convert ./images/original/{f} -density 72 -units PixelsPerInch -resize 800x600 -gravity center -background black -compress jpeg -extent 800x600 ./images/converted/{f}'
        print(e)
        os.system(e)


if __name__ == '__main__':
    rename('./images/original/')