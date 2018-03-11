from ipykernel.kernelbase import Kernel
from subprocess import check_output


class KKernel(Kernel):
    implementation = 'K'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "K kernel - wrap K in ipython kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        print("Execute call: ", code)
        result = check_output(code, shell=True).decode('utf-8')
        print(result)
        if not silent:
            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
                }


if __name__ == '__main__':
    kernel = KKernel()
    kernel.do_execute("dir", silent=False)
