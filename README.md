# Set Preview Range to Manual Frame Range

This script sets the [Preview Range](https://docs.blender.org/manual/en/latest/editors/dope_sheet/navigating.html#view-menu) to the action's [Manual Frame Range](https://docs.blender.org/manual/en/latest/animation/actions.html#action-properties) property, so switching between actions isn't such a hassle.

## Usage

Once installed and ran, simply add set a preview range to begin with <kbd>P</kbd> in a timeline, then it will adapt to an action's Manual Frame Range once you change the action.

> [!warning]
> The script isn't bug-free at this moment, have a look at the current [issues](#issues)

## Install

This repository currently only provides a single script ([`/script.py`](/script.py)). Copy its contents into a new text data-block in Blender in the [Text Editor](https://docs.blender.org/manual/en/latest/editors/text_editor.html), then run it.

## Issues

- [ ] Bug: actions without a manual frame range set will set the preview range to (0, 0)
- [ ] Bug: changing an action's manual frame range won't update the preview range until the action is switched to from another action again
