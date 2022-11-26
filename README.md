# outfit-color
Image processing Team Project 02  
Outfit color analyzer using OpenCV technology.  

<img src = "readme_images/output/cdpd-1-person-walking_and_dancing.jpg" height = "300">
<img src = "readme_images/output/cdpd-2-women-walking.png" height = "300">

### Color of clothes
<img src = "readme_images/output/cdpd-zoom-1-person-walking_and_dancing.jpg" height = "300">

## Contents
1. [Environment Setup](#environment-setup)
2. [Demo](#demo)
3. [Key features we have focused on](#key-features-we-have-focused-on)

---
## Environment setup
This code has been tested on Ubuntu 16.04, Python 3.6, Pytorch 0.4.1, CUDA 9.2, RTX 2080 GPUs

- Clone the repository 
```
git clone git@github.com:JoeSeongchan/outfit-color.git && cd outfit-color
```
- Setup python environment
```
pip install -r requirements.txt
```
---
## Demo
- [Setup](#environment-setup) your environment
- Download video and put video file in 'videos' directory
- Run `demo.py`

```shell
cd src
python main.py ..\\videos\\{video_name}
```

## Key features we have focused on
### - Pedestrian detection
#### Input  
<img src = "readme_images/input/2-people-walking.jpg" height = "300">

#### Output  
<img src = "readme_images/output/pd-2-people-walking.jpg" height = "300"> 

### - Clothes color detection
#### Input
<img src = "readme_images/input/1-person-wearing_colorful_clothes.jpg" height = "300"> 

#### Output
<img src = "readme_images/output/cd-1-person-wearing_colorful_clothes.jpeg" height = "300"> 

> - video source: https://www.youtube.com/watch?v=tB-0oWBuK7A
> 
> - image source: https://www.gq.com/story/why-normal-ass-clothes-are-the-best-way-to-dress-right-now
> 
