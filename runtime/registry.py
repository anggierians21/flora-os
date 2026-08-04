"""
Flora Runtime Registry

Single Source of Truth
untuk seluruh knowledge yang harus dimuat
ke Runtime.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REGISTRY = {
    "brain": ROOT / "brain",
    "organization": ROOT / "knowledge" / "organization",
    "programs": ROOT / "knowledge" / "programs",
    "operations": ROOT / "knowledge" / "operations",
    "agents": ROOT / "knowledge" / "agents",
    "islamic": ROOT / "knowledge" / "islamic",
    "learning": ROOT / "knowledge" / "learning",
}
