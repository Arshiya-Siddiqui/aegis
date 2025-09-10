import re

class PromptSanitizer:
    """
    Sanitizer module to clean potentially malicious prompts before they reach the LLM.
    """

    def __init__(self):
        # Define dangerous patterns (regex)
        self.block_patterns = [
            r"ignore previous instructions",
            r"reveal.*training data",
            r"system prompt",
            r"jailbreak",
            r"bypass",
            r"override"
        ]

    def sanitize(self, prompt: str) -> str:
        """
        Detects and neutralizes malicious patterns in the user prompt.
        """
        sanitized_prompt = prompt
        for pattern in self.block_patterns:
            sanitized_prompt = re.sub(pattern, "[BLOCKED]", sanitized_prompt, flags=re.IGNORECASE)
        return sanitized_prompt
