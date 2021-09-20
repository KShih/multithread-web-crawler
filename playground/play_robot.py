import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
robot_url = "https://www.nyu.edu/robots.txt"
url = "https://www.nyu.edu/giving/give-now/?cid=1000102"

rp.set_url(robot_url)
rp.read()
print(rp.can_fetch("*", url))