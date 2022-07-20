# Melhorias no código

As recomendações são apenas para o código na pasta "App".

## Recomendações gerais:

 - Deve-se evitar definir nomes de pastas e ficheiros com maiúsculas
   (principalmente na primeira letra). Esta é uma recomendação seguida
   normalmente porque facilita a navegação em linha de comandos.
 - Ficheiros de dados, como `20170601.nc`, devem ficar numa pasta em separado,
   p.e. `data/`.
 - Ficheiros temporários (como os `.pkl`) podem ficar numa pasta `temp`
 - Evitar definir variáveis globais dentro de funções, usar o `return` para
   atribuir resultado da função a uma variável.
 - Definir variáveis de funcções (locais) diferentes das globais, caso
   contrário pode haver conflitos.
 
### Opcional:
 - Seguir alguma convenção de documentação de código (especialmente
   para funções). Por exemplo, PEP-8, PEP-257, utilização de docstrings.
 - PEP 8 para convenções de estilo de escrita do código.
 
## `concatenate_df.py`

 - Deve-se evitar definir variáveis globais dentro de funções. Como a variável
   `dfc1` já está a ser retornada pela função, acho que se pode apagar a l.13
   (redundante).
 - Há necessidade para a variável intermédia `result`?
 - Este ficheiro tem uma funcionalidade única: concatenar dois dataframes.
   Talvez, para nao ficar isolado, incluir num ficheiro com funções de
   (pré-)processamento dos dados?

## `data_availability.py`

 - Recomendo separar este código dos restantes: não faz parte do programa
   principal. É uma ferramenta para uma tarefa específica: obter a
   disponibilidade dos dados. Passar para uma pasta `aux` por exemplo (no mesmo
   nível que `app`)
 - Opcional: não é necessário atribuir aliases (`import nome_modulo as alias`)
   para todos os módulos. Facilita na escrita do código se funções do módulo
   forem usada muitas veses, mas pode complicar a compreensão do código.
 - Mantém-se a necessidade de evitar variáveis globais (ver acima). 
 - Para ter o retorno da variável da função, executa-se da seguinte forma:

   ```
   count = wind_speed_count(var)
   ```
   
 - Evitar ter variáveis locais em funções que já estjeam definidas globalmente.
 - Documentação: pode-se retirar o "This function" em todos os comentários,
   para não ser repetitivo. 

## `data_gathering.py`

 - 1 função: extrai e concatena (apenas 1 sónico).
 
## `dates_array.py`

 - Trabalhando com módulos, evitar executar código nos módulos (exceto
   definição de variáveis), qualquer execução deve constar no script principal.
   Isto pois as operações são executadas ao fazer `import`, que é normalmente
   feito no inicio do código.
 - 1 função: processamento das datas.

## `mode_01`

 - O que varia para os outros modos é o input.
 - Tentar uniformizar inputs, para não precisar dos vários modos.
 - Agrupar código de Input em funções num ficheiro separado, p.e.,
   `input_output.py`, pode evitar código repetido entre os módulos.
  
## `mode_02 - 05`

 - ver anterior.
 
## `process_routines_compiled.py`

 - Passar nome para `processing_functions.py`.
 - O nome da função `process_routines` parece algo genérico, penso que a função
   faz o processamento total para 1 sónico, talvez `process_sonic`.

## `time_period_adjust.py`

 - Funções de resampling temporal.
 - Sugiro a mudança do nome para `time_process`, ou algo assim, e passar a
   função de `dates_array` para aqui (tudo o que tem a ver com tempo num único
   módulo).

## `save_export_function.py`

 - Talvez colocar dentro de `input_output.py`, que tinha sido sugerido atrás.
