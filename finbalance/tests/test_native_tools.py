"""Tests for the native function-calling tool agent."""

import json
import unittest

from finbalance.benchmark.ablations import ABLATION_MATRICES
from finbalance.benchmark.tools import (
    TOOL_CALCULATOR,
    TOOL_VARIANT_NATIVE_FULL_TOOL_AGENT,
    TOOLS_BY_VARIANT,
    run_native_tool_agent_completion,
)
from finbalance.tests.test_ablations import _record, _submission


class _NativeSequenceClient:
    """Fake client that yields OpenAI-shaped payloads, optionally with tool_calls."""

    def __init__(self, turns):
        self.model = "fake/native"
        self.turns = list(turns)
        self.calls = []

    def complete_messages(self, messages, *, temperature, max_tokens, timeout, tools=None):
        self.calls.append({"messages": [dict(m) for m in messages], "tools": tools})
        if not self.turns:
            raise AssertionError("fake native client ran out of turns")
        turn = self.turns.pop(0)
        if "tool_calls" in turn:
            message = {"role": "assistant", "content": None, "tool_calls": turn["tool_calls"]}
            text = ""
        else:
            message = {"role": "assistant", "content": turn["text"]}
            text = turn["text"]
        return text, {"choices": [{"message": message}], "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}


class NativeToolAgentTest(unittest.TestCase):
    def test_tool_call_round_trip_then_final_answer(self):
        record = _record()
        client = _NativeSequenceClient(
            [
                {
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {"name": TOOL_CALCULATOR, "arguments": json.dumps({"expression": "2*3"})},
                        }
                    ]
                },
                {"text": _submission(record)},
            ]
        )
        result = run_native_tool_agent_completion(
            record,
            client,
            "prompt",
            allowed_tools=TOOLS_BY_VARIANT[TOOL_VARIANT_NATIVE_FULL_TOOL_AGENT],
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(len(result.tool_calls), 1)
        self.assertEqual(result.tool_calls[0]["tool"], TOOL_CALCULATOR)
        self.assertEqual(result.tool_calls[0]["result"]["result"], 6.0)
        self.assertEqual(result.tool_call_failures, 0)
        self.assertIn("has_inconsistency", result.response_text)
        # first request declared the native tool schemas
        self.assertEqual(len(client.calls[0]["tools"]), 4)
        # tool result flowed back as a role=tool message
        roles = [m["role"] for m in client.calls[1]["messages"]]
        self.assertIn("tool", roles)

    def test_malformed_arguments_counted_as_failure(self):
        record = _record()
        client = _NativeSequenceClient(
            [
                {
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {"name": TOOL_CALCULATOR, "arguments": "{not json"},
                        }
                    ]
                },
                {"text": _submission(record)},
            ]
        )
        result = run_native_tool_agent_completion(
            record,
            client,
            "prompt",
            allowed_tools=TOOLS_BY_VARIANT[TOOL_VARIANT_NATIVE_FULL_TOOL_AGENT],
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(result.tool_call_failures, 1)
        self.assertFalse(result.tool_calls[0]["result"]["ok"])

    def test_no_tool_use_returns_immediately(self):
        record = _record()
        client = _NativeSequenceClient([{"text": _submission(record)}])
        result = run_native_tool_agent_completion(
            record,
            client,
            "prompt",
            allowed_tools=TOOLS_BY_VARIANT[TOOL_VARIANT_NATIVE_FULL_TOOL_AGENT],
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(result.tool_calls, [])
        self.assertIn("has_inconsistency", result.response_text)

    def test_variant_registered_in_coverage_matrix(self):
        names = [spec.name for spec in ABLATION_MATRICES["coverage"]]
        self.assertIn("tool_native_full_tool_agent", names)


if __name__ == "__main__":
    unittest.main()
