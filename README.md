2BD:

Components:
- scrape API and store in DB
    - NLB

- preprocess data (clean and assign genre) and store in separate table BOOK(id, title, genre, )
-


- ensure all english
- preprocess data
- not call gbook if no cover
- make sure keys are the same!


first 5000: range(1250107814, 1250740000):

Book Cover Dataset
https://github.com/uchidalab/book-dataset

Book_cover and title:
http://cs229.stanford.edu/proj2015/127_report.pdf

DAtabase commands:
mysql -u root -p
sudo apt-get install python-pip python-dev libmysqlclient-dev

sudo systemctl status mysql
pip3 install configparser
ALTER TABLE book MODIFY COLUMN ID int NOT NULL AUTO_INCREMENT PRIMARY KEY (ID);


#genre-classification
