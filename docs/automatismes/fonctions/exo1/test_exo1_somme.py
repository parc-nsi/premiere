import io
sortie = io.StringIO() 
benchmark = ['somme([]) == None', 'somme([1]) == 1', 'somme([1,2]) == 3', 'somme([-1,1]) == 0']
for k, test in enumerate(benchmark, 1):
    if eval(test):
        sortie.write(f'Test {k} réussi :  {test} \\n')
    else:
        sortie.write(f'Test {k} échoué :  {test} \\n')
        break
sortie.write("Bravo !!!")
sortie.getvalue()
