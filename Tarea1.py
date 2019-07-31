   

class node_list:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next


class linked_list:

	def __init__ (self):
		self.head= None

	def insertar(self,data):
		if not self.head:
			self.head=node_list(data=data)
			return
		x=self.head
		while x.next :
			x=x.next
		x.next=node_list(data=data)

	def modificar(self,data_se):
		x=self.head
		aux=None

		while x and x.data != data_se:
			aux=x
			x=x.next

		print(x.data)

        
     
		

	#def searchData(self,data_se):
	#	x=self.head
	#	aux=None
#
#		while x and x.data != data_se:
#			aux=x
#			x=x.next

#		print(x.data)
	
	
#	def searchData2(self,datas):
#		actual=self.head
#		encontrar=False
#
#		while actual != None and not encontrar:
#			
#			if actual.data == datas:
#				encontrar=True
#			else:
#				actual=actual.next
 #       
#		print(actual.data)
		


	def eliminar(self,data_delete): 
		x=self.head
		aux=None

		while x and x.data != data_delete:
			aux=x
			x=x.next
		if aux is None:
			self.head=x.next
		elif x:
			aux.next=x.next
			x.next=None
			


#	def delete_last(self):
#		temp=self.head
#		tem2=None
#
#		if temp == None:
#			print("lista vacia, no se puede eliminar el dato")
#
#		else:
#
#			while temp.next is not None :
#				temp2=temp
#				temp=temp.next
#
#			if temp == None:
#				temp.head=None
#			else:
#				temp2.next=None
#		
#		print("ultimo:",temp.data)


	def Listar(self):#the method called print_list
		
		node_list=self.head
		lista=" "

		if node_list==None:
			print("lista vacia")

		else:
		
			while node_list!= None:
			
				lista+=str(node_list.data)

				if node_list.next != None:
				
					
					lista+="-->"
			
				node_list=node_list.next
				
		print(lista)


import os
s=linked_list()
def menu():
    """
    os.system('cls')
    """
    print("Selecciona una opcion")
    print("\t1 - Insertar Dato")
    print("\t2 - Modificar Dato")
    print("\t3 - Listar Datos")
    print("\t4 - Eliminar Dato")
    print("\t9 - salir")



while True:
    menu()
    opcMenu = input("Inserta el numero de la opcion que desea realizar:")
    if opcMenu == "1":
        print("")
        valor = input("Ingrese el valor a insertar: ")
        s.insertar(valor)
        input("Pulsa enter tecla para continuar")
    elif opcMenu == "2":
        print("")
        valor = input("Ingrese el valor a modificar: ")
        s.modificar(valor)
        print("modificado")
        s.print_list()
        input("Has pulsado 2 pulsa una tecla para continuar")
    elif opcMenu == "3":
        print("")
        s.Listar()
        input("Pulsa enter tecla para continuar")
    elif opcMenu == "4":
        print("")
        valor = input("Ingrese el valor a eliminar: ")
        s.eliminar(valor)
        input("Pulsa enter tecla para continuar")
    elif opcMenu == "9":
        break
    else: 
        print("")
        input("tecla incorrecta, pulsa enter para continuar") 

menu()
