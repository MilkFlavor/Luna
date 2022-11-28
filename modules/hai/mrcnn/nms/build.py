import os
import torch
from torch.utils.cpp_extension import load


sources = ['src/nms.c']
headers = ['src/nms.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/nms_cuda.c']
    headers += ['src/nms_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = ['src/cuda/nms_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

extra_compile_args = ['-fopenmp', '-std=c99']

nms = load(
    name='nms',
    sources=sources,
    extra_objects=extra_objects,
    extra_compile_args=extra_compile_args,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    verbose=True
)

if __name__ == '__main__':
    nms.build()
