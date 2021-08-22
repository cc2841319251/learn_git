import jaydebeapi
import configparser


class Db_connect():
    def __init__(self, filename, section):
        conf = configparser.ConfigParser()
        conf.read(filename)
        url = conf.get(section, 'url')
        username = conf.get(section, 'username')
        pwd = conf.get(section, 'pwd')
        driver = conf.get(section, 'driver')
        jarFile = conf.get(section, 'jarFile')
        try:
            self.con = jaydebeapi.connect(driver, url=url, driver_args=[username, pwd], jars=jarFile)
            self.cur = self.con.cursor()
        except Exception as e:
            print('连接失败，失败的原因是%s' % e)
            self.con.close()

    def select_sql(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            print('查询失败，失败的原因是%s' % e)

    def insert_or_update_or_delete_sql(self, sql):
        try:
            self.cur.execute(sql)
            self.cur.execute('commit')
        except Exception as e:
            print('执行失败，失败的原因是%s' % e)
            self.cur.execute('rollback')


Db_connect('datbase.conf', 'OracleDb')
