# composio_router_mock.py

class ToolRouterMock:
    """
    Mock version of Composio Tool Router.
    Simulates tool execution for hackathon demo.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key

    def execute_tool(self, tool_name, params):
        """
        Simulate executing a tool.
        """
        if tool_name == "summarizer":
            text = params.get("text", "")
            # Simple mock summary (first 150 characters)
            summary = text[:150] + ("..." if len(text) > 150 else "")
            return {"summary": summary}
        # Add more tools if needed
        return {"summary": "Tool output placeholder."}


# Function to process multiple reports
def process_reports(texts):
    router = ToolRouterMock()
    summaries = []
    for text in texts:
        try:
            result = router.execute_tool("summarizer", {"text": text})
            summaries.append(result.get("summary", text))
        except Exception as e:
            print(f"⚠️ Error processing report: {e}")
            summaries.append(text)
    return summaries
