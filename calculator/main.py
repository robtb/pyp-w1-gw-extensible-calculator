from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *

def create_new_calculator(operations=None): #pass in operations
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    return {
        'operations': operations or {},
        'history': []
    }

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    for param in params:
        if type(param) != int and type(param) != float:
            raise InvalidParams('Given params are invalid.')    
    if operation not in get_operations(calc):
        raise InvalidOperation("error")
    else:
        if len(params) == 1: #Checks before operating
            return params[0]
        else:
            result = calc['operations'][operation](*params) #asterisk necessary to separate list before passing it
            now = datetime.now()
            calc['history'].append((now.strftime('%Y-%m-%d %H:%M:%S'), operation, params, result))
            return result
    

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if type(operation) is dict:
        for key, value in operation.items():
            calc['operations'][key] = value
    else:
        raise InvalidOperation('Given operation is invalid.')
    #calc['operation'].update(operation)




def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'].keys()) #returns keys of operations


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    return calc['history']


def reset_history(calc):
    calc['history'] = []


def repeat_last_operation(calc):
    if len(calc['history']) > 0:
        return calc['history'][-1][-1]
    else:
        return None
