from mysql.connector import MySQLConnection, Error

hostname = 'localhost'
username = 'root'
password = 'Rese@rch2020'
database = 'gestion_spe'


class ADO(object):

    def __init__(self):
        try:
            self.conn = MySQLConnection(host=hostname, user=username, passwd=password, db=database)
            self.cursor = self.conn.cursor()
            print("Successful connection...")
        except Error as e:
            print(e)

    def query(self, sql: str):
        try:
            self.cursor.execute(sql)
            data_result = self.cursor.fetchall()
            return data_result
        except Error as e:
            print(e)
        finally:
            self.cursor.close()
            self.conn.close()
            print("Close connection")

    def dml(self, sql: str, val: str):
        try:
            result = "Insert Successful"
            self.cursor.execute(sql, val)
            self.conn.commit()
            if self.cursor.rowcount is None:
                result = "Insert Problem"
            return result
        except Error as e:
            print(e)
        finally:
            self.cursor.close()
            self.conn.close()
            print("Close connection")


if __name__ == '__main__':
    con = ADO()
    result = con.query("SELECT idperson, name, last_name FROM gestion_spe.person")
    print(result)




