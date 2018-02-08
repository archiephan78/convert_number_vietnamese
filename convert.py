#!/usr/bin/python
#coding: utf-8 
from __future__ import unicode_literals

##list
list_19 = (u'không', u'một', u'hai', u'ba', u'bốn', u'năm', u'sáu',
         u'bảy', u'tám', u'chín', u'mười', u'mười một', u'mười hai',
         u'mười ba', u'mười bốn', u'mười lăm', u'mười sáu', u'mười bảy',
         u'mười tám', u'mười chín')
list_ten = (u'hai mươi', u'ba mươi', u'bốn mươi', u'năm mươi',
        u'sáu mươi', u'bảy mươi', u'tám mươi', u'chín mươi')

bil = ('',u'nghìn', u'triệu', u'tỷ', u'nghìn tỷ', u'trăm nghìn tỷ')

###conver 1-> 99
def convert_chuc(value):
  if value < 20:
    return list_19[value]
  for (dkey, dvalue) in ((k, 20 + (10 * v)) for (v, k) in enumerate(list_ten)):
    if dvalue + 10 > value:
      if value % 10:
        a = u'lăm'
        if list_19[value % 10] == u'một':
          a = u'mốt'
        else:
          a = list_19[value % 10]
        if list_19[value % 10] == u'năm':
          a = u'lăm'
        return dkey + ' ' + a
      return dkey

##convert 100 -> 999
def convert_tram(value):
  word = ''
  (mod, re) = (value % 100, value // 100)
  if re > 0:
    word = list_19[re] + u' trăm'
    if mod > 0:
      word = word + ' '
  if mod > 0 and mod < 10:
    if mod == 5:
      word = word != '' and word + u'lẻ năm' or word + u'năm'
    else:
      word = word != '' and word + u'lẻ ' + convert_chuc(mod) or word + convert_chuc(mod)
  if mod >= 10:
    word = word + convert_chuc(mod)
  return word

###convert tu 1000 -> 9 nghin ty
def convert_1k(value):
  for (dkey, dvalue) in ((v - 1, 1000 ** v) for v in range(len(bil))):
    if dvalue > value:
      mod = 1000 ** dkey
      dval = value // mod
      r = value - (dval * mod)
      re = convert_tram(dval) + u' ' + bil[dkey]
      if 99 >= r > 0:
        re = convert_tram(dval) + u' ' + bil[dkey] + u' lẻ'
      if r > 0:
        re = re + ' ' + convert_1k(r)
      return re  

###


if __name__ == "__main__":
  num = int(raw_input("Nhap: "))
  if len(str(num)) == 1 or len(str(num)) == 2:
    res =  convert_chuc(num)
  elif len(str(num)) == 3:
    res =  convert_tram(num)
  elif len(str(num)) >= 4:
    res = convert_1k(num) 
  print res
