from threading import Lock
from esipy import App, EsiClient, EsiSecurity
import key_config

class Client:

    DEFAULT_CONFIG_FILE = r"config/keys/esi_client_keys.yaml"

    CONFIG_REQUIREMENTS = [
        {"name": "swagger_spec_url", "description": "The URL of the swagger spec you wish to run against"},
        {"name": "esi_user_agent", "description": "A description of what your application is"},
    ]

    def __init__(self, config_file=DEFAULT_CONFIG_FILE):
        self.esi_app = None
        self.esi_client = None
        self.is_connected = False
        self.config = None
        self.config_file = config_file
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
        """
        Request the 'op' parameter with the given op_kwargs
        :param op:
        :param op_kwargs:
        :return:
        """
        self.connect()
        local_op = self.esi_app.op[op](**op_kwargs)
        return self.esi_client.request(local_op)

    def _open(self):
        """
        Initialize EsiPy
        :return:
        """
        config = key_config.load(self.config_file, self.CONFIG_REQUIREMENTS)

        self.esi_app = App.create(config['swagger_spec_url'])

        # init the security object
        '''
        esisecurity = EsiSecurity(
            app=esiapp,
            redirect_uri=config.ESI_CALLBACK,
            client_id=config.ESI_CLIENT_ID,
            secret_key=config.ESI_SECRET_KEY,
        )
        '''

        # init the client
        self.esi_client = EsiClient(
        #    security=esisecurity,
            cache=None,
            headers={'User-Agent': config['esi_user_agent']}
        )

