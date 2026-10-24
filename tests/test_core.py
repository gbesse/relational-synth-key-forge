import unittest,sqlite3
from relational_synth_key_forge import run
class Tests(unittest.TestCase):
 def data(self):return {'seed':3,'tables':[{'id':'parent','count':3,'columns':{}},{'id':'child','count':100,'columns':{'parent_id':{'kind':'foreign','table':'parent'}}}]}
 def test_actual_sqlite_foreign_key_check(self):
  r=run(self.data());db=sqlite3.connect(':memory:');db.execute('PRAGMA foreign_keys=ON');db.execute('CREATE TABLE parent(id TEXT PRIMARY KEY)');db.execute('CREATE TABLE child(id TEXT PRIMARY KEY,parent_id TEXT REFERENCES parent(id))');db.executemany('INSERT INTO parent VALUES(?)',[(x['id'],)for x in r['tables']['parent']]);db.executemany('INSERT INTO child VALUES(?,?)',[(x['id'],x['parent_id'])for x in r['tables']['child']]);self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(),[]);db.close()
 def test_table_declaration_order_does_not_change_generation(self):
  d=self.data();a=run(d);d['tables'].reverse();self.assertEqual(run(d),a)
 def test_cycle_and_empty_required_parent_rejected(self):
  d=self.data();d['tables'][0]['columns']={'child_id':{'kind':'foreign','table':'child'}}
  with self.assertRaises(ValueError):run(d)
  d=self.data();d['tables'][0]['count']=0
  with self.assertRaises(ValueError):run(d)
 def test_all_null_foreign_key_on_empty_parent_is_explicit(self):
  d=self.data();d['tables'][0]['count']=0;d['tables'][1]['columns']['parent_id']['null_probability']=1;self.assertTrue(all(x['parent_id']is None for x in run(d)['tables']['child']))
