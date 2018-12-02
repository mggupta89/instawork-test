Requirements
  -Python 3.7
  -Mysql server up and running
  -pip3

Create a database
Set db properties in db.cnf file

Run these commands in terminal (directory should be set root folder of this project)
    pip3 install -r requirements.txt
    python3 manage.py migrate team
    python3 manage.py runserver

Not required, but to test I am using postman
Import Instawork.postman_collection.json into postman workspace
Execute the collection to see the results

Note:
   Tests are not written
   Have not setup docker.