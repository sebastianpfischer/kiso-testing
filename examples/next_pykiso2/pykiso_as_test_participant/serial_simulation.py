from pathlib import Path

import pykiso

pykiso.load_config(Path(__file__).parent.resolve() / "serial.yaml")


from pykiso.lib.auxiliaries.communication_auxiliary import CommunicationAuxiliary

sender = CommunicationAuxiliary.get_instance('com_aux_sender')
receiver = CommunicationAuxiliary.get_instance('com_aux_receiver')


if __name__ == "__main__":
    pykiso.expose.rest_server("http://localhost:5000")
    # or
    pykiso.expose.prompt() # e.g. with https://python-prompt-toolkit.readthedocs.io/en/master/
