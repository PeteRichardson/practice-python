
__all__ = ['bsort', 'bubblesort', 'clockutils', 'countbits', 'minmax']

import importlib
import sys
map(lambda x: importlib.import_module("."+x, 'palgorithms'), __all__)


def selftest(verbosity=1):
    for module_name in __all__:
        module = sys.modules['palgorithms.' + module_name]
        if hasattr(module, 'selftest'):
            module.selftest(verbosity)
