#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints info about Python bytes object
 * @p: pointer to PyObject object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *s;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	s = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", s);

	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", s[i]);

	putchar('\n');
}

/**
 * print_python_list - prints info about Python list object
 * @p: pointer to PyObject object
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

