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
constant.DB= 'test'
constant.PORT= 3306
constant.CHARSET= 'utf8'
constant.FUND_CATEGORY= ['gp','hh','zq','zs','bb','qdii','lof','fof']
constant.FUNRRANK_URL= 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&pi=1&pn=10000&dx=1&ft='
constant.MANAGER_URL= 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&st=asc'
constant.DTRANK_URL='http://fund.eastmoney.com/api/Dtshph.ashx?c=dwjz&s=desc&issale=1&page=1&psize=20000&t='
constant.GUPIAOZHANBI_URL='http://fund.eastmoney.com/Data/FundCompare_Interface.aspx?t=2&cb=data&bzdm='
constant.FUND_VALUE_URL='http://api.fund.eastmoney.com/f10/lsjz?'
constant.HOLD_FUND_IDS= ['007455','100055','000988','270023','002891','513050','006373','000934',
                 '006309','457001','118001','001668','001691','005534','164906','100061',
                  '262001','002230',
                  '001832','161725','110022','009265','001382','163406','005827','110011','166011','162605']