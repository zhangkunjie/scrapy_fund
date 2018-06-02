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
constant.FUNRRANK_URL= 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&pi=1&pn=10000&dx=0&ft='
constant.HOST = 'localhost'
constant.USER= 'root'
constant.PASSWORD= 'mysql'
constant.DB= 'test'
constant.PORT= 3306
constant.CHARSET= 'utf8'
constant.FUND_CATEGORY= ['gp','hh','zq','zs','bb','qdii','lof']
constant.FUNRRANK_URL= 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&pi=1&pn=10000&dx=0&ft='
