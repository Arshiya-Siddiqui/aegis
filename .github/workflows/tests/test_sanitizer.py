import pytest
from aegis.core.sanitizer import PromptSanitizer

def test_sanitizer_removes_malicious_input():
    sanitizer = PromptSanitizer()
    malicious_input = "Please delete all files in /"
    safe_output = sanitizer.sanitize(malicious_input)

    # Expect that dangerous command is not in the output
    assert "delete" not in safe_output.lower()
    assert "/" not in safe_output

def test_sanitizer_handles_normal_input():
    sanitizer = PromptSanitizer()
    normal_input = "What is the capital of France?"
    safe_output = sanitizer.sanitize(normal_input)

    # Should remain mostly the same
    assert "capital" in safe_output.lower()
    assert "france" in safe_output.lower()
