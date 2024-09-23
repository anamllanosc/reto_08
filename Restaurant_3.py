def c_exception(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
    return wrapper
def discounts(func):
    def wrapper(self, *args, **kwargs):
        # Llama al método original para calcular el total
        total = func(self, *args, **kwargs)

        # Cálculo de descuentos
        beverage_count = sum(isinstance(item, Beverage) for item in self.order_list)
        appetizer_count = sum(isinstance(item, Appetizer) for item in self.order_list)
        main_course_count = sum(isinstance(item, MainCourse) for item in self.order_list)

        discount = 0
        
        if 1 <= beverage_count <= 3 and appetizer_count == beverage_count and main_course_count == beverage_count:
            discount = total * 0.05  # 5% de descuento

        elif beverage_count >= 4 and appetizer_count >= 4 and main_course_count >= 4:
            discount = total * 0.10  # 10% de descuento

        elif beverage_count == 4 and main_course_count == 4:
            discount = total * 0.08  # 8% de descuento

        final_total = total - discount
        print(f"Descuento aplicado: - ${discount:.2f}")
        print(f"Total a pagar: ${final_total:.2f}")
        return final_total

    return wrapper
    
    

class MenuItem:
    def __init__(self,name:str,price:int):
        self.name=name #Nombre del producto
        self.price=price #Precio del producto

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Beverage(MenuItem): #Clase derivada de MenuItem (Bebidas)
    def __init__(self,name,price,temperature:str):
        super().__init__(name,price)# Hereda el inicializador de la super clase MenuItem
        self.temperature=temperature# Temperatura -> Atributo de unico de la clase Beverage

class Appetizer(MenuItem): #Clase derivada de MenuItem (Entradas)
    def __init__(self,name,price,pieces:int): 
        super().__init__(name,price) # Hereda el inicializador de la super clase MenuItem
        self.pieces=pieces# Numero de piezas -> Atributo de unico de la clase Appetizer

class MainCourse(MenuItem): #Clase derivada de MenuItem (Plato principal)
    def __init__(self,name,price,accompainments):
        super().__init__(name,price) # Hereda el inicializador de la super clase MenuItem
        self.accompainments=accompainments # Acompañamientos -> Atributo de unico de la clase MainCourse


class Order:
    def __init__(self):

        self.order_list=[] #Lista vacia para guardar los productos ingresados por el usuario
    @c_exception    
    def add_item(self): #metodo para crear la orden
        
        while True:
            item= str(input("Ingrese el producto que desea agregar a su pedido o (fin) para terminar: "))
            if item.lower()=="fin":
                return #El pedido terminara de hacerse cuando el usuario escriba "fin"
            elif item.lower() in menu_items:
                self.order_list.append(menu_items[item.lower()]) #Los productos de agregan a la lista "order_list unicamente si hacen parte de las claves del diccionario "menu_items"
                                                                      #A la lista se agraga el nombre objeto que corresponidia a la clave ingresada por el usiario
            else:
                raise Exception(f"El producto '{item}' no está en el menú.")
    
    @discounts
    def total_bill(self): #metodo para calcular el valor total a pagar por el pedido

        self.bill=0 #se inicializa la la cuenta en 0
        for product in self: #por cada producto en la lista de la orden del usuario
                self.bill+=product.price #se accede al atributo "price" de cada uno de los objetos y se acumulan a 0.
        
        return self.bill


    def __iter__(self): #Generador (iterador) de los productos que hacen parte de la orden
        for item in self.order_list:
            yield item

    def print_order(self):  # Nuevo metodo para imprimir la orden utilizando el iterador
        print("Orden actual:")
        for item in self:
            print(f"-{item}")


#Objetos de la clase Beverages
coffe=Beverage("Coffe",3000,"Hot")
chocolate=Beverage("Chocolate",3500,"Hot")
lemonade=Beverage("Lemonade",2500,"Cold")
water=Beverage("Water",2000,"Hot")

#Objetos de la clase Appetizer
spicy_shrimp=Appetizer("Spicy Shrimp",20000,"6")
mini_quiches=Appetizer("Mini Quiches",18000,"4")
fried_platains=Appetizer("Fried Platains",15000,"8")
capresse_salad=Appetizer("Capresse Salad",15000,"1")

#Objetos de la clase Main Course
grilled_salmon=MainCourse("Grilled Salmon",38000,"Accompainments= Mashed Potatoes and Mango Salad")
BBQ_ribs=MainCourse("Bbq Ribs",34000,"Accompainments= Fries")
stuffed_chicken=MainCourse("Stuffed Chicken",30000,"Accompainments= Parsley Rice")
vegetarian_curry=MainCourse("Vegetarian Curry",30000,"Accompainments= Pita Bread")

#Objeto de la clase orden 
order = Order()

#Diccionario con todos los productos del menu
menu_items={"coffe":coffe,"chocolate":chocolate,"lemonade":lemonade,"water":water,
            "spicy shrimp":spicy_shrimp,"mini quiches":mini_quiches,"fried platains":fried_platains,"capresse salad":capresse_salad,
            "grilled salmon":grilled_salmon,"bbq ribs":BBQ_ribs,"stuffed chicken":stuffed_chicken,"vegetarian curry":vegetarian_curry}


#Impresion del menu 
def product_generator(menu_items):
    for item in menu_items.values():
        print (item)


#Lista de descuentos
print("\n")
print("DESCUENTOS:\n-Entre uno y tres productos de cada categoria: 5% de descuento\n-Desde cuatro productos de cada categoria: 10% de descuento\n-Cuatro bebidas y cuatro platos principales:8% de descuento")
print("\n")

print(product_generator(menu_items))    
order.add_item()# Llama al método add_item() de la clase Order para agregar productos a la orden.
order.print_order()  # Imprimir la lista de la orden
order.total_bill()# Calcula el total de la factura llamando el método total_bill() de la clase Order.