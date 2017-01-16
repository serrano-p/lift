import platform
import os
import subprocess

operating_system = platform.system()

database = 3
#database = int(raw_input("Choose DB (1 for MonetDB, 2 for CouchDB or 3 for both): "))

def executeCmd(cmd):
	#process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	#process.wait()
	#p = subprocess.Popen(cmd.split())
	#wait(p)
	p = os.system(cmd)

if database == 1 or database == 3:

	if operating_system == "Linux":


		print("installation monetdb sql client")

		codeName = os.popen("lsb_release -c").read()

		executeCmd("sudo touch /etc/apt/sources.list.d/monetdb.list")

		f = open('/etc/apt/sources.list.d/monetdb.list', 'w')

		if "trusty" in codeName:
			f.write( "%s \n %s" % ("deb http://dev.monetdb.org/downloads/deb/ trusty monetdb", 
				         "deb-src http://dev.monetdb.org/downloads/deb/ trusty monetdb"))

			f.close()
		if "precise" in codeName:
			f.write("%s \n %s" % ("deb http://dev.monetdb.org/downloads/deb/ precise monetdb", 
				         "deb-src http://dev.monetdb.org/downloads/deb/ precise monetdb"))

			f.close()
		if "vivid" in codeName:
			f.write("%s \n %s" % ("deb http://dev.monetdb.org/downloads/deb/ vivid monetdb", 
				         "deb-src http://dev.monetdb.org/downloads/deb/ vivid monetdb"))

			f.close()
		if "jessie" in codeName:
			f.write("%s \n %s" % ("deb http://dev.monetdb.org/downloads/deb/ jessie monetdb", 
				         "deb-src http://dev.monetdb.org/downloads/deb/ jessie monetdb"))

			f.close()
		if "utopic" in codeName:
			f.write("%s \n %s" % ("deb http://dev.monetdb.org/downloads/deb/ utopic monetdb", 
				         "deb-src http://dev.monetdb.org/downloads/deb/ utopic monetdb"))

			f.close()

		executeCmd("wget --output-document=- https://www.monetdb.org/downloads/MonetDB-GPG-KEY | sudo apt-key add -")
		executeCmd("sudo apt-get install monetdb5-sql monetdb-client")

		f = open('~/.monetdb', 'w')
		f.write("%s \n %s \n %s" % ("user=monetdb", 
	         	"password=monetdb", "language=sql"))
		f.close()

		executeCmd("export DOTMONETDBFILE=~/.monetdb")
	
		f = open('~/.bashrc', 'a+')
		f.write("%s" % ("export DOTMONETDBFILE=~/.monetdb"))
		f.close()

	if operating_system == "Darwin":

		print("installation monetDB")

		executeCmd("xcode-select --install")
		executeCmd("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
		executeCmd("brew install monetdb")
		executeCmd("brew install wget")

		f = open(os.path.expanduser('~/.monetdb'), 'w+')
		f.write("%s\n%s\n%s" % ("user=monetdb", "password=monetdb", "language=sql"))
		f.close()

		f = open(os.path.expanduser('~/.bashrc'), 'a+')
		f.write("export DOTMONETDBFILE=~/.monetdb")
		executeCmd("source ~/.bashrc")
		f.close()
	
	executeCmd("monetdbd create $HOME/myMONETDB")
	executeCmd("sudo chmod 777 -R  $HOME/myMONETDB")
	executeCmd("monetdbd start $HOME/myMONETDB")
	executeCmd("monetdb create demo")
	executeCmd("monetdb release demo")

	f = open('test.sql', 'w')

	f.write( "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %("CREATE USER \"feta\" WITH PASSWORD 'feta' NAME 'FETA Explorer' SCHEMA \"sys\";", 
		"CREATE SCHEMA \"feta\" AUTHORIZATION \"feta\";",
		"ALTER USER \"feta\" SET SCHEMA \"feta\";",
		"CREATE TABLE test (id int, data varchar(30));", 
		"INSERT INTO test VALUES (2, 'geard');", 
		"SELECT * from test;", 
		"CREATE TABLE feta.test2 (id int, data varchar(30));",
		"INSERT INTO feta.test2 VALUES (2, 'geard');",
		"SELECT * from feta.test2;"))
	
	f.close()

	print("end write test.sql")
	executeCmd("mclient -d demo -u monetdb  < test.sql")

if database == 2 or  database == 3:

	print(operating_system)
	if operating_system == "Linux":
		executeCmd("sudo apt-get install couchdb -y")
		executeCmd("curl localhost:5984")

	if operating_system == "Darwin":

		print("installation coucdhDB")
		executeCmd("wget https://dl.bintray.com/apache/couchdb/mac/1.6.1/Apache-CouchDB-1.6.1.zip")
		executeCmd("unzip Apache-CouchDB-1.6.1.zip")
		executeCmd("chmod 777 -R Apache\ CouchDB.app")
		executeCmd("sudo mv  Apache\ CouchDB.app /Applications")


if operating_system == "Linux":

	print("installation justinfer")
	executeCmd("sudo add-apt-repository ppa:oreste-notelli/ppa")
	executeCmd("sudo apt-get install justniffer")

if operating_system == "Darwin":
	print("Install Justniffer")

	executeCmd("brew install homebrew/dupes/gpatch")
	executeCmd("brew update")
	executeCmd("brew install elementary")
	executeCmd("brew update")
	#executeCmd("brew install png++")
	executeCmd("brew tap homebrew/versions")
	executeCmd("brew install gcc48")
	executeCmd("brew update")
	executeCmd("brew install patch")
	executeCmd("brew update")
	executeCmd("brew install tar")
	executeCmd("brew update")
	executeCmd("brew install autotools")
	executeCmd("brew update")
	executeCmd("brew install make")
	executeCmd("brew update")
	executeCmd("brew install patch")
	executeCmd("brew update")
	executeCmd("brew install libc6")
	executeCmd("brew update")
	executeCmd("brew install libpcap0.8")
	executeCmd("brew update")
	#executeCmd("brew install g++")
	executeCmd("brew update")
	executeCmd("brew install libboost-iostreams")
	executeCmd("brew update")
	executeCmd("brew install libboost-program-options")
	executeCmd("brew update")
	executeCmd("brew install libboost-regex")
	executeCmd("brew update")

	executeCmd("wget https://sourceforge.net/projects/justniffer/files/justniffer_0.5.14.tar.gz")
	#executeCmd("unzip justniffer_0.5.14.tar.gz")
	#executeCmd("chmod 777 -R justniffer_0.5.14.tar.gz")
	#executeCmd("gunzip -c justniffer_0.5.14.tar.gz")
	executeCmd("gunzip -c justniffer_0.5.14.tar.gz | tar xopf -")
	# Warning: "_" replaced by "-" in the unzipped directory
	justnifferDirectory = "cd justniffer-0.5.14 && "
	executeCmd(justnifferDirectory + "autoreconf --install")
	executeCmd(justnifferDirectory + "./configure")
	executeCmd(justnifferDirectory + "make")
	executeCmd(justnifferDirectory + "sudo make install")