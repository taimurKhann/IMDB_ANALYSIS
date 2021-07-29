# IMDB_ANALYSIS

### Requirement
* Docker Installed on system

### Libraries
Pandas

### How to run
* Open the terminal and Go to project folder\
    **cd IMDB_analysis**
* Run the below command\
    **docker build -t app_image .**
* Once image has been created run below command\
    **docker run --rm -it --entrypoint  bash app_image**
* Now you entered into the container, run below command to list all data\
    **ls -ltr**
* Run the main script\
    **python main.py**
* Once it is completed use below command to get result of each task in file\
    **cat Task1.tsv**\
    **cat Task2.tsv**
