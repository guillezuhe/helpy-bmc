from helpybmc import sendhelpy

def test_sendhelpy():
    assert sendhelpy.send() == 'Helpy!'