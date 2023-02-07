from hcl_database_connection import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        custid=2
        sql="delete from customer where idcustomer=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=HclPythonTransaction()
connect_obj.connect("localhost","root","SALEEMasha@7","yasmin")
connect_obj.execute_transaction_query()