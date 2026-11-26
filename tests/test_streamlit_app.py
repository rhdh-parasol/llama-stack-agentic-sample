from unittest.mock import patch

import pytest

import streamlit_app


class TestRenderExchangeResponse:
    """
    tests for _render_exchange_response function.
    """

    @pytest.mark.parametrize("state", [None, {}])
    def test_falsy_state_returns_early_without_rendering(self, state):
        with patch("streamlit_app.st") as mock_st:
            result = streamlit_app._render_exchange_response(state)

        assert result is None
        assert mock_st.mock_calls == []
