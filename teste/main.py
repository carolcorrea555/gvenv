import oracledb
import config

sql = 'SELECT ID, '\
    'XMLTYPE(req.REQUESTXML).EXTRACT(\'//Application/creditApplication/applicationNumber/text()\').getStringVal()'\
        'as applicationNumber'\
    'FROM T1_OS_ADMIN.OSUSR_D69_GMFDMREQ req'

try:
    with oracledb.connect(
        user=config.username,
        password=config.password,
        host=config.host,
        port=config.port,
        service_name=config.service_name,
        encoding=config.encoding
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                print(row)

except oracledb.Error as error:
    print("There was an error .o.")
    print(error)