# n8n Workflows Repository

This directory stores exported JSON definitions for all n8n workflows in the Project-K pipeline.

## Audio-First MVP Workflow Structure
1. `01-audio-first-pipeline.json`:
   - **Trigger**: Manual / Webhook (`topic`, `target_duration`, `language`, `style`).
   - **Node 1**: Content Input & validation.
   - **Node 2**: Research Agent (AI Provider Router).
   - **Node 3**: Scriptwriter Agent (AI Provider Router).
   - **Node 4**: Script QC Agent (Validation & Polish).
   - **Node 5**: TTS Generation (TTS Provider Router).
   - **Node 6**: Audio Normalization & Metadata storage.
