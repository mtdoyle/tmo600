# Prereqs

1. install these python modules:

	* Just for running the 600 finder:
	 	* pip install pika pymysql
	* For running the coordinate trimmer (only works on OSX and linux):
		* pip install fiona shapely 

2. Install docker:
	* https://www.docker.com

3. Download and run MySQL and RabbitMQ containers:
	* docker run -d --hostname tmorabbit --name tmorabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management
	* docker run --name tmomysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql

4. Download a mysql brower, such as mysql explorer


# Database setup

1. run 'python create\_db.py'
2. OPTIONAL: if you want to create your own coordinate set:
	* run 'python create\_table\_coords.py'

# Load coordinates into RabbitMQ
1. run 'python load\_rabbitmq.py'

# Run the 600Mhz checker
1. run 'python tmo600\_worker.py'
	* this can be ran multiple times on the same machine or multiple machines. If running on a different machine than your docker server, change the IP address from either 'localhost' or '127.0.0.1' to the IP address of the docker host machine.
2. wait a few hours for it to run
	* You can check how many coordinates are left by logging into the RabbitMQ gui:
		* http://localhost:8080
		* user: guest
		* pass: guest
		* nagivate to the "queue" tab
			* the "ready" column is how many coordinates are remaining to be checked
3. Open your sql editor and get your results. A sample command to see the results:
	* select * from tmo600.tmo600
4. Export the results to CSV format (google it)
5. Load the csv into a google map (google it)
