# jpg_msg

jpg_msg is a small in python written commandline utility to write and read messages to and from jpg files without manipulating the picture

# how does it work?
jpg files start with the two bytes FF D8 (here in hex) and end with FF D9 (also in hex). All image programms process the image file till the end bytes wich don't occure in the main part. After that byte sequenz normal programms stop. If we add data after that particular sequenz we dont change the content of the original image and it would be displayed normally, but with additional data attatched.

# how to use the utility 
- arguments
  - -a 
