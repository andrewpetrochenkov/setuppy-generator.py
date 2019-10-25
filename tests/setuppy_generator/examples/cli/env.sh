#!/usr/bin/env bash
{ set +x; } 2>/dev/null

export SETUP_NAME="name"
export SETUP_PACKAGES=""
export SETUP_LONG_DESCRIPTION=""
python -m setuppy_generator
