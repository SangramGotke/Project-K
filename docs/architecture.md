# Architecture Blueprint: Audio-First MVP

## 1. High-Level Architecture
```text
+-------------------------------------------------------------+
|                      User / Trigger                         |
|   (Manual Trigger / Webhook: Topic, Language, Duration)     |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                        n8n Engine                           |
|  (Workflow Orchestrator running in Docker on OCI VM)        |
|                                                             |
|   [Stage 1: Research]   --> AI Provider (Router Abstraction)|
|   [Stage 2: Script]     --> AI Provider (Router Abstraction)|
|   [Stage 3: Script QC]  --> AI Provider (Router Abstraction)|
|   [Stage 4: TTS Synth]  --> TTS Engine (Router Abstraction) |
|   [Stage 5: Audio Post] --> Audio Normalization / Stitching |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                     PostgreSQL Database                     |
|  - jobs (id, topic, status, duration, created_at)           |
|  - scripts (id, job_id, content, version, word_count)       |
|  - audio_assets (id, job_id, provider, path, duration)      |
+-------------------------------------------------------------+
```

---

## 2. Abstraction Layers

### 2.1 AI Router Abstraction
The AI interaction layer handles prompting for Research, Scriptwriting, and Quality Control.
- Initial provider: Google Gemini / OpenAI / OpenRouter (swappable without workflow restructuring).
- Handles: Prompt template interpolation, JSON response formatting, rate limit retry.

### 2.2 TTS Router Abstraction
Converts script text to natural-sounding narration.
- Initial target: Single working, cost-effective provider (e.g. Edge-TTS, ElevenLabs, or OpenAI TTS).
- Output format: 44.1kHz or 48kHz WAV / MP3 with standard loudness normalization (-14 LUFS).

---

## 3. Storage & Persistence
- **Runtime Stack**: Located at `~/n8n-stack/` on OCI VM.
- **Docker Network**: `n8n_network` (bridge).
- **Volumes**:
  - `n8n_data`: Persistent workflow graphs, credentials, and execution history.
  - `postgres_data`: Persistent relational state for PostgreSQL 16.
- **Asset Directory**: Future mount for audio work artifacts (e.g. `/var/media/audio/`).
