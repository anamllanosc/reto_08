# reto_08
## Cambios:
1. Decorador para manejar excepciones (```c_exception```) que permite que el programa continúe solicitando la entrada del usuario hasta que se ingrese un valor válido.
2. Los descuentos ya no se aplican en si con un metodo, si no con un decorador ```@discounts``` que se aplica al metodo ``` total_bill()```
3. Implementación de un generador en la clase Order. Sus elementos se imprimen a traves del metodo ```print_order()```.
4. Metodo ```__str__()``` para la clase ```MenuItem```, el cual permite imprimir correctamente los atributos de los objetos tanto en la lista de la orden como en la impresión del menú.
