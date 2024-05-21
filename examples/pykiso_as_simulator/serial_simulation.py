from pathlib import Path

import pykiso

pykiso.load_config(Path(__file__).parent.resolve() / "serial.yaml")


from pykiso.lib.auxiliaries.communication_auxiliary import CommunicationAuxiliary

sender = CommunicationAuxiliary.get_instance('com_aux_sender')
receiver = CommunicationAuxiliary.get_instance('com_aux_receiver')


if __name__ == "__main__":
    sender.start()
    receiver.start()

    sender.send_message("Hello, World!")
    assert receiver.receive_message() == "Hello, World!"

    sender.stop()
    receiver.stop()
