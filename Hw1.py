import pandas as pd
import vertica_python as vp
from verticapy.utilities import pandas_to_vertica as ptv

path = r'C:\Users\Ярослав\Desktop\Python\Practicum\Genesis\sandbox.KNU'
df = pd.read_csv(path + r'\dictionary\context.tsv', sep='\t')

conn_cluster = {
    'host': "localhost",
    'port': 5433,
    'user': 'dbadmin',
    'password': 'pass',
    'database': 'VMart'
}

with vp.connect(**conn_cluster) as connection:
    cur = connection.cursor()
    ptv(df=df, name='context', cursor=cur, schema='product')
    cur.close()
