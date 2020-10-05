#ref: https://www.youtube.com/watch?v=swU3c34d2NQ
# It use to configure log messages from an application
def logger(msg):
    def log_msg():
        print("Log: ", msg)
    print(log_msg)
    return log_msg


log_hi = logger("hi")
print(log_hi)
log_hi()

#2nd Example.. log_message also called closure function


def html_tag(tag):
    def log_message(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return log_message


H1 = html_tag("h1")
H1("I am h1 tag")

H2 = html_tag("h2")
H2("I am h1 tag")

P = html_tag("p")
P("I am paragraph")
