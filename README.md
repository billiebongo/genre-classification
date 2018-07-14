Status: commented gbooks API
Third run
used amyyytannn creds


2bd: set global variable to switch off from gbooks

2BD:



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
sudo apt-get install python-pip python-dev libmysqlclient-dev

sudo systemctl status mysql
pip3 install configparser
ALTER TABLE book MODIFY COLUMN ID int NOT NULL AUTO_INCREMENT PRIMARY KEY (ID);
CREATE TABLE book ( book_title varchar(100), authors varchar(50), cover varchar(70), pub_year int, src varchar(2), genre varchar(20), description varchar(1000));
https://stackoverflow.com/questions/28973453/mysql2error-incorrect-string-value-xe2-x80-xa8-x09
#genre-classification

https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost
https://stackoverflow.com/questions/40942061/changing-version-of-python-when-using-nohup
https://stackoverflow.com/questions/42662104/how-to-install-pip-for-python-3-6-on-ubuntu-16-10
https://stackoverflow.com/questions/1673530/error-2003-hy000-cant-connect-to-mysql-server-on-127-0-0-1-111