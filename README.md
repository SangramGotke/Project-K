# YouTube Content Automation Platform (Project-K)

## 1. Project Overview
Project-K is an automated YouTube content-generation platform built with a modular, scalable architecture. The platform orchestrates the complete workflow from topic research to final media generation and publishing.

---

## 2. Current Phase: Audio-First MVP
We are strictly executing an **Audio-First MVP**. Video generation, visual assembly, and thumbnail creation are deferred until the audio generation pipeline is verified, robust, and reproducible.

### Pipeline Stages
```text
Topic
  ↓
Research
  ↓
Script Generation
  ↓
Script QC
  ↓
Text-to-Speech (TTS)
  ↓
Final Audio File (.mp3/.wav)
```

---

## 3. Infrastructure & Runtime Environment
- **Server**: Oracle Cloud Infrastructure (OCI) Compute Instance
- **OS**: Ubuntu 24.04 LTS (Kernel 6.17.0-1020-oracle)
- **Hostname**: `n8n-automationvm`
- **Public IP**: `140.245.234.110` (SSH key authentication only)
- **Container Engine**: Docker & Docker Compose
- **Orchestration**: n8n (`docker.n8n.io/n8nio/n8n:latest`) bound to `127.0.0.1:5678`
- **Database**: PostgreSQL 16 (`n8n-postgres`) on internal Docker network `n8n_network`

---

## 4. Secure Access & Local Tunneling
`n8n` is bound exclusively to `127.0.0.1` on the VM for security. To access the web interface from your local laptop browser:

```powershell
# Run from your local Windows machine:
ssh -i "C:\Users\gotke\Downloads\ssh-key-2026-09-07.key" -L 5678:localhost:5678 ubuntu@140.245.234.110
```
Then open `http://localhost:5678` in your local browser.

---

## 5. Development Principles
1. **Audio First**: Do not construct video pipelines before audio is rock-solid.
2. **Modular & Interchangeable**: Keep AI and TTS providers decoupled via router abstractions.
3. **Zero Secrets in Git**: All `.env`, `*.key`, `*.pem`, and credentials remain local/ignored.
4. **Controlled Deployments**: Code and workflows are versioned in Git; runtime deployment to OCI is intentional and verified.
