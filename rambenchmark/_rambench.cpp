#include <Python.h>
#include "rambench.hpp"

static char rambench_doc[] = "Performs RAM memory benchmark (speed).";

static PyObject* wrapper_perform_benchmark(PyObject *self, PyObject *args);

static PyMethodDef rambench_methods[] = {
    {"perform_benchmark",  wrapper_perform_benchmark, METH_VARARGS},
    {NULL, NULL}
};


#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef rambenchmodule = {
   PyModuleDef_HEAD_INIT,
   "rambench",
   rambench_doc,
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   rambench_methods
};
#endif

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

PyObject* wrapper_perform_benchmark(PyObject *self, PyObject *args) {
    perform_benchmark();
}

