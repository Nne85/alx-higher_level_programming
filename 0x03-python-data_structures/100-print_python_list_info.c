#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic information about Python lists
 * @p: Python object (must be a list)
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < PyList_Size(p); i++)
    {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

