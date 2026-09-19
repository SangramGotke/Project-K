"""
Edge-TTS Audio Synthesis Utility for Project-K
Free, neural text-to-speech engine utilizing Microsoft neural voices.
"""

import asyncio
import sys
from pathlib import Path

DEFAULT_VOICE = "en-US-ChristopherNeural"  # Authoritative, engaging documentary narrator
DEFAULT_RATE = "+0%"
DEFAULT_PITCH = "+0Hz"


async def synthesize_speech(
    text: str,
    output_path: str,
    voice: str = DEFAULT_VOICE,
    rate: str = DEFAULT_RATE,
    pitch: str = DEFAULT_PITCH
) -> str:
    """Synthesizes text input into a high-quality speech MP3 file."""
    try:
        import edge_tts
    except ImportError:
        raise RuntimeError(
            "edge-tts package is required. Install it using: pip install edge-tts"
        )

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out_file))

    return str(out_file)


if __name__ == "__main__":
    test_text = (
        "Imagine a place where gravity is so intense that not even light can escape. "
        "A boundary beyond which time itself grinds to a halt. "
        "Welcome to the mysterious world of black holes."
    )
    output_target = "output/test_sample.mp3"
    print(f"Synthesizing test narration to {output_target}...")
    asyncio.run(synthesize_speech(test_text, output_target))
    print("Synthesis complete.")
