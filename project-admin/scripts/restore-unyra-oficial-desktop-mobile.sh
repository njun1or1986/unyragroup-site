#!/bin/zsh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SNAPSHOT_PATH="$PROJECT_ROOT/snapshots/unyra-oficial-desktop-mobile.tar.gz"
TIMESTAMP="$(date +%Y-%m-%d-%H%M%S)"
BACKUP_PATH="$PROJECT_ROOT/snapshots/unyra-before-oficial-restore-$TIMESTAMP.tar.gz"
TEMP_DIR="$(mktemp -d /tmp/unyra-oficial-restore.XXXXXX)"

cleanup() {
  rm -rf "$TEMP_DIR"
}

trap cleanup EXIT

if [[ ! -f "$SNAPSHOT_PATH" ]]; then
  echo "Versao oficial nao encontrada em: $SNAPSHOT_PATH"
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

echo "Extraindo versao oficial..."
tar -xzf "$SNAPSHOT_PATH" -C "$TEMP_DIR"

echo "Restaurando arquivos da versao oficial..."
rsync -a --delete \
  --exclude 'node_modules' \
  --exclude 'snapshots' \
  "$TEMP_DIR"/ "$PROJECT_ROOT"/

echo ""
echo "Versao oficial restaurada com sucesso."
echo "Backup do estado anterior salvo em:"
echo "$BACKUP_PATH"
echo ""
echo "Proximo passo:"
echo "npm run dev"
