import random,re
from .common import integer,number,unique_ids

def name(x):
 if not isinstance(x,str)or not re.fullmatch('[a-z][a-z0-9_]{0,30}',x):raise ValueError('name')
 return x
def run(data):
 tables=data['tables'];unique_ids(tables);seed=integer(data.get('seed',0),0,2**53-1);rng=random.Random(seed);specs={name(t['id']):t for t in tables}
 if not 1<=len(tables)<=20 or sum(integer(t['count'],0,5000)for t in tables)>5000:raise ValueError('count')
 deps={}
 for t in tables:
  columns=t['columns']
  if not isinstance(columns,dict)or len(columns)>30:raise ValueError('columns')
  deps[t['id']]=set()
  for field,c in columns.items():
   if name(field)=='id':raise ValueError('reserved_id')
   if c['kind']=='foreign':
    parent=name(c['table'])
    if parent not in specs:raise ValueError('unknown_parent')
    deps[t['id']].add(parent)
   elif c['kind']=='integer':integer(c['minimum'],-10**9,10**9);integer(c['maximum'],c['minimum'],10**9)
   elif c['kind']=='category':
    if not isinstance(c['values'],list)or not c['values']or len(c['values'])>100 or any(not isinstance(x,str)for x in c['values']):raise ValueError('categories')
   else:raise ValueError('kind')
   number(c.get('null_probability',0),0,1)
 order=[];pending=set(specs)
 while pending:
  ready=sorted(t for t in pending if deps[t]<=set(order))
  if not ready:raise ValueError('dependency_cycle')
  order.extend(ready);pending.difference_update(ready)
 generated={};contracts=[]
 for table in order:
  t=specs[table];rows=[]
  for field,c in t['columns'].items():
   if c['kind']=='foreign':
    if t['count']and not generated[c['table']]and c.get('null_probability',0)!=1:raise ValueError('empty_parent')
    contracts.append({'table':table,'field':field,'references':[c['table'],'id']})
  for i in range(t['count']):
   row={'id':table+':'+str(i+1)}
   for field,c in sorted(t['columns'].items()):
    if rng.random()<c.get('null_probability',0):value=None
    elif c['kind']=='foreign':value=rng.choice(generated[c['table']])['id']
    elif c['kind']=='integer':value=rng.randint(c['minimum'],c['maximum'])
    else:value=rng.choice(c['values'])
    row[field]=value
   rows.append(row)
  generated[table]=rows
 return {'tables':generated,'foreign_keys':contracts,'generation_order':order,'seed':seed,'model':'seeded_declared_dag_primary_foreign_key_generation_not_private_data_learning'}
