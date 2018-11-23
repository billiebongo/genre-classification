2bd:


Things to do:

Do proper EDA
Scrape the numbers properly.... hm.
after scraping batches of 10, INSERT into db
put all the data in csv into database.
set up the database in the server
The number of the 


SCRAPER:

script to run scraper: indicate range of isbn to colelct on various sources: gbooks and greads
actually need to find all the shit and store in SQL.

Data cleaning
he 
Labelling: 
Rely on goodreads genres
Gbooks can be used to test data
Consolidate data


EDA: genres, top words in each genres

misclassified

Experiments:
- bag of words wordcount
- tfidf word count
- tfidf svm, NVB
-




data set 1: set2.csv
data set 2: need to empty DB and run scraper w better genre allocator.



check the set 2 csv for wrong column errors
HAND LABEL SHIT.
might have to empty database at the server and local before scraping new batch
id 4869,5266 is not english




2bd: set global variable to switch off from gbooks


ssh root@128.199.109.98


check results and continue for 10000 more books



Components:
- should actually time how long the isbn calling takes on avg
-

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
SELECT * INTO OUTFILE '/var/lib/mysql-files/33691.csv' FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM book;

sudo apt-get install python-pip python-dev libmysqlclient-dev

sudo systemctl status mysql
pip3 install configparser
ALTER TABLE book MODIFY COLUMN ID int NOT NULL AUTO_INCREMENT PRIMARY KEY (ID);
CREATE TABLE book ( book_title varchar(100), authors varchar(50), cover varchar(70), pub_year int, src varchar(2), genre varchar(20), description varchar(1000));
https://stackoverflow.com/questions/28973453/mysql2error-incorrect-string-value-xe2-x80-xa8-x09
#genre-classification

from local machine
cd /var/lib/mysql-files/
sudo scp root@128.199.109.98:/root/set3.tar.gz ~/Desktop
https://www.itworld.com/article/2833078/it-management/3-ways-to-import-and-export-a-mysql-database.html
https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost
https://stackoverflow.com/questions/40942061/changing-version-of-python-when-using-nohup
python3.6 -m pip install -r requirements.txt
https://stackoverflow.com/questions/1673530/error-2003-hy000-cant-connect-to-mysql-server-on-127-0-0-1-111
