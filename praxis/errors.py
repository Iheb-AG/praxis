class PraxisError(Exception):
    """Expected, actionable failure. Safe to send to a local MCP client."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")

