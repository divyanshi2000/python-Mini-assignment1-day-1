class StringClass:
      def __init__(self):
        self.n= input('enter your string \n')
        print(len(self.n))
      def Con(self,String):
          list=[]
          list[1:0]=String
          return list
obj=StringClass()
str1=obj.n
print(obj.Con(str1))