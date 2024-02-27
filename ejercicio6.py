
from enum import Enum

class Categoria(Enum):
    SALARIO_FIJO = 1
    A_COMISION = 2

class Antiguedad(Enum):
    MENOS_DE_DOS = 1
    DE_DOS_A_CINCO = 2
    MAS_DE_CINCO = 3

class Empleado:
    def __init__(self, dni, nombre, apellido, anno_ingreso, categoria, clientes_captados, monto_por_cliente, salario_minimo, salario_fijo, antiguedad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anno_ingreso = anno_ingreso
        self.categoria = categoria
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente
        self.salario_minimo = salario_minimo
        self.salario_fijo = salario_fijo
        self.antiguedad = antiguedad


    def calcular_salario(self):
        if self.categoria == Categoria.A_COMISION:
            salario = self.clientes_captados * self.monto_por_cliente
            print( salario)
            if salario < self.salario_minimo:
                salario = self.salario_minimo
            return salario
        else:
            salario = self.salario_fijo
            if self.antiguedad == Antiguedad.DE_DOS_A_CINCO.value:
                salario *= 1.05
            elif self.antiguedad == Antiguedad.MAS_DE_CINCO.value:
                salario *= 1.10
            return salario

class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_salarios(self):
        for empleado in self.empleados:
            salario = empleado.calcular_salario()
            print(f"{empleado.nombre} {empleado.apellido}: ${salario}")

    def empleado_con_mas_clientes(self):
        max_clientes = -1
        empleado_max_clientes = None
        for empleado in self.empleados:
            if empleado.categoria == Categoria.A_COMISION:
                if empleado.clientes_captados > max_clientes:
                    max_clientes = empleado.clientes_captados
                    empleado_max_clientes = empleado
        return empleado_max_clientes

# Creación de empleados de ejemplo
empresa = Empresa()
empresa.agregar_empleado(Empleado("11111111", "Juan", "Perez", 2019, Categoria.SALARIO_FIJO, 2, 200, 10000, 20000, Antiguedad.MAS_DE_CINCO.value ))
empresa.agregar_empleado(Empleado("22222222", "Maria", "Gomez", 2018, Categoria.SALARIO_FIJO, 2, 200, 10000, 20000, Antiguedad.MENOS_DE_DOS.value))
empresa.agregar_empleado(Empleado("33333333", "Carlos", "Lopez", 2020, Categoria.A_COMISION, 10, 200, 10000, 20000, 0))
empresa.agregar_empleado(Empleado("44444444", "Ana", "Martinez", 2017, Categoria.A_COMISION, 20, 200, 10000, 20000, 0))
empresa.agregar_empleado(Empleado("55555555", "Luis", "Rodriguez", 2016, Categoria.SALARIO_FIJO, 2, 200, 10000, 20000, Antiguedad.DE_DOS_A_CINCO.value))
empresa.agregar_empleado(Empleado("66666666", "Laura", "Diaz", 2021, Categoria.A_COMISION, 25, 200, 10000, 20000, 0))
empresa.agregar_empleado(Empleado("77777777", "Pedro", "Sanchez", 2015, Categoria.SALARIO_FIJO, 2, 200, 10000, 20000, Antiguedad.MAS_DE_CINCO.value))
empresa.agregar_empleado(Empleado("88888888", "Sofia", "Fernandez", 2019, Categoria.A_COMISION, 8, 200, 10000, 20000, 0))
empresa.agregar_empleado(Empleado("99999999", "Diego", "Garcia", 2018, Categoria.SALARIO_FIJO, 2, 200, 10000, 20000, Antiguedad.MENOS_DE_DOS.value))
empresa.agregar_empleado(Empleado("10101010", "Paula", "Ramirez", 2017, Categoria.A_COMISION, 40, 200, 10000, 20000, 0))

# Mostrar salarios de los empleados
print("Salarios de los empleados:")
empresa.mostrar_salarios()

# Empleado con más clientes captados
empleado_max_clientes = empresa.empleado_con_mas_clientes()
if empleado_max_clientes:
    print(f"\nEmpleado con más clientes captados: {empleado_max_clientes.nombre} {empleado_max_clientes.apellido}")
else:
    print("\nNo hay empleados a comisión para determinar quién tiene más clientes captados.")
