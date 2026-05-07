from llm import Llm

# NOTE: We default to the Gemini 2.5 GA models (Flash + Pro) because the
# Gemini 3 preview models require special access and most public Gemini API
# keys (especially free-tier AI Studio keys) cannot call them.

# Video variants always use Gemini.
VIDEO_VARIANT_MODELS = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GEMINI_2_5_PRO,
)

# All API keys available.

# Image (Create)

ALL_KEYS_MODELS_DEFAULT = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GPT_5_2_CODEX_HIGH,
    Llm.CLAUDE_OPUS_4_6,
    Llm.GEMINI_2_5_PRO,
)

# Text (Create)

ALL_KEYS_MODELS_TEXT_CREATE = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GPT_5_2_CODEX_HIGH,
    Llm.CLAUDE_OPUS_4_6,
    Llm.GEMINI_2_5_PRO,
)

# Image + Text (Update)

ALL_KEYS_MODELS_UPDATE = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GPT_5_4_2026_03_05_LOW,
)

# Key subset fallbacks.
GEMINI_ANTHROPIC_MODELS = (
    Llm.GEMINI_2_5_FLASH,
    Llm.CLAUDE_OPUS_4_6,
    Llm.GEMINI_2_5_PRO,
    Llm.CLAUDE_SONNET_4_6,
)
GEMINI_OPENAI_MODELS = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GPT_5_2_CODEX_HIGH,
    Llm.GEMINI_2_5_PRO,
    Llm.GPT_5_2_CODEX_MEDIUM,
)
OPENAI_ANTHROPIC_MODELS = (
    Llm.CLAUDE_OPUS_4_6,
    Llm.GPT_5_2_CODEX_HIGH,
    Llm.GPT_5_2_CODEX_MEDIUM,
)
GEMINI_ONLY_MODELS = (
    Llm.GEMINI_2_5_FLASH,
    Llm.GEMINI_2_5_PRO,
)
ANTHROPIC_ONLY_MODELS = (
    Llm.CLAUDE_OPUS_4_6,
    Llm.CLAUDE_SONNET_4_6,
)
OPENAI_ONLY_MODELS = (
    Llm.GPT_5_2_CODEX_HIGH,
    Llm.GPT_5_2_CODEX_MEDIUM,
)
