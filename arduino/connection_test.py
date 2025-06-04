from sensors.serial_interface import read_serial_data

def test_serial_mock(monkeypatch):
    def fake_serial(*args, **kwargs):
        class Fake:
            def __enter__(self): return self
            def __exit__(self, *a): pass
            def readline(self): return b'123\n'
        return Fake()

    monkeypatch.setattr("serial.Serial", fake_serial)
    assert read_serial_data() == 123