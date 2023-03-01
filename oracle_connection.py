import cx_Oracle

def dbConnect():
    dsn_tns = cx_Oracle.makedsn('192.168.16.1', '1521', service_name='ectdb')
    conn = cx_Oracle.connect(user='ECT_MC', password='qwerty', dsn=dsn_tns)
    c = conn.cursor()
    
    return c, conn


def machinelist():
    c, conn = dbConnect()
    sql = "SELECT MACHINE_CODE, MACHINE_NAME, MACHINE_LABEL_NO from MACHINE_LIST where MACHINE_SECTION='IN' and MACHINE_TYPE=2 Order By MACHINE_CODE DESC"
    c.execute(sql)
    
    row_data=[]
    for row in c:
        row_data.append(row)
    conn.close()
    return row_data

def machineCount():
    c, conn = dbConnect()
    c.execute('select * from MACHINE_LIST')
    
    row_data=[]
    for row in c:
        row_data.append(row)
    conn.close()
    return len(row_data)
    

#print(machineCount())

def lotCode(code):
    c, conn = dbConnect()
    sql = "SELECT a.LOT_NO , b.product_name FROM ECT_MC.CONTROL_LOT2 a, ECT_MC.PRODUCT b  WHERE  a.PRODUCT_ID = b.ID AND a.CONTROL_NO = '{}'".format(code)
    c.execute(sql)
    
    row_data=[]
    for row in c:
        row_data.append(row)
    conn.close()
    return row_data[0]
    
def machine_name(mcid):
    c, conn = dbConnect()
    sql = "select MACHINE_NAME, MACHINE_LABEL_NO from MACHINE_LIST where MACHINE_CODE = {}".format(mcid)
    c.execute(sql)
    
    row_data=[]
    for row in c:
        row_data.append(row)
        
    conn.close()
    return row_data[0]