"""
End-to-End Audio Pipeline Runner for Project-K
Takes approved script text, synthesizes speech, and masters loudness to -14 LUFS.
"""

import asyncio
import json
import sys
from pathlib import Path

from generate_tts import synthesize_speech
from master_audio import normalize_audio


async def run_audio_pipeline(
    text: str,
    job_id: str,
    output_dir: str = "output",
    voice: str = "en-US-ChristopherNeural"
) -> dict:
    """Executes Stage 05 (TTS) and Stage 06 (Mastering) for an approved script."""
    base_dir = Path(output_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    raw_audio_path = base_dir / f"{job_id}_raw.mp3"
    mastered_audio_path = base_dir / f"{job_id}_master.mp3"

    print(f"[Stage 05 - TTS] Synthesizing speech with voice '{voice}'...")
    await synthesize_speech(text, str(raw_audio_path), voice=voice)

    print(f"[Stage 06 - Master] Normalizing loudness to -14 LUFS standard...")
    normalize_audio(str(raw_audio_path), str(mastered_audio_path))

    return {
        "job_id": job_id,
        "raw_audio": str(raw_audio_path),
        "mastered_audio": str(mastered_audio_path),
        "voice": voice,
        "target_lufs": -14.0,
        "status": "COMPLETED"
    }


if __name__ == "__main__":
    sample_text = (
        "Welcome to the event horizon. Beyond this boundary, the escape velocity exceeds the speed of light. "
        "At the center of our Milky Way lies Sagittarius A*, with the gravitational pull of four million suns."
    )
    result = asyncio.run(run_audio_pipeline(sample_text, "test_job_001"))
    print(json.dumps(result, indent=2))
