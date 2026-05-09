#!/bin/zsh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SNAPSHOT_PATH="$PROJECT_ROOT/snapshots/unyra-live-form-validated-2026-05-09.tar.gz"
TIMESTAMP="$(date +%Y-%m-%d-%H%M%S)"
BACKUP_PATH="$PROJECT_ROOT/snapshots/unyra-before-live-form-validated-restore-$TIMESTAMP.tar.gz"
TEMP_DIR="$(mktemp -d /tmp/unyra-live-form-restore.XXXXXX)"

cleanup() {
  rm -rf "$TEMP_DIR"
}

trap cleanup EXIT

if [[ ! -f "$SNAPSHOT_PATH" ]]; then
  echo "Snapshot live-form-validated nao encontrado em: $SNAPSHOT_PATH"
  exit 1
fi

echo "Criando backup do estado atual..."
tar \
  --exclude='./node_modules' \
  --exclude='./snapshots' \
  --exclude='./.next' \
  -czf "$BACKUP_PATH" \
  -C "$PROJECT_ROOT" \
  .

echo "Extraindo snapshot live-form-validated..."
tar -xzf "$SNAPSHOT_PATH" -C "$TEMP_DIR"

echo "Restaurando arquivos..."
rsync -a --delete \
  --exclude 'node_modules' \
  --exclude 'snapshots' \
  "$TEMP_DIR"/ "$PROJECT_ROOT"/

echo ""
echo "Checkpoint live-form-validated restaurado com sucesso."
echo "Backup do estado anterior salvo em:"
echo "$BACKUP_PATH"
echo ""
echo "Proximo passo:"
echo "npm run dev"
