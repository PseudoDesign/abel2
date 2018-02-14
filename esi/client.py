from threading import Lock


class Client:

    def __init__(self):
        self.esi_app = None
        self.esi_client = None
        self.is_connected = False
        self._lock = Lock()

    def connect(self):
        """
        Connect to ESI if we're not already connected.
        :return:
        """
        if self.is_connected:
            return True
        else:
            with self._lock:
                # Checking the state again in case it was set before we got the lock
                if self.is_connected:
                    return True
                else:
                    self._open()
                    self.is_connected = True

    def execute_op(self, op, **op_kwargs):
        self.connect()
        local_op = self.esi_app.op[op](**op_kwargs)
        return self.esi_client.request(local_op)

    def _open(self):
        pass

