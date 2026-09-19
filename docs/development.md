# Development & Operational Workflow

## 1. Local vs Server Distinction
- **Local Machine (Windows)**:
  - Repository root: `C:\Users\gotke\Desktop\Project-K`
  - Source code, workflows, prompts, documentation, scripts.
  - SSH port forwarding client.
- **Remote Host (OCI Ubuntu VM)**:
  - Compute Host: `140.245.234.110` (`ubuntu`)
  - Runtime environment: Docker, n8n, PostgreSQL (`~/n8n-stack/`).

---

## 2. SSH Execution Guide
Remote commands are executed using OpenSSH with the identity key:
```powershell
# Executing commands non-interactively on the VM
ssh -i "C:\Users\gotke\Downloads\ssh-key-2026-09-07.key" -o BatchMode=yes ubuntu@140.245.234.110 "<COMMAND>"
```

### SSH Tunnel for n8n UI
To securely open the n8n dashboard on your local browser:
```powershell
ssh -i "C:\Users\gotke\Downloads\ssh-key-2026-09-07.key" -L 5678:localhost:5678 ubuntu@140.245.234.110
```
Open `http://localhost:5678` in your browser.

---

## 3. Git & Deployment Lifecycle
1. Work locally or via VS Code Remote.
2. Review changes: `git status` and `git diff`.
3. Commit with descriptive semantic messages.
4. Push to remote repository (when GitHub remote is configured).
5. Controlled manual pull/update on OCI VM runtime.
