from ipykernel.kernelapp import IPKernelApp
from .kernel import KKernel

IPKernelApp.launch_instance(kernel_class=KKernel)
