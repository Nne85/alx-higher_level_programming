#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <bytesobject.h>
/**
 * print_python_list - Prints some basic info about Python lists
 * @p: PyObject *
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, len;
    PyObject *obj;

    len = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", len);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < len; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: PyObject *
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, len;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    len = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", len);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes:", len + 1 < 10 ? len + 1 : 10);
    for (i = 0; i < len + 1 && i < 10; i++)
        printf(" %02x", (unsigned char)str[i]);
    printf("\n");
}

