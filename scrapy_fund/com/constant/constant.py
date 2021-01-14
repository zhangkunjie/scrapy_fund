#coding:utf-8
class constant:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value):
      if name in self.__dict__:
          raise self.ConstError("can't change const %s" % name)
      if not name.isupper():
          raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
      self.__dict__[name] = value

import sys

sys.modules[__name__] = constant()
constant.HOST = 'localhost'
constant.USER= 'root'
constant.PASSWORD= '!PPxy168891'
constant.DB= 'fund'
constant.PORT= 3306
constant.CHARSET= 'utf8'
constant.FUND_CATEGORY= ['gp','hh','zq','zs','bb','qdii','lof','fof']
constant.ALLFUND_URL='http://fund.eastmoney.com/allfund.html'
constant.FUNRRANK_URL= 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&pi=1&pn=10000&dx=1&ft='
constant.MANAGER_URL= 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&st=asc'
constant.DTRANK_URL='http://fund.eastmoney.com/api/Dtshph.ashx?c=dwjz&s=desc&issale=1&page=1&psize=20000&t='
constant.GUPIAOZHANBI_URL='http://fund.eastmoney.com/Data/FundCompare_Interface.aspx?t=2&cb=data&bzdm='
constant.FUND_VALUE_URL='http://api.fund.eastmoney.com/f10/lsjz?'
constant.HOLD_FUND_IDS= ['007455','100055','000988','270023','002891','513050','006373','000934',
                 '006309','006328','457001','118001','001668','001691','005534','164906','100061','262001','002230','001832','161725','110022','009265','001382','163406','005827','110011','166011','162605']
constant.HOLD_FUND_IDS=['007455','100055','000988','270023','002891','513050','006373','000934','006309','006328','457001','118001','001668','001691','005534','164906','100061','262001','002230','001832',
                        '161725','110022','009265','001382','163406','005827','110011','166011','162605'
'163403',
'270012',
'161005',
'003494',
'007120',
'003096',
'519069',
'004241',
'206009',
'166006',
'002001',
'001410',
'166002',
'519736',
'001714',
'161606',
'519068',
'519712',
'180031',
'000362',
'001071',
'001500',
'519732',
'000251',
'000595',
'001371',
'040008',
'260101',
'000619',
'001985',
'660010',
'000577',
'000136',
'450009',
'519700',
'000566',
'110001',
'260116',
'570001',
'450003',
'202001'
'000172',
'161219',
'217005',
'530003',
'260112'
 ]
