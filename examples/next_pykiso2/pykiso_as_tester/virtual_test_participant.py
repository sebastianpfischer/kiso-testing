import pykiso

pykiso.load_config("./virtual.yaml")


from pykiso.lib.auxiliaries.dut_auxiliary import DUTAuxiliary
from pykiso.lib.auxiliaries.simulated_auxiliary import SimulatedAuxiliary
from pykiso.lib.auxiliaries.udsaux import UdsAuxiliary

aux_virtual = SimulatedAuxiliary.get_instance('aux_virtual')
aux_udp = DUTAuxiliary.get_instance('aux_udp')
aux_uds = UdsAuxiliary.get_instance('aux_uds')


@pykiso.task
def test_virtual_simulator():
    aux_udp.send_ping_command()
    aux_udp.send_fixture_command()
    report = aux_udp.wait_and_get_report()
    assert report == "OK"



if __name__ == "__main__":
    pykiso.expose.uart(...)
    pykiso.expose.rest_server("http://localhost:5000")
    # or
    pykiso.expose.prompt() # e.g. with https://python-prompt-toolkit.readthedocs.io/en/master/


    # Idea, there is an interface available as API. A 3rd party user can call something like "pykiso.setup()", "pykiso.run('test_virtual_simulator')"
