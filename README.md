2bd:

Steps:
- get more data. run scraper. set up DB?
    - 
- run more models. make pipelines. try all methods
- word embeddings
-neural networks
-research for other types.

Things to do:

Do proper EDA
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






check the set 2 csv for wrong column errors
HAND LABEL SHIT.
might have to empty database at the server and local before scraping new batch
id 4869,5266 is not english




Trivial to do list: 
Log errors from scraper D:

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

Delete rows with dupe col value book_title
DELETE t1.*
FROM
  book t1 INNER JOIN (SELECT book_title
                           FROM book
                           GROUP BY book_title
                           HAVING COUNT(*)>1) t2
  ON t1.book_title = t2.book_title;

DAtabase commands:
mysql -u root -p
SELECT * INTO OUTFILE '/var/lib/mysql-files/run2.csv' FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM book;
DEC 2018: SELECT *
FROM book
INTO OUTFILE '/var/lib/mysql-files/dec2018.csv'
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
sudo apt-get install python-pip python-dev libmysqlclient-dev



sudo systemctl status mysql
pip3 install configparser
ALTER TABLE `book` ADD COLUMN `id` INT AUTO_INCREMENT UNIQUE FIRST;
ALTER TABLE book MODIFY COLUMN ID int NOT NULL AUTO_INCREMENT PRIMARY KEY (ID);
CREATE TABLE book ( book_title varchar(120), authors varchar(60), cover varchar(100), pub_year int, src varchar(2), genre varchar(20), description varchar(1500));
https://stackoverflow.com/questions/28973453/mysql2error-incorrect-string-value-xe2-x80-xa8-x09
#genre-classification

from local machine
cd /var/lib/mysql-files/
sudo scp root@128.199.109.98:/root/genre-classification/90k.csv .
https://www.itworld.com/article/2833078/it-management/3-ways-to-import-and-export-a-mysql-database.html
https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost
https://stackoverflow.com/questions/40942061/changing-version-of-python-when-using-nohup
python3.6 -m pip install -r requirements.txt
https://stackoverflow.com/questions/1673530/error-2003-hy000-cant-connect-to-mysql-server-on-127-0-0-1-111


45734
remove books wirth desc == NaN
Index(['id', 'book_title', 'authors', 'pub_year', 'genre', 'description',
       'desc_word_count'],
      dtype='object')
39222 -> 6000 books have no descriptions
