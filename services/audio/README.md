# Audio Service & TTS Engine

## Overview
This service provides the text-to-speech abstraction layer and audio post-processing (normalization, format conversion) for the YouTube Content Automation Platform.

## Specifications
- **Standard Speaking Rate**: 140 - 150 wpm.
- **Audio Format**: 44.1kHz / 48kHz WAV or 192kbps MP3.
- **Loudness Normalization**: EBU R128 standard (-14 LUFS integrated loudness, -1 dBFS true peak) for YouTube platform compliance.
- **Pluggable TTS Providers**:
  - Provider A: Edge-TTS (Free, high-quality neural voices).
  - Provider B: ElevenLabs (Premium voice cloning/expressive narration).
  - Provider C: OpenAI TTS (`tts-1` / `tts-1-hd`).
