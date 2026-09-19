"""
Audio Master & Loudness Normalization Utility for Project-K
Applies EBU R128 loudness normalization (-14 LUFS, -1.5 dBFS True Peak) for YouTube standard.
"""

import subprocess
import sys
from pathlib import Path

TARGET_INTEGRATED_LUFS = -14.0
TARGET_TRUE_PEAK = -1.5
TARGET_LRA = 11.0


def normalize_audio(input_file: str, output_file: str) -> str:
    """
    Normalizes audio loudness to -14 LUFS using FFmpeg loudnorm filter.
    """
    src = Path(input_file)
    dst = Path(output_file)
    dst.parent.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        raise FileNotFoundError(f"Input audio file not found: {input_file}")

    loudnorm_filter = (
        f"loudnorm=I={TARGET_INTEGRATED_LUFS}:"
        f"TP={TARGET_TRUE_PEAK}:"
        f"LRA={TARGET_LRA}:print_format=summary"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(src),
        "-af", loudnorm_filter,
        "-ar", "44100",
        "-b:a", "192k",
        str(dst)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg normalization failed:\n{result.stderr}")

    return str(dst)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 master_audio.py <input.mp3> <output_master.mp3>")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]
    print(f"Mastering {in_path} to -14 LUFS -> {out_path}...")
    normalized = normalize_audio(in_path, out_path)
    print(f"Mastered successfully: {normalized}")
