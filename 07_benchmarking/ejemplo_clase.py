''' 
Ejemplo de benchmarking con pytest.
'''


from time import sleep


# Funciones a testear
def func_constant(n: int):

    sleep(0.01)
    return None


def func_linear(n: int):

    for _ in range(n):
        sleep(0.01)
    
    return None


def func_quadratic(n: int):

    for _ in range(n):
        for _ in range(n):
            sleep(0.01)

    return None


# Syntax para benchmarking

# Wrapper de configuración
def my_benchmark(option):
    n = 5  # Reducido de 25 para que la función cuadrática no tarde demasiado # TODO: cambio no modificó test
    option(n)


# Ejecucion de tests
def test_constant(benchmark):
    # benchmark(my_benchmark, func_constant)
    benchmark.pedantic(
        my_benchmark,
        args=(func_constant,),
        rounds=5,
        iterations=3
    )


def test_linear(benchmark):
    # benchmark(my_benchmark, func_linear)
    benchmark.pedantic(
        my_benchmark,
        args=(func_linear,),
        rounds=5,
        iterations=3
    )

def test_quadratic(benchmark):
    # benchmark(my_benchmark, func_quadratic)
    benchmark.pedantic(
        my_benchmark,
        args=(func_quadratic,),
        rounds=5,
        iterations=3
    )
