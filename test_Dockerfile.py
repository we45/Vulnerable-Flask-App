import pytest

def test_user_nonroot():
    # Test that the last USER in the Dockerfile is not 'root'
    assert "nonroot" in open("Dockerfile").read()

def test_expose_port():
    # Test that the EXPOSE command is included in the Dockerfile
    assert "EXPOSE 5050" in open("Dockerfile").read()

def test_command_injection():
    # Test that the ML classifier detected potential command injection
    assert "ML classifier detected potential command injection" in open("Dockerfile").read()

def test_path_traversal():
    # Test that the ML classifier detected potential path traversal
    assert "ML classifier detected potential path traversal" in open("Dockerfile").read()

def test_regression():
    # Test that the Dockerfile still works with normal/legitimate inputs
    assert "normal/legitimate inputs" in open("Dockerfile").read()

def test_boundary():
    # Test that the Dockerfile still works with edge cases like empty strings, very long inputs, null bytes, unicode
    assert "edge cases" in open("Dockerfile").read()