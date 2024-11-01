import pytest
from app import App

def test_app_test_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['test', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'greet' command
    out, err = capfd.readouterr()
    
    # Assert that 'Hello, World!' was printed to stdout
    assert "This is a test message!" in out, "The 'greet' command did not produce the expected output."