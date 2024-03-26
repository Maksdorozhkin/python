# импортировать весь пакет нельзя, можно только из модуля
from pack.one_more_module import c  # пример импорта переменной с из ракета pack
import pack.import_module

print(pack.import_module.a)
