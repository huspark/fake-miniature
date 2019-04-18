## Fake Miniature
Fake-minature is a python program that manipulates various image properties in order to generate a miniature scene.

### How to Run
####usage
python3 main.py [-h] -f FILENAME [-s FILTER_SIZE] [-r FILTER_RADIUS] [-b BRIGHTEN_FACTOR] [-c SATURATE_FACTOR]

####required arguments:
  -f FILENAME, --filename FILENAME
                        the input file name

####optional arguments:
  -h, --help            show this help message and exit
  -s FILTER_SIZE, --filter_size FILTER_SIZE
                        the vertical size of each Gaussian filter in pixels
  -r FILTER_RADIUS, --filter_radius FILTER_RADIUS
                        the sigma value for the first Gaussian blur filter
  -b BRIGHTEN_FACTOR, --brighten_factor BRIGHTEN_FACTOR
                        the constant for a brightening effect
  -c SATURATE_FACTOR, --saturate_factor SATURATE_FACTOR
                        the constant for a saturation effect

### Sample Output Images
python3 main.py -f stadium.png -s 60 -r 1.003 -b 1.1 -c 1.5
<img src="/sample/stadium.png" width="48">
![alt text](/sample/stadium_out.png)

python3 main.py -f pool.jpeg -s 60 -r 1.3 -b 1.1 -c 1.5
![alt text](/sample/pool.jpeg)
![alt text](/sample/pool_out.jpg)

python3 main.py -f river.jpg -s 60 -r 1.3 -b 1.1 -c 1.5
![alt text](/sample/river.jpg)
![alt text](/sample/river_out.jpg)

### Citation
http://graphics.berkeley.edu/papers/Held-UBA-2010-03/Held-UBA-2010-03.pdf
