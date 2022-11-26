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
This code has been tested on Windows 11, Python 3.10, Pycharm 2022.2.4 (Community), Vscode 1.73.0

- Clone the repository 
```
git clone git@github.com:JoeSeongchan/outfit-color.git && cd outfit-color
```
- Setup python environment
```
python -m venv venv
cd .\\venv\\Scripts
.\activate
cd ..
cd ..
pip install -r requirements.txt
```

If you want to run the code in windows + VsCode environment use the comment-out-ed codes in the 'main.py'
```
""" If you are using Windows + Vscode, enable comments in below ..."""
# if (len(sys.argv)-1) != 1:
#     print("Please feed the file path you want to run")
# video_path = sys.argv[1]
# print(video_path)
"""                        Windows + Vscode                        """
```
and add...
```
"args": ["\\\\videos\\\\1-person_walking.mp4"],
```
to the 'launch.json' file.
which can be easily made by 'Run and Debug' sidebar (ctrl+shift+D)

---
## Demo
- [Setup](#environment-setup) your environment
- Download video and put video file in 'videos' directory
- Run `demo.py`

```shell
cd src
python main.py "..\\videos\\{video_name}"
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
