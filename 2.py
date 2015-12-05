from __future__ import print_function, unicode_literals, division
# {'party': 'FIDESZ,KDNP', 'MP ID': '657', 'net_amount': '718000.0', 'MP name': 'Szászfalvi László', 'city': 'Barcs', 'provider_U': 'HONLAP HU BT', 'payment_date': '2014-03-20', 'row_number': '1.0', 'invoice_reference': 'NQ95B3562948', 'purpose_CAT': '', 'gross_amount': '718000.0', 'invoice_issue_date': '2014-03-06', 'ID': '12', 'VAT_amount': '0.0', 'links': 'https://drive.google.com/file/d/0B1ve-jHPt_yfTXNjTDFUaUNXUmM/view?usp=drivesdk', 'provider': 'HONLAP HU BT', 'purpose': 'A honlap szolgáltatása', 'claimed_amount': '718000.0', 'product': 'Szászfalvi.hu weboldal'}
# _U = unified, pontok kiszedve meg szemet. (normalizalt)
# opten hozzaferes Bori, Marci, Lilla
import csv
import smart_csv_dictreader as SCD
import collections
D = collections.defaultdict(set)
import sys

import itertools
hanyszor_ceg = collections.defaultdict(lambda: collections.defaultdict(lambda: itertools.count(1)))
hanyszor_ceg2 = collections.defaultdict(lambda: collections.defaultdict(int))
with open('1.csv', 'r') as f:
  x = SCD.DictReader(f, lineterminator='\n', delimiter=',') 
# 'product', 'purpose_CAT', 'party', 'MP ID', 'invoice_reference', 'row_number', 'provider_U', 'city', 'gross_amount', 'VAT_amount', 'ID', 'net_amount', 'MP name', 'claimed_amount', 'links', 'invoice_issue_date', 'purpose', 'provider', 'payment_date'
  print('melyik ceg i) hany partnak ii) es melyiknek mennyit osszegre iii) es darabra iiii) es ez hogy aranyul a partteljeshez')
  for row in x:
    D[row['provider_U']].add(row['party'])
    hanyszor_ceg2[row['party']][row['provider_U']]= next(hanyszor_ceg[row['party']][row['provider_U']])
    if not row['provider_U']:#
      print(row)
  for (provi, szett) in sorted(D.items(), key=lambda v: len(v))[:5]:
    print(provi, szett, len(szett))
  import subprocess
  import io
  s = io.StringIO
  for party, provok in hanyszor_ceg2.items():  
    for prov, ertek in provok.items():
      print('{}/{},'.format(party.replace('\n', '' ).replace(',',''), prov.replace('\n', '').replace(',','').replace(',','')), ertek or 0, file=sys.stderr)
