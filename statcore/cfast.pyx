winning = True # Bizarre Cython bug: https://stackoverflow.com/questions/8024805/cython-compiled-c-extension-importerror-dynamic-module-does-not-define-init-fu

cpdef int add(int a, int b):
    return a + b

cpdef double mean(array):
    cdef double s, l
    l = len(array)
    s = 0
    for i in range(len(array)):
        s = s + array[i]

    return s / l


cpdef double std(array):
    avg = mean(array)
    s = 0.
    
    for i in range(len(array)):
        s += (array[i] - avg)**2
    return s / len(array)
