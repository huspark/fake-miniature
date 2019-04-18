## Fake Miniature
Fake-minature is a python program that manipulates various image properties in order to generate a miniature scene.  

<img src="/sample/stadium.png" width="420">
<img src="/sample/stadium_out.jpg" width="420">

### How to Run
* usage  
python3 main.py [-h] -f FILENAME [-s FILTER_SIZE] [-r FILTER_RADIUS] [-b BRIGHTEN_FACTOR] [-c SATURATE_FACTOR]  

* required arguments  
  * -f FILENAME, --filename FILENAME  
   the input file name  

* optional arguments  
  * -h, --help
   show this help message and exit  
  * -s FILTER_SIZE, --filter_size FILTER_SIZE  
   the vertical size of each Gaussian filter in pixels  
  * -r FILTER_RADIUS, --filter_radius FILTER_RADIUS  
   the sigma value for the first Gaussian blur filter  
  * -b BRIGHTEN_FACTOR, --brighten_factor BRIGHTEN_FACTOR  
   the constant for a brightening effect  
  * -c SATURATE_FACTOR, --saturate_factor SATURATE_FACTOR  
   the constant for a saturation effect  

### Citation
Using Blur to Affect Perceived Distance and Size,  
http://graphics.berkeley.edu/papers/Held-UBA-2010-03/Held-UBA-2010-03.pdf
