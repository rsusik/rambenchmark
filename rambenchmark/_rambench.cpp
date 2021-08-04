#include <Python.h>
#include "rambench.hpp"

static char rambench_doc[] = "Examples for C/C++ python wrapping";


/*
 * Exported Methods declarations
 */
static PyObject* wrapper_perform_benchmark(PyObject *self, PyObject *args);

/*
 * Methods exported by this module
 */
static PyMethodDef rambench_methods[] = {
    {"perform_benchmark",  wrapper_perform_benchmark, METH_VARARGS},
    {NULL,      NULL}        /* Sentinel */
};


#if PY_MAJOR_VERSION >= 3
/* ! the struct name must respect the format: <name of the module> followed by string "module"*/
static struct PyModuleDef rambenchmodule = {
   PyModuleDef_HEAD_INIT,
   "rambench",   /* name of module */
   rambench_doc, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   rambench_methods
};
#endif


/*
 * Module initialization
 */
#if PY_MAJOR_VERSION >= 3
    PyMODINIT_FUNC PyInit_rambench(void)
#else
    PyMODINIT_FUNC initrambench(void)
#endif
{
#if PY_MAJOR_VERSION >= 3
    return PyModule_Create(&rambenchmodule);
#else
    (void) Py_InitModule("rambench", rambench_methods);
#endif
}

/*
 * Methods definition
 */

PyObject* wrapper_perform_benchmark(PyObject *self, PyObject *args)
{
    /*char *message = NULL;
    char *echoed = NULL;
    if (!PyArg_ParseTuple(args, "s", &message))
        Py_RETURN_NONE;

    echoed = echo(message);
    return Py_BuildValue("s", echoed);*/
    perform_benchmark();
    //Py_RETURN_NONE;
}

