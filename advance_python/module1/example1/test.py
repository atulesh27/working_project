def cred():
    username = "admin"
    password = "admin@123"
    port = 3306
    dbname = "test.db"
    return username,password,port,dbname

def db_connection(username,password,port,dbname):
    print("connection db ..")
    print(f"with {dbname},username :: {username} ,password::{password}, port ::{port}")
    return True


def data_process():
    print("data processing ")

def dbdump():
    print("dump....")

#driver code

def main():
   u,p,port,dbn = cred()
   status = db_connection(u,p,port,dbn)
   if status:
       print("db connection successfull")
   else:
       print("db not connected ")

data_process()

dbdump()

if __name__ == "__main__":
    main()